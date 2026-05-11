---
spec: auto-install
phase: requirements
created: 2026-05-11
---

# Requirements: auto-install

## Overview

Eliminar o passo manual `/<pkg>-setup` após `/plugin install <pkg>@myskills`. Quando o usuário instala um plugin do marketplace `myskills`, as skills standalone declaradas no README do plugin devem ser bootstrapped automaticamente na primeira sessão pós-install, de forma silenciosa, idempotente e tolerante a falhas. Abordagem escolhida: `SessionStart` hook + marker em `${CLAUDE_PLUGIN_DATA}` (Alternativa B do research), executando `npx skills add ...` uma vez por versão do plugin. Decisão registrada em ADR-001 (a criar). Implementação de referência em `plugins/workflow`; demais plugins ficam para iterações futuras.

## User Stories

### US-1 — Primeira instalação de um plugin

**Como** Felipe (ou alguém que acabou de descobrir o `myskills`)
**Quero** rodar `/plugin install workflow@myskills` e ter as skills standalone disponíveis sem comando extra
**Para que** a experiência de onboarding seja de 1 passo, não 2

**Acceptance Criteria:**
- **Dado** que o plugin `workflow` nunca foi instalado neste host
- **Quando** o usuário roda `/plugin install workflow@myskills` e abre uma nova sessão Claude Code
- **Então** o hook `SessionStart` executa `bootstrap.sh`, que roda os `npx skills add ...` declarados, cria o marker `.bootstrapped-v<version>` em `${CLAUDE_PLUGIN_DATA}`, e as skills `gsd-*`, `find-skills` e `1password` ficam disponíveis sem o usuário digitar nada
- **E** o terminal mostra apenas `[myskills/workflow] instalando skills standalone…` seguido de `[myskills/workflow] ok`

### US-2 — Sessão de retorno (sem re-bootstrap)

**Como** Felipe usando o `workflow` no dia-a-dia
**Quero** que sessões subsequentes abram instantaneamente
**Para que** o startup do Claude Code não pague custo de instalação repetida

**Acceptance Criteria:**
- **Dado** que o marker `.bootstrapped-v<version>` já existe em `${CLAUDE_PLUGIN_DATA}`
- **Quando** uma nova sessão é iniciada (`startup` ou `resume`)
- **Então** o `bootstrap.sh` retorna em <100ms sem executar nenhum `npx skills add`
- **E** nenhuma linha é impressa no terminal

### US-3 — Bump de versão do plugin

**Como** Felipe publicando `workflow@0.2.0` com standalones novos
**Quero** que o bootstrap rode de novo automaticamente para os usuários existentes
**Para que** standalones novos cheguem sem pedir `/workflow-setup` manual

**Acceptance Criteria:**
- **Dado** que existe `.bootstrapped-v0.1.0` em `${CLAUDE_PLUGIN_DATA}` e o `plugin.json` foi atualizado para `version: 0.2.0`
- **Quando** uma nova sessão é iniciada
- **Então** o `bootstrap.sh` detecta ausência de `.bootstrapped-v0.2.0`, executa os `npx skills add` (idempotentes), e cria o novo marker
- **E** o marker antigo `.bootstrapped-v0.1.0` permanece (não polui mas também não atrapalha)

### US-4 — Primeira sessão offline

**Como** Felipe instalando o plugin em avião / rede ruim
**Quero** que o Claude Code abra normalmente mesmo se o bootstrap falhar
**Para que** falta de rede não vire startup quebrado

**Acceptance Criteria:**
- **Dado** que a máquina está offline e o marker ainda não existe
- **Quando** uma nova sessão é iniciada
- **Então** `bootstrap.sh` tenta os `npx skills add`, captura o erro, grava o stderr em `${CLAUDE_PLUGIN_DATA}/bootstrap.log`, **não cria o marker**, imprime `[myskills/workflow] bootstrap adiado (offline) — ver bootstrap.log`, e sai com código 0
- **E** o Claude Code segue startup normal sem bloquear
- **E** a próxima sessão (já online) re-executa o bootstrap automaticamente

### US-5 — Fallback manual via `/workflow-setup`

**Como** Felipe debugando um bootstrap quebrado ou forçando re-instalação
**Quero** continuar tendo o comando `/workflow-setup` disponível
**Para que** eu possa reparar estado sem mexer no marker manualmente

**Acceptance Criteria:**
- **Dado** que o plugin está instalado
- **Quando** o usuário roda `/workflow-setup`
- **Então** o comando executa os mesmos `npx skills add` do bootstrap, independente do marker
- **E** o README documenta o comando como "fallback manual / re-execução"

### US-6 — Documentação e descoberta

**Como** alguém lendo o README do `workflow`
**Quero** ver instalação em 1 comando
**Para que** o caminho feliz seja óbvio e o fallback fique secundário

**Acceptance Criteria:**
- **Dado** o `plugins/workflow/README.md` atualizado
- **Quando** o leitor olha a seção de instalação
- **Então** a primeira instrução é `/plugin install workflow@myskills` (sem step `/workflow-setup` no caminho principal)
- **E** `/workflow-setup` aparece numa subseção "Re-instalação / fallback"
- **E** o ADR-001 está linkado em `docs/adr/ADR-001-auto-install-strategy.md`

### US-7 — Replicabilidade do padrão

**Como** Felipe planejando rolar a mesma solução para `design`, `programming`, `marketing`
**Quero** que o padrão (hook + script) seja copiável em <5 minutos por plugin
**Para que** o rollout das próximas specs seja mecânico

**Acceptance Criteria:**
- **Dado** o `workflow` como implementação de referência
- **Quando** Felipe replica para outro plugin
- **Então** basta: (1) copiar `.claude-plugin/hooks.json`, (2) copiar `scripts/bootstrap.sh` trocando os blocos `npx skills add`, (3) garantir que `PLUGIN_VERSION` esteja sincronizado com `plugin.json`
- **E** o ADR-001 lista esses 3 passos explicitamente

## Functional Requirements

| ID | Requisito | Prioridade | Como verificar |
|----|-----------|-----------|----------------|
| FR-1 | `plugins/workflow/.claude-plugin/hooks.json` DEVE conter um evento `SessionStart` com `matcher: "startup\|resume"` apontando para `${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.sh` com `timeout: 120`. | Alta | `jq` no arquivo confere shape |
| FR-2 | `plugins/workflow/scripts/bootstrap.sh` DEVE ser executável (`chmod +x`), usar shebang `#!/usr/bin/env bash` e `set -uo pipefail` (sem `-e` global para permitir fail-soft por bloco). | Alta | `test -x` + leitura |
| FR-3 | O script DEVE ler a versão do plugin a partir do `plugin.json` co-localizado (via `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`, parse com `grep`/`sed` para evitar dependência de `jq`) e usar como sufixo do marker: `${CLAUDE_PLUGIN_DATA}/.bootstrapped-v<version>`. | Alta | Inspeção do script |
| FR-4 | Se o marker existir, o script DEVE sair com código 0 em <100ms sem qualquer output. | Alta | Bench manual com `time` |
| FR-5 | Se o marker NÃO existir, o script DEVE imprimir `[myskills/workflow] instalando skills standalone…` em stdout, executar os `npx skills add ...` declarados, redirecionar stdout/stderr de cada `npx` para `${CLAUDE_PLUGIN_DATA}/bootstrap.log` (append, com timestamp por bloco). | Alta | Teste manual com plugin limpo |
| FR-6 | Se todos os blocos `npx skills add` retornarem sucesso, o script DEVE criar o marker (`touch`) e imprimir `[myskills/workflow] ok`. | Alta | Teste manual |
| FR-7 | Se qualquer bloco falhar, o script DEVE **não criar** o marker, imprimir `[myskills/workflow] bootstrap adiado — ver ${CLAUDE_PLUGIN_DATA}/bootstrap.log`, e sair com código 0 (fail-soft, não bloqueia startup). | Alta | Teste manual com rede desligada |
| FR-8 | Os blocos `npx skills add` DEVEM incluir flag `-y` (não-interativo) e fontes idênticas às listadas hoje em `plugins/workflow/commands/setup.md` (GSD, find-skills, 1password). | Alta | Diff entre `setup.md` e `bootstrap.sh` |
| FR-9 | O comando slash `/workflow-setup` (`plugins/workflow/commands/setup.md`) DEVE permanecer funcional e DEVE executar o mesmo conjunto de fontes — sem checar marker. | Alta | Rodar `/workflow-setup` após bootstrap automático: deve reinstalar |
| FR-10 | `plugins/workflow/README.md` DEVE ser atualizado: instalação primária = `/plugin install workflow@myskills` apenas; `/workflow-setup` aparece como fallback numa subseção. | Alta | Inspeção do README |
| FR-11 | `docs/adr/ADR-001-auto-install-strategy.md` DEVE ser criado, contendo: contexto, alternativas A–E (resumo), decisão, consequências, e os 3 passos de replicação para outros plugins. | Alta | Arquivo existe e referencia research.md |
| FR-12 | Teste manual documentado: desinstalar `workflow` → remover `${CLAUDE_PLUGIN_DATA}/.bootstrapped-*` → reinstalar via `/plugin install workflow@myskills` → abrir nova sessão → verificar que `gsd-*` aparece em `/help` sem rodar `/workflow-setup`. | Alta | Checklist no PR body |
| FR-13 | O script NÃO DEVE solicitar input do usuário em nenhuma hipótese (nenhum `read`, nenhum prompt interativo). | Alta | Inspeção + teste |

## Non-Functional Requirements

| ID | Requisito | Métrica | Alvo |
|----|-----------|---------|------|
| NFR-1 | Performance (sessão de retorno) | Tempo de execução do `bootstrap.sh` quando marker já existe | <100ms |
| NFR-2 | Performance (primeira sessão) | Timeout do hook `SessionStart` | ≤120s (limite do `timeout` no `hooks.json`) |
| NFR-3 | Não bloqueia UI | Hook NÃO DEVE travar startup mesmo em falha | Exit code 0 sempre, exceto em bug do próprio script |
| NFR-4 | Idempotência | Re-execução do `bootstrap.sh` mesma versão | Marker presente → no-op; marker ausente → re-tenta sem efeitos colaterais destrutivos |
| NFR-5 | Observabilidade | Local fixo do log | `${CLAUDE_PLUGIN_DATA}/bootstrap.log`, append, com timestamp ISO-8601 por execução |
| NFR-6 | Portabilidade | Sistemas suportados | macOS (bash 3.2+ via `/usr/bin/env bash`) e Linux (bash ≥ 4). Windows fora de escopo |
| NFR-7 | Segurança | Conteúdo do script | Sem segredos, sem `curl | sh`, apenas `npx skills add` de fontes já listadas no research §"Codebase Findings". Sem `eval` de input externo |
| NFR-8 | Output do terminal | Linhas impressas em sucesso/no-op/falha | Sucesso: 2 linhas; no-op: 0; falha: 1 linha + ponteiro pro log |
| NFR-9 | Permanência do marker | Local do marker | `${CLAUDE_PLUGIN_DATA}` (sobrevive a update do plugin) — NÃO usar `${CLAUDE_PLUGIN_ROOT}` |

## Glossary

- **`${CLAUDE_PLUGIN_ROOT}`** — caminho efêmero do plugin instalado; muda a cada update. Usar para referenciar scripts/arquivos versionados.
- **`${CLAUDE_PLUGIN_DATA}`** — caminho persistente por plugin; sobrevive a updates. Usar para markers, logs, estado de bootstrap.
- **Marker file** — arquivo vazio (`.bootstrapped-v<version>`) cuja existência sinaliza que o bootstrap dessa versão já rodou com sucesso.
- **Bootstrap** — execução única (por versão) dos `npx skills add` declarados, na primeira sessão após install/update.
- **Skill standalone** — skill 3rd-party fora de marketplaces, instalada via `npx skills add <git-source>` (ex: GSD, find-skills). Distinta de "plugin dependency", que vem via `dependencies` no `plugin.json`.
- **Plugin dependency** — outro plugin Claude Code referenciado em `dependencies` do `plugin.json`; auto-instala via mecanismo nativo (já funciona).
- **Fallback manual** — comando slash `/<pkg>-setup` preservado para re-execução / debug.

## Out of Scope

- Rollout para `design`, `programming`, `marketing` (specs separadas).
- Plugin `copy` (sem standalones até v0.2 — não recebe `hooks.json` nesta spec).
- `uipro-cli` (npm global + `uipro init --ai claude` interativo): permanece manual via `/design-setup`. Documentar como exceção conhecida no ADR-001.
- Substituir as `dependencies` cross-marketplace existentes (já funcionam — não mexer).
- Telemetria / analytics de taxa de sucesso do bootstrap.
- Suporte a Windows / PowerShell.
- Coordenação especial com servidores MCP (MCPs são independentes do `SessionStart` per docs).

## Dependencies / Assumptions

- **Node.js + `npx`** disponíveis no PATH do usuário (pré-requisito existente para usar `myskills` hoje).
- Pacote `skills` no npm continua publicado e estável (mesma fonte usada pelos `/<pkg>-setup` atuais).
- **`bash`** ≥ 3.2 disponível (default macOS). Não dependemos de bash 4-only features.
- Versão do Claude Code suportando `${CLAUDE_PLUGIN_DATA}` e `${CLAUDE_PLUGIN_ROOT}` (documentado por Anthropic, current).
- Acesso de rede (HTTPS para `npm` e SSH/HTTPS para `github.com`) na primeira sessão pós-install.
- Usuário tem chave SSH configurada para os repos `git@github.com:...` (assumption já válida hoje para `/workflow-setup`).

## Open Decisions

Nenhuma. As 6 open questions do research foram resolvidas no escopo desta spec:

1. Offline → fail-soft sem criar marker (FR-7, US-4).
2. Output → 2 linhas PT-BR + log em arquivo (FR-5, NFR-8).
3. Marker → keyed por versão do plugin (FR-3).
4. `uipro-cli` → permanece manual (Out of Scope).
5. `copy` plugin → sem `hooks.json` até v0.2 (Out of Scope).
6. MCP coordination → não necessária (Out of Scope).

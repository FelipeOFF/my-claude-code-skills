---
spec: auto-install
phase: tasks
created: 2026-05-11
totalTasks: 8
---

# Tasks: auto-install (v1 — plugin `workflow`)

Sequência atômica para `spec-executor`. Cada tarefa = 1 commit (exceto 7 e 8). Cita seções de [design.md](./design.md) e [research.md](./research.md). PT-BR no texto humano; identificadores/paths em inglês.

Branch alvo: `feat/auto_install_skills` (já existe).

---

## Task 1 — ADR-001: registrar política de auto-install

**Goal**: Criar ADR documentando a decisão (Alternativa B + D, com E seletiva) para futura replicação a outros plugins. Satisfaz FR-11, US-6, US-7.

**Files**:
- NEW: `docs/adr/ADR-001-auto-install-strategy.md`

**Steps**:
1. Criar diretório `docs/adr/` se não existir.
2. Copiar conteúdo verbatim da estrutura em [design.md §4.5](./design.md), incluindo seções: Status/Date/Spec, Context, Alternatives considered (A–E), Decision, Consequences (positivas/negativas/exceção uipro-cli), Replicação para outros plugins (3 passos), References.
3. Confirmar citação explícita a `specs/auto-install/research.md` e à tabela de alternativas.

**Acceptance criteria**:
- Arquivo existe em `docs/adr/ADR-001-auto-install-strategy.md`.
- Lista as 5 alternativas (A, B, C, D, E) com 1 linha cada.
- Decisão é "B primário + D para plugin deps + E seletivo".
- Cita `specs/auto-install/research.md`.

**Verification command**:
```bash
test -f docs/adr/ADR-001-auto-install-strategy.md \
  && grep -q "Alternative" docs/adr/ADR-001-auto-install-strategy.md \
  && grep -q "research.md" docs/adr/ADR-001-auto-install-strategy.md \
  && echo PASS
```

**Commit message**: `docs: Adiciona ADR-001 estratégia de auto-install de skills`

---

## Task 2 — Bootstrap script idempotente

**Goal**: Criar `bootstrap.sh` fail-soft que roda `npx skills add` para GSD, find-skills e 1password, com marker keyed por versão. Satisfaz FR-2..FR-8, FR-13, NFR-1, NFR-3..NFR-8.

**Files**:
- NEW: `plugins/workflow/scripts/bootstrap.sh`

**Steps**:
1. Criar diretório `plugins/workflow/scripts/`.
2. Copiar corpo do script verbatim de [design.md §4.2](./design.md) (bloco `#!/usr/bin/env bash` ... `exit 0`).
3. `chmod +x plugins/workflow/scripts/bootstrap.sh`.
4. Garantir que `set -uo pipefail` é usado (sem `-e`), referências a `${CLAUDE_PLUGIN_ROOT}` e `${CLAUDE_PLUGIN_DATA}`, e que existem exatamente 3 blocos `run_step` (GSD bundle, find-skills, 1password).

**Acceptance criteria**:
- Arquivo executável (`-x` set).
- `bash -n` passa sem erros de sintaxe.
- Contém `${CLAUDE_PLUGIN_ROOT}` e `${CLAUDE_PLUGIN_DATA}`.
- Contém 3 `run_step` calls: `GSD bundle`, `find-skills (vercel-labs)`, `1password (openclaw)`.
- Não usa `jq` nem `set -e`.

**Verification command**:
```bash
test -x plugins/workflow/scripts/bootstrap.sh \
  && bash -n plugins/workflow/scripts/bootstrap.sh \
  && grep -q 'CLAUDE_PLUGIN_ROOT' plugins/workflow/scripts/bootstrap.sh \
  && grep -q 'CLAUDE_PLUGIN_DATA' plugins/workflow/scripts/bootstrap.sh \
  && [ "$(grep -c '^run_step ' plugins/workflow/scripts/bootstrap.sh)" = "3" ] \
  && ! grep -q '^set -e' plugins/workflow/scripts/bootstrap.sh \
  && echo PASS
```

**Commit message**: `feat: Adiciona bootstrap.sh idempotente para auto-install do workflow`

---

## Task 3 — Hooks config para SessionStart

**Goal**: Registrar hook `SessionStart` (matcher `startup|resume`, timeout 120s) que executa `bootstrap.sh`. Satisfaz FR-1, NFR-2.

**Files**:
- NEW: `plugins/workflow/.claude-plugin/hooks.json`

**Steps**:
1. Criar `plugins/workflow/.claude-plugin/hooks.json` com o JSON exato de [design.md §4.1](./design.md).
2. Confirmar matcher `"startup|resume"`, `timeout: 120`, comando `${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.sh`.

**Acceptance criteria**:
- JSON válido (`jq .` parseia).
- Tem evento `SessionStart` com matcher `startup|resume`.
- Comando referencia `${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.sh`.
- `timeout` = 120.

**Verification command**:
```bash
jq -e '.hooks.SessionStart[0].matcher == "startup|resume"
       and .hooks.SessionStart[0].hooks[0].timeout == 120
       and (.hooks.SessionStart[0].hooks[0].command | contains("bootstrap.sh"))' \
  plugins/workflow/.claude-plugin/hooks.json && echo PASS
```

**Commit message**: `feat: Registra hook SessionStart para bootstrap automático do workflow`

---

## Task 4 — Anotar `/workflow-setup` como fallback manual

**Goal**: Manter comando `/workflow-setup` funcional, deixando claro no topo que virou fallback após auto-install. Satisfaz FR-9, US-5.

**Files**:
- MODIFY: `plugins/workflow/commands/setup.md`

**Steps**:
1. Abrir `plugins/workflow/commands/setup.md`.
2. Após o título `# /workflow-setup`, inserir bloco de 3 linhas (blockquote PT-BR) explicando: "Fallback manual / re-execução. Auto-install acontece no primeiro SessionStart via `scripts/bootstrap.sh`. Use este comando para forçar re-instalação ou debugar."
3. Manter os 3 blocos `npx skills add` intactos (FR-9).

**Acceptance criteria**:
- Header com aviso de fallback em PT-BR está presente no topo (antes do primeiro bloco bash).
- Blocos `npx skills add` originais preservados (não checam marker).

**Verification command**:
```bash
grep -q "Fallback manual" plugins/workflow/commands/setup.md \
  && grep -q "SessionStart" plugins/workflow/commands/setup.md \
  && [ "$(grep -c 'npx.*skills add' plugins/workflow/commands/setup.md)" -ge "3" ] \
  && echo PASS
```

**Commit message**: `docs: Marca /workflow-setup como fallback manual após auto-install`

---

## Task 5 — Atualizar README do workflow

**Goal**: Mostrar instalação em 1 comando + subseção de re-instalação. Satisfaz FR-10, US-6.

**Files**:
- MODIFY: `plugins/workflow/README.md`

**Steps**:
1. Substituir a seção `## How to install` conforme [design.md §4.4](./design.md): apenas 2 comandos (`/plugin marketplace add ...` + `/plugin install workflow@myskills`).
2. Adicionar parágrafo explicando que standalones instalam automaticamente no primeiro SessionStart e que existe marker em `${CLAUDE_PLUGIN_DATA}`.
3. Adicionar subseção `### Re-instalação / fallback` com instruções para `/workflow-setup` e `rm` do marker.
4. Atualizar título da tabela "Standalone setup": `"Standalone setup (run /workflow-setup)"` → `"Standalone setup (auto)"`.
5. Citar `docs/adr/ADR-001-auto-install-strategy.md`.

**Acceptance criteria**:
- Seção `## How to install` mostra fluxo de 1-step (sem `/workflow-setup` obrigatório).
- Subseção `Re-instalação / fallback` presente.
- README cita ADR-001.

**Verification command**:
```bash
grep -q "Re-instalação" plugins/workflow/README.md \
  && grep -q "ADR-001" plugins/workflow/README.md \
  && grep -q "automaticamente" plugins/workflow/README.md \
  && echo PASS
```

**Commit message**: `docs: Atualiza README do workflow com auto-install em 1 comando`

---

## Task 6 — Smoke test local

**Goal**: Validar sintaxe, JSON e fail-soft do bootstrap antes do PR. Satisfaz FR-12 (subset executável localmente — passos de uninstall/reinstall ficam para validação pós-merge).

**Files**:
- READ-ONLY: `plugins/workflow/scripts/bootstrap.sh`, `plugins/workflow/.claude-plugin/hooks.json`
- WRITE: `/tmp/test-bootstrap/` (sandbox temporário)
- APPEND: `specs/auto-install/.progress.md` (anotar resultados)

**Steps**:
1. Syntax check: `bash -n plugins/workflow/scripts/bootstrap.sh`.
2. JSON validity: `jq . plugins/workflow/.claude-plugin/hooks.json > /dev/null`.
3. Dry-run sandboxed:
   ```bash
   mkdir -p /tmp/test-bootstrap
   CLAUDE_PLUGIN_ROOT="$PWD/plugins/workflow" \
   CLAUDE_PLUGIN_DATA=/tmp/test-bootstrap \
     bash -x plugins/workflow/scripts/bootstrap.sh
   ```
4. Verificar comportamento esperado:
   - Exit code 0 (fail-soft).
   - Log criado em `/tmp/test-bootstrap/bootstrap.log`.
   - Se `npx skills add` falhar (rede/CLI indisponível), marker NÃO criado e mensagem `bootstrap adiado` aparece — comportamento esperado.
   - Se todos os 3 sucederem, marker `.bootstrapped-v<version>` criado.
5. Anotar resultados em `specs/auto-install/.progress.md` (seção `## Test results — Task 6`).
6. Limpar sandbox: `rm -rf /tmp/test-bootstrap`.

**Acceptance criteria**:
- `bash -n` retorna 0.
- `jq .` em `hooks.json` retorna 0.
- Dry-run não trava shell e retorna exit 0.
- Log file existe em `/tmp/test-bootstrap/bootstrap.log` após dry-run.
- Resultado documentado em `.progress.md`.

**Verification command**:
```bash
bash -n plugins/workflow/scripts/bootstrap.sh \
  && jq . plugins/workflow/.claude-plugin/hooks.json > /dev/null \
  && grep -q "Test results — Task 6" specs/auto-install/.progress.md \
  && echo PASS
```

**Commit message**: `test: Valida sintaxe e fail-soft do bootstrap.sh do workflow`

---

## Task 7 — Push e abrir PR

**Goal**: Submeter mudanças via PR no padrão Felipe (PT-BR, conventional). Branch `feat/auto_install_skills` já existe.

**Files**: nenhum (operação git/gh).

**Steps**:
1. Confirmar branch atual: `git branch --show-current` → deve retornar `feat/auto_install_skills`.
2. Push: `git push -u origin feat/auto_install_skills`.
3. Criar PR via `gh pr create`:
   - Title: `feat: Adiciona auto-install de skills standalone ao instalar plugin`
   - Body (HEREDOC, PT-BR) com 3 seções:
     - **Summary**: 2–3 linhas explicando objetivo (eliminar `/workflow-setup` manual via hook `SessionStart`), citar Alternativa B do research e ADR-001.
     - **Changes**: bullet list dos arquivos novos/modificados (ADR, bootstrap.sh, hooks.json, setup.md, README.md).
     - **Test plan**: copiar checklist de [design.md §7](./design.md) (5 cenários: fresh install, returning session, version bump, offline, manual fallback) marcando o que foi validado localmente (Task 6) e o que requer instalação real do plugin.
   - Mencionar explicitamente: "v1 cobre apenas plugin `workflow`. Plugins `design`, `programming`, `marketing` ficam para specs futuras (replicability checklist em ADR-001)."

**Acceptance criteria**:
- PR criado e URL retornada por `gh pr create`.
- Body em PT-BR com seções **Summary**, **Changes**, **Test plan**.
- Cita ADR-001 e marca v1-scope explicitamente.

**Verification command**:
```bash
gh pr view --json url,title,body \
  | jq -e '.title | startswith("feat:")' \
  && gh pr view --json body | jq -er '.body | contains("ADR-001") and contains("Test plan")' \
  && echo PASS
```

**Commit**: No commit (deliverable é a PR).

---

## Task 8 — Sumário no vault Obsidian

**Goal**: Persistir rationale e comandos de reprodução no vault pessoal para consulta futura.

**Files**:
- NEW: `~/obsidian-vault/Projetos/myskills-autoinstall-2026-05-11.md` (fora do repo)

**Steps**:
1. Confirmar que `~/obsidian-vault/Projetos/` existe (criar se faltar).
2. Escrever arquivo `myskills-autoinstall-2026-05-11.md` com 4 seções PT-BR:
   - **Rationale**: 1 parágrafo explicando por que Alternativa B foi escolhida (cita pattern Anthropic-documentado, idempotência via marker, fail-soft, replicabilidade <5min/plugin).
   - **Comandos de reprodução**: bloco bash com os comandos exatos do dry-run (Task 6) e os do fresh install path (Task 7 / design §7).
   - **PR link**: URL retornada na Task 7.
   - **Next steps**: replicar para `plugins/design` (com nota sobre `uipro-cli` permanecer manual), `plugins/programming`, `plugins/marketing` como specs separadas; cada uma <5min seguindo checklist do ADR-001.

**Acceptance criteria**:
- Arquivo existe em `~/obsidian-vault/Projetos/myskills-autoinstall-2026-05-11.md`.
- Possui as 4 seções (Rationale, Comandos, PR link, Next steps).

**Verification command**:
```bash
test -f ~/obsidian-vault/Projetos/myskills-autoinstall-2026-05-11.md \
  && grep -q "Rationale" ~/obsidian-vault/Projetos/myskills-autoinstall-2026-05-11.md \
  && grep -q "Next steps" ~/obsidian-vault/Projetos/myskills-autoinstall-2026-05-11.md \
  && echo PASS
```

**Commit**: No commit (deliverable fora do repo, vault pessoal).

---

## Notes

- **POC shortcuts**: nenhum — todos os arquivos são produção-ready.
- **Production TODOs**: replicar padrão para `design`, `programming`, `marketing` (specs futuras; checklist em ADR-001 §"Replicação para outros plugins").
- **Risk areas**: Task 6 dry-run pode falhar em `npx skills add` se rede/registry indisponível — isso valida o fail-soft (resultado aceitável). Task 7 depende de `gh` CLI autenticado. Task 8 grava fora do repo (vault pessoal Obsidian) — não afeta o PR.

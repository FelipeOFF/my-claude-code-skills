# ADR-001: Auto-install de skills standalone via SessionStart hook

- Status: Accepted
- Date: 2026-05-11
- Spec: specs/auto-install/{research,requirements,design}.md

## Context

Marketplace `myskills` distribui plugins que dependem de skills 3rd-party
externas (GSD, find-skills, 1password, ECC, Matt Pocock, FelipeOFF/*).
Hoje o usuário roda `/<pkg>-setup` manualmente após `/plugin install`.
Step esquecível → onboarding quebra.

## Alternatives considered

- **Alternative A** — `postInstall` em `plugin.json` — não existe no schema.
- **Alternative B** — `SessionStart` hook + marker em `${CLAUDE_PLUGIN_DATA}` — pattern canônico Anthropic.
- **Alternative C** — Auto-invoke via `/plugin install` — não existe mecanismo.
- **Alternative D** — Cross-marketplace `dependencies` — só funciona para plugins registrados; não cobre `npx skills add`.
- **Alternative E** — Bundle inline em `./skills/` — quebra upstream sync; viola Constituição (standalone).

Detalhes em [specs/auto-install/research.md](../../specs/auto-install/research.md), tabela §"Alternatives A–E".

## Decision

Adotar **B** (`SessionStart` hook + marker keyed por versão) como mecanismo
primário para skills standalone.

Manter **D** (cross-marketplace `dependencies`) para plugin deps já
registrados em marketplaces (sem mudança em relação ao estado atual).

Reservar **E** (vendoring inline) para casos específicos (FelipeOFF/* tiny
skills onde manter cópia local é mais barato que rebaixar via `npx`).

## Consequences

**Positivas:**
- Instalação em 1 step (`/plugin install <pkg>@myskills`).
- Idempotente por versão (marker `.bootstrapped-v<version>`).
- Sobrevive update do plugin (`${CLAUDE_PLUGIN_DATA}` persiste).
- Fail-soft em offline — bootstrap re-tenta na sessão seguinte.
- Preserva `/<pkg>-setup` como fallback manual para debug/re-execução.

**Negativas:**
- Bootstrap roda na 1ª sessão pós-install, não no momento do install.
- Requer rede disponível na 1ª sessão para suceder de primeira.
- Hook precisa ser robusto a falha parcial (1 fonte cair não pode travar startup).

**Exceção conhecida:** `uipro-cli` (npm global + `init` interativo)
permanece manual via `/design-setup`. Auto-install de CLI interativo
exigiria prompt em hook, que viola o requisito de fail-soft silencioso.

## Replicação para outros plugins (3 passos, <5min)

1. **Copiar `hooks.json`** de `plugins/workflow/.claude-plugin/hooks.json`
   verbatim para `plugins/<dst>/.claude-plugin/hooks.json` (usa
   `${CLAUDE_PLUGIN_ROOT}` relativo — zero edição).

2. **Copiar `bootstrap.sh`** de `plugins/workflow/scripts/bootstrap.sh`
   para `plugins/<dst>/scripts/bootstrap.sh`:
   - Trocar `PLUGIN_NAME="workflow"` pelo nome do plugin destino.
   - Substituir os blocos `run_step ...` pelas fontes do
     `commands/setup.md` daquele plugin.

3. **Atualizar `README.md`** do plugin destino: mover `/<pkg>-setup`
   para subseção "Re-instalação / fallback" e adicionar 1 linha
   explicando que o bootstrap roda automaticamente. Atualizar o título
   da tabela "Standalone setup" trocando "(run /<pkg>-setup)" por "(auto)".

V1 cobre `workflow`. Specs futuras: `design` (com nota sobre `uipro-cli`
permanecer manual), `programming`, `marketing`.

## References

- [specs/auto-install/research.md](../../specs/auto-install/research.md)
- [specs/auto-install/requirements.md](../../specs/auto-install/requirements.md)
- [specs/auto-install/design.md](../../specs/auto-install/design.md)
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/hooks

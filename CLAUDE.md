# CLAUDE.md — my-claude-code-skills

Repo do marketplace `myskills`. Curadoria pessoal de skills Claude Code
organizada em packages temáticos.

## Leitura obrigatória

- [`docs/CONSTITUTION.md`](docs/CONSTITUTION.md) — regras de curadoria
  (A–E), packages top-level, procedimento para adicionar skill nova.

## Quando o usuário pede "sobe essa skill aqui" ou "adiciona X ao MySkills"

Siga o **Procedimento "sobe essa skill aqui"** descrito no final da
Constituição. Resumo:

1. Identifique a origem (autoral / dependency / standalone).
2. Classifique o package (Regra A).
3. Aplique a mudança no diretório certo:
   - autoral → `plugins/<pkg>/skills/<skill>/SKILL.md`
   - dependency → `plugins/<pkg>/.claude-plugin/plugin.json`
   - standalone → `plugins/<pkg>/commands/setup.md`
4. Atualize `plugins/<pkg>/README.md`.
5. Commit atômico no padrão Felipe (conventional + corpo PT-BR).

## Estrutura

- `.claude-plugin/marketplace.json` — catálogo do marketplace.
- `plugins/<pkg>/` — packages top-level (`design`, `copy`, `marketing`,
  `programming`).
- `agents/`, `commands/`, `rules/` — workflow autoral PT-BR/Jira do
  Felipe; **não** migram para dentro de packages.
- `docs/superpowers/specs/`, `docs/superpowers/plans/` — design e
  planos versionados.
- `docs/legacy/` — versões antigas preservadas (ex: README pré-v0.1).

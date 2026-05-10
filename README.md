# MySkills

Marketplace pessoal de skills Claude Code, curado por
[Felipe Oliveira](https://github.com/FelipeOFF) e organizado em
packages temáticos instaláveis individualmente.

> **Por que packages?** Carregar 200+ skills toda sessão queima tokens
> sem motivo. Aqui você instala só o nicho do trabalho atual.

## Quick install

```bash
# Uma vez por máquina
/plugin marketplace add FelipeOFF/my-claude-code-skills

# Por contexto de trabalho — instale só o que precisa agora
/plugin install design@myskills
/plugin install copy@myskills
/plugin install marketing@myskills
/plugin install programming@myskills
```

## Packages disponíveis (v0.1)

| Package | Escopo | README |
|---|---|---|
| `design` | UI/UX, design system, taste, mockups | [plugins/design/README.md](plugins/design/README.md) |
| `copy` | Copywriting, headlines, escrita persuasiva | [plugins/copy/README.md](plugins/copy/README.md) |
| `marketing` | SEO, CRO, tráfego pago, email, social | [plugins/marketing/README.md](plugins/marketing/README.md) |
| `programming` | Backend, frontend web/mobile, testing, debugging | [plugins/programming/README.md](plugins/programming/README.md) |

## Filosofia e regras

Toda decisão de "qual skill vai em qual package" segue uma constituição
escrita: [`docs/CONSTITUTION.md`](docs/CONSTITUTION.md).

Resumo:

- **Regra A — Localização única.** Uma skill, um package.
- **Regra B — Top-level por default.** Mid-level só com >15 skills + agrupamento ≥5.
- **Regra C — Frontmatter declara origem.** `authored | dependency | standalone-setup`.
- **Regra D — README de package padronizado.**
- **Regra E — Constituição é a fonte da verdade.**

## Workflow autoral PT-BR/Jira (raiz do repo)

Os diretórios `agents/`, `commands/` e `rules/` na raiz **não** são
parte dos packages. Eles são consumidos via `~/.claude/CLAUDE.md`
global e suportam o workflow pessoal do autor (Conventional Commits +
Jira `DTP-###`, branches `<type>/<JIRA>/<slug>`, PRs em PT-BR).

- `agents/` — `commit-crafter`, `jira-linker`, `pr-writer`
- `commands/` — `/branch`, `/commit`, `/pr`, `/review`, `/wt`
- `rules/` — `branches`, `commits`, `context7`, `language`, `workflow`

## Histórico

A versão monolítica do README (catálogo de 959 linhas pré-v0.1) está
preservada em [`docs/legacy/README-2026-05-10.md`](docs/legacy/README-2026-05-10.md).

## Contribuir / curadoria

Esta é uma curadoria **pessoal**. Sugestões via issues são bem-vindas,
mas a inclusão segue critérios da Constituição. Para abrir PR
adicionando uma skill, leia primeiro
[`docs/CONSTITUTION.md`](docs/CONSTITUTION.md).

# MySkills

> 🇺🇸 [English version](README.md)

Marketplace pessoal de skills Claude Code, curado por
[Felipe Oliveira](https://github.com/FelipeOFF) e organizado em
packages temáticos instaláveis individualmente.

> **Por que packages?** Carregar 200+ skills toda sessão queima tokens
> sem motivo. Aqui você instala só o nicho do trabalho atual.

## Instalação rápida

```bash
# Uma vez por máquina
/plugin marketplace add FelipeOFF/my-claude-code-skills

# Por contexto de trabalho — instale só o que precisa agora
/plugin install design@myskills
/plugin install copy@myskills
/plugin install marketing@myskills
/plugin install programming@myskills
/plugin install workflow@myskills
```

## Requisitos

O marketplace é **self-contained**: as skills são vendorizadas (o conteúdo
real mora em cada pasta de skill), então após o `/plugin install` elas já
ficam disponíveis — sem passo de download por skill. Algumas skills chamam
runtimes locais, então para usar **tudo** você precisa de:

| Runtime | Versão | Usado por |
|---|---|---|
| **Python** | **3.12** (testado em 3.12.1; 3.10+ funciona) | MCP `code-review-graph` e os harnesses `pytest`/`hypothesis` das skills `n-plus-one-guard` e `race-condition-guard` |
| **Node.js** | 18+ | skills que rodam via `npx` (`render-plans-to-html`, `find-skills`, `ui-ux-pro-max`) e os MCP servers auto-configurados |
| **git** + **gh** | recente | clonar fontes standalone e o workflow de PR/branch do autor |

> Recomendado: gerenciar Python com `asdf`/`pyenv` e pinar `3.12.1`. O MCP
> `code-review-graph` espera um caminho de interpretador estável — ver
> [programming/README.md](plugins/programming/README.md) para o ajuste do `.mcp.json`.

## Como usar

1. **Adicione o marketplace uma vez** e **instale só o(s) package(s)** do
   trabalho atual (acima) — carregar todas as skills toda sessão queima tokens.
2. **Skills vendorizadas já vêm prontas.** As instruções completas ficam em
   `plugins/<pkg>/skills/<skill>/SKILL.md`; o Claude carrega sob demanda quando
   a tarefa casa com a `description` da skill. Não há passo de setup.
3. **Setup externo opcional.** Poucas skills não dá pra vendorizar (binário
   npm global, MCP server, bundle 3rd-party grande). Cada package expõe um
   comando `/<package>-setup` que instala só essas — é opcional e está listado
   no README do package.
4. **Deps e MCPs auto-configuram.** Plugin deps cross-marketplace e MCP servers
   declarados em cada `plugin.json` instalam/configuram sozinhos; credenciais
   pessoais ficam em env vars (nunca commitadas).

## Packages

| Package | Escopo | O que tem dentro | Detalhes |
|---|---|---|---|
| `design` | UI/UX, design system, taste, mockups | Stitch (Google Labs), Huashu, plugin frontend-design, image generation, style packs, MCP Magic da 21st.dev | [→ design/README.md](plugins/design/README.md) |
| `copy` | Copywriting, headlines, escrita persuasiva | _scaffold (sem skills curadas ainda)_ | [→ copy/README.md](plugins/copy/README.md) |
| `marketing` | SEO, CRO, tráfego pago, email, social | TopRank (SEO) | [→ marketing/README.md](plugins/marketing/README.md) |
| `programming` | Backend, frontend web/mobile, testing, debugging, infra | Skills vendorizadas (tdd, obscura, render-plans-to-html), guardrails (n-plus-one-guard, race-condition-guard), MCP code-review-graph, Stripe, Firebase, Agent SDK, Rust LSP, MCPs (chrome-devtools, react-grab, hostinger) | [→ programming/README.md](plugins/programming/README.md) |
| `workflow` | Planning, memória, multi-phase, autonomous loops, multi-agent | superpowers, claude-mem, octo, codex, ralph-specum, sleepwell, bundle GSD (64 skills), find-skills, 1password | [→ workflow/README.md](plugins/workflow/README.md) |

## Por que essas skills?

Esta é uma **curadoria pessoal ativa**, não um catálogo exaustivo.
Toda skill listada aqui foi selecionada porque o autor de fato usa em
projetos reais. As razões se agrupam em:

- **Override de defaults do LLM**: design-taste skills, frontend-patterns, code-reviewer — LLMs caem em outputs genéricos; essas skills injetam regras opinativas.
- **Memória cross-sessão**: claude-mem — projetos longos perdem contexto sem memória persistente.
- **Planejamento multi-fase**: GSD, ralph-specum, superpowers — features que duram dias precisam de estrutura (PLAN.md, REVIEW.md, milestones).
- **Integrações MCP**: chrome-devtools, hostinger, magic — ferramentas que o autor usa todo dia ficam auto-configuradas (env vars continuam pessoais).
- **Patterns de stack**: Anthropic SDK, Postgres, REST design — opiniões formadas, não boilerplate genérico.

Cada README de package explica por que **cada** skill incluída está
na curadoria.

## Filosofia e regras

Toda decisão de "qual skill vai em qual package" segue uma constituição
escrita: [`docs/CONSTITUTION.md`](docs/CONSTITUTION.md).

Resumo:

- **Regra A — Localização única.** Uma skill, um package.
- **Regra B — Top-level por default.** Mid-level só com >15 skills + agrupamento ≥5.
- **Regra C — Frontmatter declara origem.** `authored | vendored | dependency | standalone-setup`.
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

## Contribuir / curadoria

Esta é uma curadoria **pessoal**. Sugestões via issues são bem-vindas,
mas a inclusão segue critérios da Constituição. Para abrir PR
adicionando uma skill, leia primeiro
[`docs/CONSTITUTION.md`](docs/CONSTITUTION.md).

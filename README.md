# MySkills

> 🇧🇷 [Versão em Português](README.pt-BR.md)

Personal Claude Code skills marketplace, curated by
[Felipe Oliveira](https://github.com/FelipeOFF) and organized into
themed packages installable individually.

> **Why packages?** Loading 200+ skills every session burns tokens
> for no reason. Here you install only the niche relevant to your
> current work.

## Quick install

```bash
# Once per machine
/plugin marketplace add FelipeOFF/my-claude-code-skills

# Per work context — install only what you need now
/plugin install design@myskills
/plugin install copy@myskills
/plugin install marketing@myskills
/plugin install programming@myskills
/plugin install workflow@myskills
```

## Packages

| Package | Scope | What's inside | Details |
|---|---|---|---|
| `design` | UI/UX, design system, taste, mockups | Stitch (Google Labs), Huashu, frontend-design plugin, image generation, style packs, 21st.dev Magic MCP | [→ design/README.md](plugins/design/README.md) |
| `copy` | Copywriting, headlines, persuasive writing | _scaffold (no curated skills yet)_ | [→ copy/README.md](plugins/copy/README.md) |
| `marketing` | SEO, CRO, paid traffic, email, social | SEO audit (ECC), TopRank | [→ marketing/README.md](plugins/marketing/README.md) |
| `programming` | Backend, frontend web/mobile, testing, debugging, infra | ECC patterns (api-design, postgres, e2e), Stripe, Firebase, Agent SDK, Rust LSP, MCPs (chrome-devtools, react-grab, hostinger), TDD bundle | [→ programming/README.md](plugins/programming/README.md) |
| `workflow` | Planning, memory, multi-phase, autonomous loops, multi-agent | superpowers, claude-mem, agentmemory, octo, codex, ralph-specum, sleepwell, GSD bundle (64 skills), find-skills, 1password | [→ workflow/README.md](plugins/workflow/README.md) |

## Why these skills?

This is **active personal curation**, not an exhaustive catalog. Every
skill listed here was selected because the author actually uses it in
real projects. Reasons cluster into:

- **Override LLM defaults**: design-taste skills, frontend-patterns, code-reviewer — LLMs default to generic outputs; these skills inject opinionated rules.
- **Cross-session memory**: claude-mem, agentmemory — long projects lose context without persistent memory.
- **Multi-phase planning**: GSD, ralph-specum, superpowers — features that span days need structure (PLAN.md, REVIEW.md, milestones).
- **MCP integrations**: chrome-devtools, hostinger, magic — tools the author uses daily get auto-configured (env vars stay personal).
- **Stack patterns**: Anthropic SDK, Postgres, REST design — opinionated patterns, not generic boilerplate.

Each package README explains why **each** included skill is in the curation.

## Philosophy and rules

Every "which skill goes in which package" decision follows a written
constitution: [`docs/CONSTITUTION.md`](docs/CONSTITUTION.md).

Summary:

- **Rule A — Single location.** One skill, one package.
- **Rule B — Top-level by default.** Mid-level only with >15 skills + ≥5 cohesive cluster.
- **Rule C — Frontmatter declares origin.** `authored | dependency | standalone-setup`.
- **Rule D — Standardized package README.**
- **Rule E — The Constitution is the source of truth.**

## Author's PT-BR/Jira workflow (repo root)

The directories `agents/`, `commands/`, and `rules/` at the root are
**not** part of any package. They're consumed via `~/.claude/CLAUDE.md`
global and support the author's personal workflow (Conventional Commits +
Jira `DTP-###`, branches `<type>/<JIRA>/<slug>`, PRs in PT-BR).

- `agents/` — `commit-crafter`, `jira-linker`, `pr-writer`
- `commands/` — `/branch`, `/commit`, `/pr`, `/review`, `/wt`
- `rules/` — `branches`, `commits`, `context7`, `language`, `workflow`

## Contribute / curation

This is a **personal** curation. Issues with suggestions are welcome,
but inclusion follows Constitution criteria. To open a PR adding a
skill, read [`docs/CONSTITUTION.md`](docs/CONSTITUTION.md) first.

# Package: programming

Curated skills for backend, frontend (web and mobile), testing, debugging, and infra.

> **Why this package?** Stack-specific patterns + dev workflow tooling
> + MCPs the author runs daily. Each dep is a battle-tested override
> for LLM defaults: typed Anthropic SDK usage, REST design that scales,
> Playwright E2E with proper artifact handling. Generic boilerplate
> need not apply.

## Plugin dependencies (auto-installed)

| Plugin @ Marketplace | Why it's curated |
|---|---|
| `agent-sdk-dev` @ `claude-plugins-official` | Scaffolding for new Claude Agent SDK applications — boilerplate avoidance, project setup, recommended structure. |
| `stripe` @ `claude-plugins-official` | Stripe integration: best practices, error code explainer, test card numbers for various scenarios. |
| `rust-analyzer-lsp` @ `claude-plugins-official` | Rust LSP integrated into CC — go-to-definition, type hints, refactoring while editing Rust code. |
| `firebase` @ `firebase` | Firebase deploy, env management, project init, security rules, SDK config — full lifecycle for Firebase apps. |

## MCP servers (auto-configured)

| MCP | Command | Required env | Why it's curated |
|---|---|---|---|
| `chrome-devtools` | `npx chrome-devtools-mcp@latest` | none | Live Chrome DevTools control: inspect DOM, debug runtime, profile performance directly from CC. |
| `react-grab-mcp` | `npx -y @react-grab/mcp --stdio` | none | Extracts React component context (props, state, source location) from a running app — bridges DOM inspection and component code. |
| `hostinger-mcp` | `npx hostinger-api-mcp@latest` | `HOSTINGER_API_TOKEN` | Manages Hostinger VPS, DNS, domains, hosting, billing via API — the author's host of choice. |

> Personal credentials live in your env vars — never committed here.

## Standalone setup (run `/programming-setup`)

Skills installed individually via `npx skills add --skill <name>` —
pulls just the skill, not the parent bundle.

| Skill | Source | Why it's curated |
|---|---|---|
| `backend-patterns` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/backend-patterns) | API architecture for Node.js/Express/Next.js — service layers, error handling, validation, async patterns. |
| `frontend-patterns` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/frontend-patterns) | React/Next idioms: state management, hooks, performance (memoization, code splitting), client/server boundary. |
| `api-design` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/api-design) | REST design at production scale: resource naming, status codes, pagination, filtering, error responses, versioning, rate limiting. |
| `postgres-patterns` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/postgres-patterns) | PostgreSQL query optimization, schema design, indexing strategy, security (RLS, roles) — based on Supabase best practices. |
| `e2e-testing` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/e2e-testing) | Playwright E2E: Page Object Model, CI/CD integration, artifact management (screenshots/videos/traces), flaky test strategies. |
| `claude-api` | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/claude-api) | **Oficial da Anthropic.** Padrões do Claude API: Messages API, streaming, tool use, vision, extended thinking, batches, prompt caching, Agent SDK. |
| `tdd`, `to-prd` | [mattpocock/skills](https://github.com/mattpocock/skills) | `tdd` runs strict red-green-refactor; `to-prd` turns chat context into a GitHub issue PRD — both reduce friction in feature lifecycle. |
| `obscura` | [FelipeOFF/obscura-skill](https://github.com/FelipeOFF/obscura-skill) | Scraping/E2E with a Rust-based headless browser (~30 MB) compatible with Puppeteer/Playwright over CDP — light footprint, stealth on. |
| `render-plans-to-html` | [FelipeOFF/render-plans-to-html](https://github.com/FelipeOFF/render-plans-to-html) | Renders planning Markdown (PLAN.md, REVIEW.md, etc.) as a self-contained HTML dashboard with sidebar nav, mermaid diagrams, syntax highlighting — for sharing artifacts with non-engineers. |

## Local-only skills (no public source mapped)

Author's bundle, not publicly distributable. Each fills a specific gap:

- `backend-code-review` — checklist-driven review for backend files (`.py`, `api/` paths).
- `frontend-code-review` — checklist for frontend files (`.tsx`, `.ts`, `.js`).
- `code-reviewer` — general security/performance/best-practices review (cross-stack).
- `debugger` — systematic root-cause analysis with stack-trace dissection.
- `defuddle` — cleans markdown from web pages (saves tokens vs raw WebFetch HTML).
- `frontend-testing` — Vitest + React Testing Library generation patterns.
- `fuzzing-dictionary` — domain-specific tokens for guiding fuzzers (AFL++, OSS-Fuzz).
- `fuzzing-obstacles` — patches around checksums/magic-numbers/anti-debug to unblock fuzz coverage.
- `property-based-testing` — PBT cross-language (Hypothesis, fast-check, proptest, QuickCheck).
- `context7-mcp` — heuristics for when to call the Context7 MCP (vs trusting training data).

## How to install

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install programming@myskills
/programming-setup   # optional — installs 3rd-party standalone bundles
```

## How to remove

```bash
/plugin uninstall programming@myskills
```

> When this package crosses >15 skills with a natural ≥5 cluster,
> Constitution Rule B promotes to mid-level (e.g., `programming-frontend-mobile@myskills`).

---

## 🇧🇷 Resumo em PT-BR

Package `programming` = tooling + MCPs do dia-a-dia (4 deps
cross-marketplace): Stripe, Firebase, Rust LSP e scaffolding de
Agent SDK. Sem dependência do bundle `everything-claude-code`.

Os 6 stack patterns (backend-patterns, frontend-patterns, api-design,
postgres-patterns, e2e-testing, claude-api) são instalados via
`/programming-setup` direto do source (`affaan-m/everything-claude-code`
e `anthropics/skills`), usando `npx skills add --skill <name>` — pega
só a skill específica sem trazer o bundle inteiro.

3 MCPs auto-configurados: `chrome-devtools` (DevTools ao vivo),
`react-grab-mcp` (extrai contexto de componente React do DOM rodando),
e `hostinger-mcp` (gerencia VPS/DNS — precisa de `HOSTINGER_API_TOKEN`
pessoal). Credenciais ficam em env vars.

Via `/programming-setup`: bundle Matt Pocock (`tdd` + `to-prd`),
`obscura` (scraping com browser Rust) e `render-plans-to-html`
(renderiza PLAN.md/REVIEW.md como dashboard HTML).

Local-only (sem fonte pública): code-reviewers (backend/frontend/geral),
debugger sistemático, fuzzing toolchain (PBT, dictionaries, obstacles),
e helpers de testing/parsing (frontend-testing, defuddle, context7-mcp).

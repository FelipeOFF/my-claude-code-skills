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

## Vendored skills (real content in the repo)

These skills ship their full instructions inside their folder — available
immediately after `/plugin install programming@myskills`, no setup step.

| Skill | Source | Why it's curated |
|---|---|---|
| `tdd` | [mattpocock/skills](https://github.com/mattpocock/skills) (`vendored`) | Strict red-green-refactor loop with behavior-over-implementation testing; ships its `mocking`/`refactoring`/`interface-design` references. |
| `obscura` | [FelipeOFF/obscura-skill](https://github.com/FelipeOFF/obscura-skill) (`vendored`) | Scraping/E2E with a Rust-based headless browser (~30 MB) compatible with Puppeteer/Playwright over CDP — light footprint, stealth on. |
| `render-plans-to-html` | [FelipeOFF/render-plans-to-html](https://github.com/FelipeOFF/render-plans-to-html) (`vendored`) | Renders planning Markdown (PLAN.md, REVIEW.md, etc.) as a self-contained HTML dashboard with sidebar nav, mermaid, syntax highlighting — runs via `npx`. |
| `n-plus-one-guard` | [FelipeOFF/n-plus-one-guard-skill](https://github.com/FelipeOFF/n-plus-one-guard-skill) (`authored`) | Detects/prevents **N+1 SQL queries** and redundant per-item HTTP calls in one request: query-count interceptor, per-endpoint budget asserts, allowlist, eager/prefetch/DataLoader/batch cures. |
| `race-condition-guard` | [FelipeOFF/race-condition-guard-skill](https://github.com/FelipeOFF/race-condition-guard-skill) (`authored`) | Validates/prevents **race conditions** in concurrent handlers (TOCTOU, lost update, double-submit): atomic updates, locks, constraints, idempotency keys + concurrency & property-based tests that prove the invariant. |
| `code-review-graph` | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) (`pip` MCP) | Semantic codebase knowledge graph via MCP — architecture map + blast-radius impact analysis with ~8× fewer tokens. Needs Python (see below). |

## Stack pattern skills (authored)

Opinionated stack patterns, content in the repo (`source: authored`) — ready
on install, no setup step.

| Skill | Scope |
|---|---|
| `api-design` | REST design at production scale: resource naming, status codes, pagination, filtering, error responses, versioning, rate limiting. |
| `backend-patterns` | Backend architecture for Node.js/Express/Next.js API routes — service layers, error handling, validation, async patterns. |
| `frontend-patterns` | React/Next idioms: state management, hooks, performance (memoization, code splitting), client/server boundary. |
| `postgres-patterns` | PostgreSQL query optimization, schema design, indexing strategy, security (RLS, roles). |
| `e2e-testing` | Playwright E2E: Page Object Model, config, CI/CD integration, artifact handling (screenshots/videos/traces), flaky-test strategies. |

## Optional external setup (run `/programming-setup`)

Only skills that can't be vendored (external bundle):

| Skill | Source | Why it's curated |
|---|---|---|
| `claude-api` | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/claude-api) | **Anthropic official.** Claude API patterns: Messages API, streaming, tool use, vision, extended thinking, batches, prompt caching, Agent SDK. |

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
/programming-setup   # optional — installs only the external `claude-api` skill
```

> **Python required** for the `code-review-graph` MCP and for the
> `pytest`/`hypothesis` harnesses shipped by `n-plus-one-guard` and
> `race-condition-guard` — Python **3.12** (tested on 3.12.1; 3.10+ works).
> The MCP's generated `.mcp.json` uses `uvx`, which breaks under asdf —
> replace `command` with your stable interpreter path:
>
> ```json
> { "mcpServers": { "code-review-graph": {
>   "command": "<asdf>/installs/python/3.12.1/bin/code-review-graph",
>   "args": ["serve"], "cwd": "/path/to/project", "type": "stdio" } } }
> ```

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
Agent SDK.

Skills **vendorizadas** (conteúdo real no repo, prontas no install):
`tdd` (red-green-refactor da Matt Pocock), `obscura` (scraping com
browser Rust), `render-plans-to-html` (renderiza PLAN.md/REVIEW.md como
dashboard HTML), e as duas autorais de guardrail — `n-plus-one-guard`
(trava N+1 de queries/chamadas por request com teto por endpoint) e
`race-condition-guard` (valida/previne race conditions com locks,
idempotência e testes de concorrência). O `code-review-graph` é um MCP
em Python (grafo semântico + blast-radius).

Skills de **stack pattern** (autorais, conteúdo no repo): `api-design`,
`backend-patterns`, `frontend-patterns`, `postgres-patterns` e
`e2e-testing` — padrões opinativos de REST, backend Node, React/Next,
PostgreSQL e Playwright E2E, prontos no install.

**Python** é necessário para o MCP `code-review-graph` e para os
harnesses `pytest`/`hypothesis` das skills de guardrail — Python 3.12
(testado em 3.12.1; 3.10+ funciona).

Via `/programming-setup` (opcional) entra só o `claude-api` da Anthropic
(`anthropics/skills`), que não dá pra vendorizar.

3 MCPs auto-configurados: `chrome-devtools` (DevTools ao vivo),
`react-grab-mcp` (extrai contexto de componente React do DOM rodando),
e `hostinger-mcp` (gerencia VPS/DNS — precisa de `HOSTINGER_API_TOKEN`
pessoal). Credenciais ficam em env vars.

Local-only (sem fonte pública): code-reviewers (backend/frontend/geral),
debugger sistemático, fuzzing toolchain (PBT, dictionaries, obstacles),
e helpers de testing/parsing (frontend-testing, defuddle, context7-mcp).

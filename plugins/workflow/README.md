# Package: workflow

Meta-workflow: phase planning, persistent memory, autonomous loops,
multi-session debugging, multi-agent orchestration.

> **Why this package?** Long projects break without structure. These
> tools encode the structure: how to plan a feature in phases, how
> to keep context across sessions (so day 3 doesn't rebuild day 1),
> how to delegate to other agents safely, how to run an autonomous
> loop overnight without losing your branch.

## Plugin dependencies (auto-installed)

| Plugin @ Marketplace | Why it's curated |
|---|---|
| `superpowers` @ `superpowers-marketplace` | Brainstorming, writing-plans, executing-plans, systematic-debugging, TDD — the workflow spine for non-trivial features. |
| `claude-mem` @ `thedotmack` | Persistent cross-session memory: smart-explore, knowledge-agent, timeline reports — survives compaction and new sessions. |
| `octo` @ `nyldn-plugins` | Claude Octopus orchestration: personas, multi-provider routing, parallel multi-agent flows for big tasks. |
| `codex` @ `openai-codex` | Runtime contract for delegating investigation/fixes to the Codex CLI when a second model perspective is needed. |
| `ralph-specum` @ `smart-ralph` | Spec workflow (research → requirements → design → tasks → implement) — pipeline for features with high ambiguity. |
| `sleepwell` @ `sleepwell` | Autonomous overnight loop with discipline (isolated branch, atomic commit per iter, automatic rollback) + voice matching + meta-learning. |

## MCP servers (auto-configured)

_None directly. The plugin deps above each declare their own MCPs
when needed (e.g., `claude-mem` brings `mcp-search`)._

## Vendored skills (real content in the repo)

Available immediately after `/plugin install workflow@myskills` — no setup step.

| Skill | Source | Why it's curated |
|---|---|---|
| `diagnose`, `grill-me`, `grill-with-docs`, `handoff`, `improve-codebase-architecture`, `prototype`, `to-issues`, `to-prd`, `triage`, `write-a-skill`, `zoom-out` | [mattpocock/skills](https://github.com/mattpocock/skills) (`vendored`) | Lean workflow toolkit: diagnose/grill loops, ADR + handoff docs, architecture deepening, throwaway prototyping, issue/PRD generation, triage, skill authoring, and zoom-out for higher-level maps. |
| `find-skills` | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) (`vendored`) | Discovery and install of new skills via `npx skills find/add` — meta-tool for extending the toolkit on demand. |
| `llm-wiki` | authored | Karpathy-style LLM wiki pattern — structured, navigable knowledge capture for a codebase/domain. |

## Standalone setup (auto)

Installed on first session via `SessionStart` bootstrap (or `/workflow-setup`):

| Skill / Bundle | Source | Why it's curated |
|---|---|---|
| GSD — Get Shit Done | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | 64-skill `gsd-*` family covering project lifecycle: roadmap, phase planning, execution, verification, milestones, workstreams, debug, code-review, docs-update. The author's primary planning system. |
| `1password` | [openclaw/openclaw](https://github.com/openclaw/openclaw/tree/main/skills/1password) | 1Password CLI (`op`) usage: install, signin, read/inject/run secrets — secrets management without leaking to logs. |

## How to install

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install workflow@myskills
```

Standalones (GSD, 1password) são instaladas automaticamente
na primeira sessão pós-install via hook `SessionStart` + `scripts/bootstrap.sh`.
Marker em `${CLAUDE_PLUGIN_DATA}/.bootstrapped-v<version>` garante idempotência.
(`find-skills` agora é vendorizada — já vem no repo.)

### Re-instalação / fallback

Se o bootstrap automático falhar (offline na 1ª sessão, fonte temporariamente
fora do ar, etc.), rode manualmente:

```bash
/workflow-setup
```

Para forçar re-bootstrap em sessão futura (ex: depois de limpar `~/.skills/`),
delete o marker:

```bash
rm "${CLAUDE_PLUGIN_DATA}/.bootstrapped-v"*
```

Decisão de arquitetura: ver [`docs/adr/ADR-001-auto-install-strategy.md`](../../docs/adr/ADR-001-auto-install-strategy.md).

## How to remove

```bash
/plugin uninstall workflow@myskills
```

> Cross-marketplace dependencies are **not** auto-removed —
> they may be in use by other installed packages.

---

## 🇧🇷 Resumo em PT-BR

Package `workflow` = estrutura para projetos longos. As deps
cross-marketplace cobrem: `superpowers` (brainstorming, writing-plans,
TDD, debugging), `claude-mem` (memória cross-session que sobrevive a
compactação), `octo` (orchestration multi-persona/multi-provider),
`codex` (delegação ao Codex CLI), `ralph-specum` (research →
requirements → design → tasks → implement) e `sleepwell` (loop autônomo
overnight com rollback automático e meta-learning).

**Vendorizadas** (conteúdo real no repo): o bundle de workflow da Matt
Pocock (`diagnose`, `grill-me`, `grill-with-docs`, `handoff`,
`improve-codebase-architecture`, `prototype`, `to-issues`, `to-prd`,
`triage`, `write-a-skill`, `zoom-out`), o `find-skills` (descoberta de
skills via `npx skills`) e a autoral `llm-wiki`.

Via `/workflow-setup`: o bundle GSD da glittercowboy traz 64 skills
`gsd-*` que formam o sistema principal de planejamento do autor
(roadmap, fases, execução, verificação, milestones, workstreams) e
`1password` (gerenciamento de secrets via CLI `op`, sem vazar pra logs).

Conjunto desenhado pra sustentar features que duram dias/semanas sem
perder contexto entre sessões.

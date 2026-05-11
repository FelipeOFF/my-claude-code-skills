---
spec: auto-install
phase: research
created: 2026-05-11
---

# Research: auto-install

## Executive Summary

Claude Code has **no native `postInstall`/`onInstall` hook** in `plugin.json`. The canonical pattern (documented by Anthropic) is a `SessionStart` hook that idempotently bootstraps state into `${CLAUDE_PLUGIN_DATA}` (persists across plugin updates) using `${CLAUDE_PLUGIN_ROOT}` as the source-of-truth. **Recommendation: Alternative B (SessionStart hook + marker file)**, executing `npx skills add ...` once per plugin version. Cross-marketplace `dependencies` (D) is already in use for sibling plugins but does **not** cover bare `npx skills` sources (GSD, find-skills, 1password, ECC bits, Matt Pocock, FelipeOFF/* repos).

## Spec Investigation (6 questions)

| # | Question | Answer | Source |
|---|---|---|---|
| 1 | `postInstall` in `plugin.json`? | **No.** Complete manifest schema lists: `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `skills`, `commands`, `agents`, `hooks`, `mcpServers`, `outputStyles`, `lspServers`, `experimental`, `dependencies`. No `postInstall`/`onInstall`/`scripts`. | code.claude.com/docs/en/plugins-reference §Complete Plugin Manifest Schema |
| 2 | `onFirstActivation`/`onInstall` hook events? | **No.** Only standard hook events: `SessionStart` (with matchers `startup`/`resume`), `PostToolUse`, `UserPromptSubmit`, etc. No install-time event. | code.claude.com/docs/en/hooks |
| 3 | `/plugin install` auto-run command? | **No native auto-run.** CLI `claude plugin install <plugin>` only installs the plugin (and dependencies). | code.claude.com/docs/en/plugins-reference §plugin install |
| 4 | `allowCrossMarketplaceDependenciesOn` + `dependencies`? | **Yes, works.** `dependencies` field takes strings or `{ "name", "marketplace", "version" }`. Marketplace must be listed in `allowCrossMarketplaceDependenciesOn`. `claude plugin prune` (v2.1.121+) removes orphans. Already in use in `plugins/workflow/.claude-plugin/plugin.json` and `plugins/programming/.claude-plugin/plugin.json`. | code.claude.com/docs/en/plugin-dependencies |
| 5 | `bundledSkills` field? | **No.** Skills are auto-loaded from `./skills/` (default) or custom `skills` path in `plugin.json`. To "bundle" you copy files into that directory. | code.claude.com/docs/en/plugins-reference |
| 6 | Hook to detect first session post-install? | **Yes — `SessionStart` + marker file in `${CLAUDE_PLUGIN_DATA}`.** Anthropic's documented canonical pattern: hook runs every session start; bootstrap is gated by `diff`/marker check, so heavy work runs once per plugin version. `${CLAUDE_PLUGIN_DATA}` survives plugin updates; `${CLAUDE_PLUGIN_ROOT}` changes on each update. | code.claude.com/docs/en/plugins-reference §Manage plugin dependencies with CLAUDE_PLUGIN_DATA |

## Codebase Findings

### Setup commands (uniform pattern across plugins)

All 5 plugins follow the same shape: `plugins/<pkg>/commands/setup.md` is a slash-command markdown listing `npx skills add <git-source> [--skill <name>] -y` blocks for each standalone. Manual today: user runs `/<pkg>-setup` after install.

| Plugin | Standalones in `/setup` | Source |
|---|---|---|
| `workflow` | GSD bundle (64 skills), `find-skills`, `1password` | `git@github.com:glittercowboy/get-shit-done.git`, `github:vercel-labs/skills`, `github:openclaw/openclaw` |
| `programming` | ECC subset (5 skills), `claude-api`, Matt Pocock bundle, `obscura`, `render-plans-to-html` | `github:affaan-m/everything-claude-code`, `github:anthropics/skills`, `git@github.com:mattpocock/skills.git`, `git@github.com:FelipeOFF/*` |
| `design` | `frontend-project-style`, `design-advisor`, Stitch bundle, `huashu-design`, Matt Pocock bundle, `uipro-cli` (npm global) | mostly `git@github.com:FelipeOFF/*` + google-labs + alchaincyf + mattpocock |
| `marketing` | ECC `seo` only | `github:affaan-m/everything-claude-code --skill seo` |
| `copy` | none (v0.1 placeholder) | — |

### Cross-marketplace deps (already working)

`workflow` declares 7 plugin deps (`superpowers`, `claude-mem`, `agentmemory`, `octo`, `codex`, `ralph-specum`, `sleepwell`); `programming` declares 4 (`agent-sdk-dev`, `stripe`, `rust-analyzer-lsp`, `firebase`); `design` declares 1 (`frontend-design`); `marketing` declares 1 (`toprank`). All 10 source marketplaces are whitelisted in root `marketplace.json`. **These auto-install today — only the `npx skills add ...` block is manual.**

### 3rd-party attribution risk (for Alternative E)

`find-skills` (Vercel Labs), `1password` (OpenClaw), `claude-api` (Anthropic), Stitch (Google Labs), `huashu-design` (alchaincyf), Matt Pocock, ECC (affaan-m), GSD (glittercowboy) — each has its own LICENSE. Bundling inline requires preserving LICENSE + NOTICE per source and breaks upstream sync.

## Alternatives A–E

| # | Alternative | Feasibility | Pros | Cons |
|---|---|---|---|---|
| A | `postInstall` field in `plugin.json` | **Doesn't exist** | Would be cleanest if it existed | Not in schema; would be a feature request to Anthropic |
| B | `SessionStart` hook + marker in `${CLAUDE_PLUGIN_DATA}` | **Works today** (canonical pattern, Anthropic-documented) | Silent first-session bootstrap; idempotent (re-runs on plugin version bump); survives plugin update via `CLAUDE_PLUGIN_DATA`; no manual step ever; uses existing `npx skills add ...` commands | Runs slightly later than install (first session, not install moment); needs network on first session; user sees `npx` output unless redirected; hook must be tolerant to offline/failure |
| C | Auto-invoke command via `/plugin install` | **Doesn't exist** | — | No native mechanism |
| D | Cross-marketplace `dependencies` only | **Works for plugin-shaped deps only** | Already in use, fully automatic, `claude plugin prune` handles cleanup | Does **not** cover bare `git@github.com:...` or `npx skills` sources unless the upstream packages them as Claude Code plugins with their own marketplace. GSD/find-skills/1password/ECC/Matt Pocock/FelipeOFF repos are **skills**, not plugins on registered marketplaces — would require either upstream packaging or Felipe forking each into a tiny per-skill plugin |
| E | Bundle inline (copy into `./skills/`) | **Works today** | Zero install friction, fully offline, fully deterministic; no `npx` runtime; works air-gapped | Breaks upstream sync (manual re-vendoring on updates); LICENSE/attribution overhead per source; repo bloat (GSD alone = 64 skills); violates Constituição "standalone" classification |

## Recommendation

**Adopt Alternative B (SessionStart hook + `CLAUDE_PLUGIN_DATA` marker) as the primary mechanism.** Keep D for everything that already qualifies as a Claude Code plugin on a whitelisted marketplace (no change — it works). Use E selectively only for tiny FelipeOFF-authored skills where vendoring is cheaper than maintaining an external repo.

Concrete pattern per plugin (`plugins/<pkg>/.claude-plugin/hooks.json`):

```json
{
  "SessionStart": [
    {
      "matcher": "startup|resume",
      "hooks": [
        { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.sh", "timeout": 120 }
      ]
    }
  ]
}
```

`scripts/bootstrap.sh` template:

```bash
#!/usr/bin/env bash
set -euo pipefail
MARKER="${CLAUDE_PLUGIN_DATA}/.bootstrapped-v${PLUGIN_VERSION:-unknown}"
[ -f "$MARKER" ] && exit 0
mkdir -p "${CLAUDE_PLUGIN_DATA}"
# idempotent npx skills add ... blocks here (suppress noise; fail soft)
npx -y skills add git@github.com:glittercowboy/get-shit-done.git -y || true
# ...
touch "$MARKER"
```

Keep `/<pkg>-setup` as a manual fallback for re-runs / debugging.

Why B over D-only: GSD (64 skills), find-skills, 1password, ECC subset, Matt Pocock, FelipeOFF/* repos are **not plugins on registered marketplaces** — they're skill bundles distributed via `npx skills add`. D cannot reach them without Felipe forking each into a per-skill micro-plugin (high maintenance burden).

Why B over E: vendoring 64 GSD skills + LICENSE management for 8 upstreams violates Constituição's standalone classification and creates manual sync debt on every upstream release.

## Open Questions

1. **Network/offline behavior**: should the hook silently skip on offline first session, or hard-fail with a clear message? (Anthropic's example uses `|| rm -f` to invalidate marker on failure.)
2. **Output visibility**: do we redirect `npx skills add` output to a log under `${CLAUDE_PLUGIN_DATA}/bootstrap.log`, or let the user see it? Felipe prefers concise terminal output per global rules.
3. **Version bump semantics**: marker keyed on plugin version (`.bootstrapped-v0.1.0`) vs hash of `bootstrap.sh`? Plugin version is simpler and aligns with `claude plugin prune` semantics.
4. **`uipro-cli`** in `design-setup` uses `npm install -g` + `uipro init --ai claude` — should this stay manual (touches global npm + interactive init) or become opt-in via env var?
5. **`copy` plugin** has no standalones today — do we still ship `bootstrap.sh` (no-op) for consistency, or omit `hooks.json` entirely until v0.2?
6. **`claude-mem`** brings an `mcp-search` MCP server — does B need to coordinate with MCP startup, or are MCPs independent of `SessionStart`? (Docs imply independent.)

## Sources

- https://code.claude.com/docs/en/plugins-reference (Complete Plugin Manifest Schema; CLAUDE_PLUGIN_DATA pattern; `claude plugin install`; `claude plugin prune` v2.1.121+)
- https://code.claude.com/docs/en/plugin-dependencies (Cross-marketplace deps; version constraints; prune)
- https://code.claude.com/docs/en/hooks (`${CLAUDE_PLUGIN_ROOT}`; SessionStart matchers)
- https://code.claude.com/docs/en/plugin-marketplaces (Advanced plugin entry; `allowCrossMarketplaceDependenciesOn` semantics)
- https://code.claude.com/docs/en/claude-code-on-the-web (SessionStart hook bash script example)
- /Users/felipeoliveira/Projects/my-claude-code-skills/plugins/workflow/{commands/setup.md,.claude-plugin/plugin.json,README.md}
- /Users/felipeoliveira/Projects/my-claude-code-skills/plugins/{programming,design,marketing,copy}/{.claude-plugin/plugin.json,commands/setup.md}
- /Users/felipeoliveira/Projects/my-claude-code-skills/.claude-plugin/marketplace.json

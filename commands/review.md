---
description: Run local verification (lint + type-check + tests) before commit/PR
---

You are running the local verification cycle for the current project, following `~/.claude/rules/workflow.md`.

## Steps

1. Detect project type by reading files at the root:
   - `package.json` → Node/JS/TS
   - `pyproject.toml` / `requirements.txt` → Python
   - `Cargo.toml` → Rust
   - `go.mod` → Go
   - `pom.xml` / `build.gradle` → Java/Kotlin

2. For each type, identify the relevant commands:
   - **Node**: read `package.json scripts` and run (if they exist, in order) `lint`, `typecheck`/`type-check`/`tsc`, `test`
   - **Python**: `ruff check`, `mypy`, `pytest`
   - **Rust**: `cargo clippy`, `cargo test`
   - **Go**: `go vet`, `go test ./...`

3. Run the commands **sequentially**, stopping at the first failure. Show summarized output.

4. If any fails:
   - Report the failure to the user
   - Suggest a fix if trivial
   - Invoke systematic debugging if complex
   - **Do not** try to "force" passing by skipping steps

5. If all pass, green-light for commit/PR.

## Important

- Run `pnpm`/`npm`/`yarn`/`bun` depending on the project lockfile (`pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, `bun.lockb`)
- Never auto-run `--fix` on lint without confirmation
- Respect Claude Code hooks (PreTool guards) — if they block, investigate

$ARGUMENTS

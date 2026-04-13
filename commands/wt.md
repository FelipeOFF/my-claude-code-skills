---
description: Create a git worktree for isolated parallel work
---

You are creating a new git worktree following `~/.claude/rules/workflow.md`.

## Steps

1. Confirm the current directory is a git repo (`git rev-parse --show-toplevel`).

2. Parse `$ARGUMENTS` to extract:
   - Branch name (required, must follow `rules/branches.md`: `<type>/<JIRA>/<slug>`)
   - Base (optional, default: `main` or `master`)

3. If the branch name doesn't match the pattern, ask before proceeding.

4. Build destination path: `../<repo>-wt/<sanitized-branch>` where:
   - `<repo>` = basename of the toplevel
   - `<sanitized-branch>` = branch with `/` replaced by `_`

5. Check if the path already exists — if so, abort and warn.

6. Create the worktree:
   ```bash
   git worktree add <path> -b <branch> <base>
   ```

7. If the new worktree has `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`, ask if the user wants to install deps:
   - Node: detect package manager (`pnpm`/`npm`/`yarn`/`bun`) via lockfile
   - Python: `uv sync` if there is `uv.lock`, else `pip install -e .`
   - Rust: `cargo fetch`
   - Go: `go mod download`

8. Show the user:
   - Worktree path
   - How to enter: `cd <path>`
   - How to remove when done: `git worktree remove <path>`

## When to use worktrees

- Running multiple plan phases in parallel
- Reviewing someone else's PR without losing current context
- Testing urgent hotfixes during long feature work
- Running slow tests in an isolated background

$ARGUMENTS

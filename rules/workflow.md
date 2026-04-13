# Rule: Development workflow

## Git

- **One commit = one logical unit.** Don't pile unrelated changes
- Always create new commits — don't amend unless explicitly asked
- Never `--force-push` on `main`/`master`. On personal branches, only after confirming
- Never `reset --hard` without saving state first (`git stash` or backup branch)
- Investigate unknown files/branches before deleting — may be work-in-progress

## Worktrees (parallel work)

Git projects should use **git worktrees** for parallel work when:
- Running multiple phases of a plan in parallel
- Reviewing a PR while keeping local work intact
- Testing a hotfix without losing context of the current feature

Directory pattern: `../<repo>-wt/<branch>`. Use the `/wt` command.

## Checkpointing / Rewind

Claude Code does automatic checkpointing in git projects. To revert:
- `Esc Esc` — reverts the last edit of the turn
- `/rewind` — goes back to a previous checkpoint with a summary

Non-git projects don't get checkpointing. Consider initializing git
even in personal projects to gain that safety net.

## Verification before "done"

Before declaring a task complete:
1. Run the project linter
2. Run type-checking
3. Run relevant tests (ideally the full suite)
4. If UI change: test manually in the browser
5. Only then open a PR or say "done"

See the `verification-before-completion` pattern.

## PR

- PR title = main commit title
- Body with **Summary**, **Changes**, **Test plan** sections
- Never open a PR with broken tests unless explicitly marked WIP
- Use `gh pr create` via Bash, body via HEREDOC

## Hooks and validations

- Never skip pre-commit hooks (`--no-verify`). If they fail, investigate and fix the root cause
- Treat Claude Code hooks as authoritative

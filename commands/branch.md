---
description: Create a branch following the <type>/<JIRA>/<slug> pattern
---

You are creating a new branch following **strictly** `~/.claude/rules/branches.md`.

## Steps

1. Run `git status` and `git branch --show-current` to confirm a clean state and base branch.

2. If there are uncommitted changes, warn the user and offer:
   - Stash before switching
   - Commit before switching
   - Cancel

3. If the user passed arguments in `$ARGUMENTS`, try to parse:
   - Free form: `feat PROJ-123 change content` → `feat/PROJ-123/change_content`
   - Ready form: `feat/PROJ-123/change_content` → use directly

4. If arguments are missing or ambiguous, ask:
   - **Type**: feat / fix / hotfix / chore / docs / refactor / test / perf
   - **Jira**: code (e.g., `PROJ-123`) or "no ticket"
   - **Short description**: 2-5 words in English

5. Build the slug:
   - Convert description to snake_case ASCII lowercase
   - Strip accents and special chars
   - Ask for English translation if it comes in another language

6. Validate final format against `^(feat|fix|hotfix|chore|docs|refactor|test|perf)\/([A-Z]+-\d+\/)?[a-z0-9_]+$`.

7. Show final name and confirm before executing.

8. Execute `git checkout -b <name>`.

## Accepted examples

- `feat/PROJ-123/change_content`
- `fix/PROJ-410/fix_login_timeout`
- `chore/update_deps` (no Jira)
- `hotfix/PROJ-999/revert_release`

$ARGUMENTS

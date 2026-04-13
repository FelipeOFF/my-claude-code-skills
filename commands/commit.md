---
description: Generate a commit following Conventional Commits + Jira rules
---

You are creating a git commit following **strictly** `~/.claude/rules/commits.md` and `~/.claude/rules/branches.md`.

## Steps

1. Run in parallel:
   - `git status` (without `-uall`)
   - `git diff --staged`
   - `git diff` (unstaged — decide if anything is missing from staging)
   - `git branch --show-current` to detect current branch name
   - `git log --oneline -10` for style context

2. **Extract Jira from branch**: if the branch matches `<type>/<JIRA>/<slug>`, capture the Jira (e.g., `PROJ-123`). If there is no Jira, proceed without parentheses.

3. **Decide commit type**: default to the branch type, but if the diff suggests otherwise (e.g., branch `feat/...` but diff only fixes a typo → `fix`), adjust and warn the user.

4. Analyze the diff and draft the message in this format:
   ```
   <type>(<JIRA>): <imperative title>

   <body explaining the why and impact, 1-3 paragraphs>
   ```

5. **Show the message to the user before committing.** Ask for confirmation or adjustments.

6. If nothing is staged, list modified files and ask which to add (never use `git add -A` / `.` automatically).

7. After approval, commit with HEREDOC:
   ```bash
   git commit -m "$(cat <<'EOF'
   <formatted message>
   EOF
   )"
   ```

8. Run `git status` afterwards to confirm success.

## Constraints

- **Never** `--no-verify`
- **Never** amend a pushed commit
- If a pre-commit hook fails: fix the root cause and create a NEW commit (not amend)
- Do not include `Co-Authored-By` unless explicitly requested
- Do not commit `.env`, `*.key`, credentials

$ARGUMENTS

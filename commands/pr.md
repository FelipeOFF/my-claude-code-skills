---
description: Open a PR via gh with a structured body
---

You are creating a pull request following `~/.claude/rules/workflow.md`.

## Steps

1. Run in parallel:
   - `git status`
   - `git branch --show-current`
   - `git log <base>..HEAD --oneline` (detect base: `main`, `master` or `develop`)
   - `git diff <base>...HEAD` to understand full changes
   - Check if branch is pushed: `git rev-parse --abbrev-ref --symbolic-full-name @{u}` and `git status` for `ahead/behind`

2. If the branch is not pushed or is behind the remote: push with `-u` if needed.

3. Extract Jira from branch name (pattern `<type>/<JIRA>/<slug>`) to link in the body.

4. Analyze **all commits on the branch** (not just the last one) for the summary.

5. Draft title:
   - Format: `<type>(<JIRA>): <title>`
   - Max 70 chars
   - If there is only 1 commit, use its title

6. Draft body:
   ```markdown
   ## Summary
   <1-3 bullets explaining what this PR delivers>

   ## Changes
   - <file/area 1>: <change>
   - <file/area 2>: <change>

   ## Test plan
   - [ ] <step 1>
   - [ ] <step 2>

   <if there is a Jira>
   Jira: PROJ-XXX
   ```

7. Show title and body to the user, ask for confirmation or adjustments.

8. Execute with HEREDOC:
   ```bash
   gh pr create --title "<title>" --body "$(cat <<'EOF'
   <body>
   EOF
   )"
   ```

9. Return the PR URL.

## Constraints

- Never open a PR with broken tests unless explicitly labeled WIP
- Never include `Generated with Claude Code` or `Co-Authored-By` unless requested
- Check for an existing PR before creating a new one (`gh pr list --head <branch>`)

$ARGUMENTS

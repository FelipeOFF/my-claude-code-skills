# Rule: Commit format (Conventional + Jira)

Every commit must follow **Conventional Commits + Jira** in this exact format:

```
<type>(<JIRA>): <short title>

<longer description explaining the why, what changed,
and impact. 1 to 3 short paragraphs.>
```

## Allowed types

- `feat` — new feature
- `fix` — bug fix
- `chore` — maintenance, deps, build
- `docs` — docs only
- `refactor` — refactor with no behavior change
- `test` — add/adjust tests
- `perf` — performance improvement
- `style` — formatting, no code change
- `build` — build system
- `ci` — CI pipeline
- `hotfix` — urgent production fix

## Jira

- When there is a ticket: `(PROJ-123)` in parentheses right after the type
- Extract automatically from branch name when possible (see `branches.md`)
- When there is no ticket: omit parentheses → `fix: title`

## Title (after `:`)

- Sentence case (first letter capital, rest normal)
- Imperative mood: "Fix", "Add", "Remove"
- No trailing period
- Max ~70 chars
- Describes WHAT changed, not HOW

## Body

- Separated from title by one blank line
- Explains **why** the change was made, problem context, design decisions
- Wrap lines at ~80 cols
- Optional when the change is trivially obvious

## Canonical example

```
fix(PROJ-123): Fix eligibility calculation scope

The previous calculation only considered active users, but the
business rule now requires including users in triage within the
last 30 days. Fix applied in the service layer and covered by a
new integration test.

Affects the indicators dashboard and monthly export.
```

## Prohibitions

- **Never** use `--no-verify` or `--no-gpg-sign` without explicit user request
- **Never** amend commits that are already pushed
- **Never** commit files containing secrets (`.env`, `credentials.json`)
- Avoid `git add -A` / `git add .` — prefer named files

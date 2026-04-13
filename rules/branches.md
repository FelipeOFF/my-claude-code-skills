# Rule: Branch naming

Every branch name must follow:

```
<type>/<JIRA>/<slug_snake_case>
```

## Allowed types

`feat`, `fix`, `hotfix`, `chore`, `docs`, `refactor`, `test`, `perf`

## Jira

- When there is a ticket: `PROJ-123` (keep the Jira hyphen)
- When there is no ticket: reduced format `<type>/<slug>`

## Slug

- **snake_case** (underscores, not dashes)
- Short and descriptive (2-5 words)
- Lowercase, ASCII, no special chars
- Describes WHAT the PR will deliver

## Examples

```
feat/PROJ-123/change_content
fix/PROJ-410/fix_login_timeout
hotfix/PROJ-512/revert_pricing
refactor/PROJ-301/extract_auth_service
chore/update_deps
docs/readme_setup
```

## Prohibitions

- Never work directly on `main`, `master`, `develop`
- Never create branches without a type (`change_content` wrong, `feat/change_content` right)
- Never mix `kebab-case` with `snake_case` in the slug

## Integration with commits

The branch type usually matches the type of the main commit. The
branch's Jira code is extracted automatically and injected into
commits produced on that branch (see `commits.md`).

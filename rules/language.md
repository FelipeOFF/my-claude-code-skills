# Rule: Language preference

Example rule showing how to pin a non-English default language for responses while keeping technical content in English.

## Responses to the user

- **Always in the user's preferred language** (replace with yours — e.g., PT-BR, ES, FR, DE)
- Direct tone, no fluff
- Technical terms stay in English: `commit`, `branch`, `pull request`, `type-check`, `linter`, `deploy`
- Code identifiers (function, variable, class names) stay in English

## Commits

- `type` always in English: `feat`, `fix`, etc.
- Jira code always ASCII: `PROJ-123`
- **Title** can be in the preferred language, imperative mood
- **Body** can be in the preferred language

## Branches

- Type in English (`feat`, `fix`)
- Slug in lowercase ASCII snake_case English — avoids shell/CI issues
- Example: `feat/PROJ-123/change_content` (not translated)

## Documentation

- Project READMEs: follow the existing language of the repo
- New personal projects: preferred language, except for public open-source
- Inline code comments: avoid; when unavoidable, short

## Terminal output / logs

- User-facing error messages: preferred language when the audience is internal
- Technical/debug logs: English (eases searching docs/Stack Overflow)

## How to use

Copy this file to `~/.claude/rules/language.md`, replace "preferred language" with yours, then reference it from `~/.claude/CLAUDE.md`:

```markdown
@~/.claude/rules/language.md
```

# Package: programming

Curadoria de skills de programação — backend, frontend (web e mobile), testing, debugging.

## Dependências de plugins (auto-instaladas)

- `backend-patterns` @ `everything-claude-code` — APIs, data layer, server-side patterns (Node.js, Express, Next.js).
- `frontend-patterns` @ `everything-claude-code` — React/Next, state management, performance, UI.
- `api-design` @ `everything-claude-code` — REST design, status codes, paginação, error responses, versioning.
- `postgres-patterns` @ `everything-claude-code` — query optimization, schema design, indexing, security.
- `e2e-testing` @ `everything-claude-code` — Playwright, Page Object Model, CI/CD, artifact management.
- `claude-api` @ `everything-claude-code` — Anthropic SDK patterns: Messages API, streaming, tool use, prompt caching, Agent SDK.
- `agent-sdk-dev` @ `claude-plugins-official` — scaffolding e setup de novas apps Agent SDK.
- `stripe` @ `claude-plugins-official` — best practices, error explainer, test cards.
- `rust-analyzer-lsp` @ `claude-plugins-official` — LSP de Rust integrado ao CC.
- `firebase` @ `firebase` — deploy, env, projects, security rules, SDK config.

## MCPs auto-configurados

| MCP | Comando | Env vars necessárias |
|---|---|---|
| `chrome-devtools` | `npx chrome-devtools-mcp@latest` | nenhuma |
| `react-grab-mcp` | `npx -y @react-grab/mcp --stdio` | nenhuma |
| `hostinger-mcp` | `npx hostinger-api-mcp@latest` | `HOSTINGER_API_TOKEN` |

> Onde houver env var, defina antes de usar. Tokens/chaves são pessoais —
> não são compartilhados por este marketplace.

## Setup adicional (3rd-party standalone)

Rode `/programming-setup` para instalar:

| Skill | Fonte |
|---|---|
| `tdd`, `to-prd` | [mattpocock/skills](https://github.com/mattpocock/skills) |
| `obscura` | [FelipeOFF/obscura-skill](https://github.com/FelipeOFF/obscura-skill) |
| `render-plans-to-html` | [FelipeOFF/render-plans-to-html](https://github.com/FelipeOFF/render-plans-to-html) |

## Skills locais (sem fonte pública mapeada)

Documentadas como parte da curadoria do autor.

- `backend-code-review` — checklist de review para arquivos backend (`.py`).
- `frontend-code-review` — checklist de review para arquivos frontend (`.tsx`, `.ts`, `.js`).
- `code-reviewer` — review geral focado em segurança, performance e best practices.
- `debugger` — debugging sistemático com root cause analysis.
- `defuddle` — extrai markdown limpo de páginas web (alternativa ao WebFetch para economizar tokens).
- `frontend-testing` — Vitest + React Testing Library.
- `fuzzing-dictionary` — fuzzing dictionaries com tokens domain-specific.
- `fuzzing-obstacles` — técnicas para superar obstáculos de fuzzing (checksums, magic numbers).
- `property-based-testing` — PBT cross-language (Hypothesis, fast-check, proptest, QuickCheck).
- `context7-mcp` — heurísticas para chamar Context7 MCP.

## Como instalar

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install programming@myskills
/programming-setup   # opcional, instala standalone 3rd-party
```

## Como remover

```bash
/plugin uninstall programming@myskills
```

> Quando o package atingir >15 skills com agrupamento natural (≥5),
> Regra B da Constituição prevê promoção para mid-level
> (ex: `programming-frontend-mobile@myskills`).

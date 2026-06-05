---
name: programming-setup
description: Instala as poucas skills externas do package programming (não-vendorizáveis)
---

# /programming-setup

A maioria das skills de `programming` é **vendorizada** — conteúdo real no
repo, pronta logo após `/plugin install programming@myskills`. Este comando
instala apenas o que não dá pra vendorizar.

## 1. Claude API (Anthropic oficial)

Padrões do Claude API: Messages API, streaming, tool use, vision, extended
thinking, batches, prompt caching, Agent SDK.

```bash
npx skills add github:anthropics/skills --skill claude-api
```

---

> `code-review-graph` é um **MCP em Python** — requer Python 3.12 (testado em
> 3.12.1). Instruções de build/`.mcp.json` no README do package.
>
> Skills locais sem fonte pública (`backend-code-review`, `frontend-code-review`,
> `code-reviewer`, `debugger`, `defuddle`, `frontend-testing`,
> `fuzzing-dictionary`, `fuzzing-obstacles`, `property-based-testing`,
> `context7-mcp`) ficam documentadas no README — bundles do harness do Felipe
> sem distribuição pública mapeada.

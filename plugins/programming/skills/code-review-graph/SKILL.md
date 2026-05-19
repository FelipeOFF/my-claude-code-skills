---
name: code-review-graph
description: |
  Knowledge graph semântico da codebase via MCP. Mapeia arquitetura, analisa blast-radius de mudanças e faz code review com até 8x menos tokens. Usa Tree-sitter (24 linguagens) + SQLite.
source: pip
upstream: https://github.com/tirth8205/code-review-graph
license: MIT
added: 2026-05-19
---

# code-review-graph

Grafo estrutural da codebase exposto como MCP server. Parseia funções, classes e imports com Tree-sitter, constrói edges de chamadas/dependências e permite consultas semânticas sem ler arquivos individualmente.

## Setup por projeto

```bash
cd ~/Projects/meu-projeto
/Users/felipeoliveira/.asdf/installs/python/3.12.1/bin/code-review-graph build
/Users/felipeoliveira/.asdf/installs/python/3.12.1/bin/code-review-graph install --platform claude-code
crg-daemon add . --alias meu-projeto
```

O `install` cria `.mcp.json` e hooks automáticos no projeto. O `build` só precisa rodar uma vez — updates são incrementais via hook `PostToolUse`.

## Correção obrigatória pós-install

O `.mcp.json` gerado usa `uvx` que falha com asdf. Substituir sempre:

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "/Users/felipeoliveira/.asdf/installs/python/3.12.1/bin/code-review-graph",
      "args": ["serve"],
      "cwd": "/caminho/do/projeto",
      "type": "stdio"
    }
  }
}
```

## Monorepo / multi-projeto

Indexar cada subprojeto separado:

```bash
cd cortex-api && code-review-graph build && crg-daemon add . --alias cortex-api
cd cortex-frontend && code-review-graph build && crg-daemon add . --alias cortex-frontend
```

Usar `cross_repo_search_tool` para consultas cruzadas entre repos.

## Tools principais

| Tool | Quando usar |
|---|---|
| `get_minimal_context_tool` | Sempre primeiro — orienta quais outros tools chamar |
| `get_architecture_overview_tool` | Visão geral de comunidades e acoplamento |
| `get_impact_radius_tool` | Antes de alterar uma função/arquivo |
| `detect_changes_tool` | Durante code review de um diff |
| `query_graph_tool` | Busca semântica por símbolo ou conceito |
| `list_flows_tool` | Fluxos críticos e seus scores de criticidade |
| `cross_repo_search_tool` | Busca em múltiplos repos registrados no daemon |
| `find_large_functions_tool` | Identificar funções candidatas a refactor |

## Workflow token-eficiente

1. `get_minimal_context_tool` com descrição da tarefa
2. Usar `detail_level="minimal"` em todas as chamadas iniciais
3. Escalar para `"standard"` só nas entidades que precisam mais detalhe
4. Máximo 3 tool calls por turno salvo necessidade explícita

## Atenção: prompt templates quebrados

Os prompts `/code-review-graph:architecture_map` e similares têm bug na v2.3.3 (dict em vez de Message). Não usar. Pedir em linguagem natural — Claude chama os tools diretamente.

## Daemon global

O `crg-daemon` gerencia todos os repos registrados. Idempotente: chamar `start` quando já rodando é seguro. O `SessionStart` hook no `~/.claude/settings.json` sobe o daemon automaticamente em toda sessão.

```bash
crg-daemon status   # repos monitorados + PIDs
crg-daemon stop     # parar
```

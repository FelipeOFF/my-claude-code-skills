---
name: ruflo
description: |
  Plataforma de orquestração de agentes para Claude (swarms multi-agente,
  memória RAG SOTA, persistência de sessão, self-learning). Substitui o antigo
  agentmemory como camada de memória/orquestração do package workflow. Dispara
  quando o usuário pede orquestração de swarm, memória persistente avançada,
  Graph RAG multi-hop, continuidade cross-conversation, ou cita "ruflo",
  "ruflo-core", "ruflo-rag-memory", "ruflo-agentdb", "ruflo-rvf".
source: dependency
upstream: "ruflo-core@ruflo"
license: MIT
added: 2026-05-15
---

# ruflo — orquestração de agentes + memória (dependency stub)

> **Este arquivo é um stub `source: dependency` (Constituição, Regra C).**
> As skills reais do ruflo **não** vivem neste repo — chegam via
> `dependencies` cross-marketplace declaradas em
> [`plugins/workflow/.claude-plugin/plugin.json`](../../.claude-plugin/plugin.json)
> e auto-instalam quando você roda `/plugin install workflow@myskills`.
> O stub existe para documentar a origem e o fallback manual.

## O que é

[`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) (MIT) é uma plataforma
de orquestração de agentes para Claude: deploy de swarms multi-agente,
workflows coordenados, self-learning e segurança enterprise-grade.

É um **marketplace inteiro** (`ruflo`), não uma skill única. O package
`workflow` cura quatro plugins dele — escolhidos para cobrir o papel de
memória/recall que o `agentmemory` ocupava antes, com camada mais robusta:

| Plugin @ marketplace | Papel na curadoria |
|---|---|
| `ruflo-core` @ `ruflo` | Núcleo de orquestração: especialistas coder/researcher/reviewer, primitivas de coordenação de swarm. |
| `ruflo-rag-memory` @ `ruflo` | Memória RAG SOTA: hybrid search (sparse+dense), Graph RAG multi-hop, MMR diversity reranking, smart consolidation. |
| `ruflo-agentdb` @ `ruflo` | AgentDB/RuVector: memory ops, HNSW indexing, RaBitQ quantization, busca semântica via controller bridge. |
| `ruflo-rvf` @ `ruflo` | Persistência de sessão: state management, memory transfer, continuidade cross-conversation (equivalente a recall/remember/forget). |

## Como é instalado (automático)

```bash
/plugin install workflow@myskills
```

O marketplace `ruflo` está na whitelist
[`allowCrossMarketplaceDependenciesOn`](../../../../.claude-plugin/marketplace.json)
e os quatro plugins estão declarados em `plugin.json` — instalam juntos
com o package `workflow`.

## Fallback manual (se a dep cross-marketplace falhar)

Se a auto-instalação não rodar (offline na 1ª sessão, marketplace fora
do ar), instale manualmente:

```bash
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
/plugin install ruflo-rag-memory@ruflo
/plugin install ruflo-agentdb@ruflo
/plugin install ruflo-rvf@ruflo
```

Modo MCP completo (opcional, mais poderoso que o modo plugin lite):

```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

## Quando NÃO usar

- Notas/memória triviais de uma sessão só → memória de arquivo nativa.
- Memória cross-session de leitura/timeline → `claude-mem` (já no package).
- Não confundir com `agentmemory` — este foi **removido** e substituído
  por ruflo nesta curadoria.

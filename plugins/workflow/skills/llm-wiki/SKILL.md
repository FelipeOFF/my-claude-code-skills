---
name: llm-wiki
description: Mantém uma knowledge base persistente no Obsidian seguindo o pattern Karpathy LLM Wiki — ingest de sources, query sobre wiki compilado, lint de saúde. Dispara quando o usuário pede "ingest", "alimenta o wiki", "atualiza wiki", "consulta wiki", "lint wiki", "/wiki-ingest", "/wiki-query", "/wiki-lint", "que sabemos sobre X", "compila X no wiki", "adiciona ao wiki", ou ao salvar uma nova source em References/.
triggers:
  - /wiki-ingest
  - /wiki-query
  - /wiki-lint
  - "ingere isso no wiki"
  - "alimenta o wiki com"
  - "atualiza o wiki sobre"
  - "consulta o wiki sobre"
  - "o que o wiki sabe sobre"
  - "lint do wiki"
  - "compila X no wiki"
---

# llm-wiki — Knowledge Base mantida por LLM

Implementação do pattern [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
para o vault Obsidian do Felipe (`~/obsidian-vault`).

> **Princípio:** Em vez de retrievar de documentos crus a cada query, o LLM
> **compila e mantém** um wiki persistente. Conhecimento é construído uma vez
> e atualizado incrementalmente. Queries futuras leem síntese pronta.

---

## Camadas (não confundir)

| Camada | Path | Quem escreve |
|---|---|---|
| **Raw sources** | `~/obsidian-vault/References/`, `00-Inbox/`, daily notes, PDFs | Felipe (curador) — **imutável** após captura |
| **Wiki** | `~/obsidian-vault/Wiki/{entities,concepts,syntheses,comparisons,patterns}/` | LLM (você) |
| **Schema** | `~/obsidian-vault/Wiki/README.md` + esta SKILL.md | Felipe + LLM |

**Regra de ouro:** Nunca modifique `References/`. Apenas leia. Tudo que você
escreve vai para `Wiki/`.

---

## Os 3 workflows

### 1. INGEST — `/wiki-ingest <source>` ou trigger natural

Quando Felipe adiciona uma source nova (artigo, paper, podcast notes, PDF,
arquivo em `References/`) e pede pra processar.

**Fluxo:**

1. **Leia a source completa** (use Read, não amostragem).
2. **Identifique entidades e conceitos** mencionados:
   - Pessoas, empresas, ferramentas, projetos → `entities/`
   - Ideias, técnicas, padrões → `concepts/`
3. **Procure pages existentes** em `Wiki/index.md`:
   - Se entity/concept já existe → **atualize** essa page (acrescenta info nova, registra contradições)
   - Se não existe → **crie** nova page seguindo o template
4. **Atualize/crie synthesis** se a source contribui para um tópico maior já trackeado.
5. **Atualize `Wiki/index.md`** — categoria correta + one-line summary atualizado.
6. **Acrescente entry no `Wiki/log.md`**:
   ```markdown
   ## [YYYY-MM-DD HH:MM] ingest | <Source Title>
   - Pages tocadas: <list>
   - Insights chave: <2-3 bullets>
   ```
7. **Reporte para Felipe** em PT-BR curto: o que mudou, contradições flagradas, pages novas.

**Uma source típica toca 5-15 pages.**

#### Template — Entity page (`Wiki/entities/<Name>.md`)

```markdown
---
title: "<Name>"
type: entity
entity_type: person | company | tool | project | named-concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[References/Source A]]"
tags: [...]
status: stub | draft | mature
aliases: []
---

# <Name>

> One-line definition.

## O que é

2-4 parágrafos sintetizando o que sabemos.

## Fatos chave

- Fato 1 (fonte: [[References/Source A]])
- Fato 2 (fonte: [[References/Source B]])

## Conexões

- Relaciona-se com [[entities/Outra Entity]] porque…
- Implementa [[concepts/Conceito]]
- Contrasta com [[entities/Concorrente]]

## Contradições / Open questions

- Source X afirma A, source Y afirma not-A — não resolvido.

## Linha do tempo

- YYYY-MM-DD — evento (fonte: …)

## Sources

- [[References/Source A]]
- [[References/Source B]]
```

#### Template — Concept page (`Wiki/concepts/<slug>.md`)

```markdown
---
title: "<Concept Name>"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
tags: [...]
status: stub | draft | mature
---

# <Concept Name>

> Definição em 1-2 frases.

## Ideia central

Explicação aprofundada.

## Quando aplicar

- Contexto 1
- Contexto 2

## Trade-offs

| Prós | Contras |
|---|---|

## Implementações conhecidas

- [[entities/Tool A]] implementa isto via …

## Relacionado

- [[concepts/Outro]] — diferença é…

## Sources
```

#### Template — Synthesis page (`Wiki/syntheses/<slug>.md`)

```markdown
---
title: "O que sabemos sobre <Tópico>"
type: synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
tags: [...]
status: draft | mature
---

# O que sabemos sobre <Tópico>

> TL;DR em 3-5 linhas.

## Estado atual da tese

Síntese viva, atualizada a cada nova source.

## Evidências fortes

- [[References/X]] mostra que…

## Evidências fracas / em debate

- [[References/Y]] sugere…

## Contradições

- Tensão entre [[References/A]] e [[References/B]].

## Próximas perguntas

- O que ainda não sabemos.

## Sources
```

#### Template — Comparison page (`Wiki/comparisons/<a-vs-b>.md`)

```markdown
---
title: "<A> vs <B>"
type: comparison
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
status: draft | mature
---

# <A> vs <B>

> Em uma frase: quando usar cada um.

## Matriz

| Dimensão | <A> | <B> |
|---|---|---|

## Quando escolher <A>

## Quando escolher <B>

## Sources
```

---

### 2. QUERY — `/wiki-query <pergunta>` ou pergunta natural

Quando Felipe pergunta algo que pode ser respondido pelo wiki.

**Fluxo:**

1. **Leia `Wiki/index.md`** primeiro — identifique pages candidatas.
2. **Drill** nas pages relevantes (Read).
3. **Sintetize resposta com citações** — todo claim cita `[[Wiki/...]]` ou `[[References/...]]`.
4. **Decida se vale filar de volta:**
   - Pergunta gerou comparison nova? → cria `Wiki/comparisons/<x>.md`
   - Pergunta puxou síntese nova? → cria/atualiza `Wiki/syntheses/<x>.md`
   - Pergunta achou gap? → registra no `log.md` como gap detectado
5. **Atualize log:**
   ```markdown
   ## [YYYY-MM-DD HH:MM] query | <pergunta resumida>
   - Pages consultadas: <list>
   - Filed back: <page nova se houve>
   ```

**Não responda do training data quando o wiki/sources cobrem o tópico.**
Diga "Wiki não tem isso ainda — quer que eu ingira fontes?" se for o caso.

---

### 3. LINT — `/wiki-lint`

Health-check periódico. Quando Felipe pede ou ao detectar wiki >50 pages.

**Checklist:**

```markdown
## Wiki Health Report — YYYY-MM-DD

### Contradições detectadas
- [[Wiki/X]] afirma A; [[Wiki/Y]] afirma not-A — sugerir resolução.

### Claims stale
- [[Wiki/Z]] cita source de 2024; existe source 2026 mais recente em References/.

### Orphan pages (zero inbound)
- [[Wiki/...]] — sugerir conectar a … ou arquivar.

### Conceitos mencionados sem page
- Termo "X" aparece em 5+ pages mas não tem entry própria. Criar?

### Cross-references faltando
- [[Wiki/A]] menciona conceito Y mas não linka [[Wiki/concepts/Y]].

### Data gaps preencháveis
- Tópico Z tem apenas 1 source. Sugerir busca web.

### Sugestões
- Próximas perguntas que valem ingerir.
- Próximas sources a buscar.
```

Salve relatório em `Wiki/lint-reports/lint-YYYY-MM-DD.md` (crie pasta se não existir).

Registre no `log.md`:
```markdown
## [YYYY-MM-DD HH:MM] lint | <N issues found>
```

---

## Regras estritas

1. **Toda claim no wiki cita pelo menos 1 source** (via `[[References/...]]`).
2. **Wikilinks Obsidian sempre**: `[[entities/X]]` ou `[[X]]` (relativo se ambíguo).
3. **Index.md é fonte de verdade do catálogo.** Após cada ingest/query/lint, atualize.
4. **Log.md é append-only.** Nunca edite entries passadas.
5. **Sources em `References/` são imutáveis.** Você apenas lê.
6. **PT-BR para tudo** (frontmatter em inglês para chaves, valores em PT é ok).
7. **Frontmatter `updated:` muda a cada edit.**
8. **`status: stub` → `draft` → `mature`** conforme page ganha sources.
9. **Contradições não são bug — são feature.** Registre-as explicitamente em "Contradições / Open questions".
10. **Não invente sources.** Se não há source, marque como `inferência` ou `não verificado`.

---

## Quando NÃO usar essa skill

- Tarefa de código → use skills de programação.
- Quick capture de uma nota solta → use `scribe` agent do vault.
- Busca em código/projeto → use Read/Grep direto.
- O usuário só quer ler uma source, não compilar → não ingere automaticamente.

---

## Ferramentas auxiliares

- `Read` para sources e pages do wiki.
- `Write`/`Edit` para criar/atualizar pages.
- `Glob`/`Grep` para encontrar pages existentes antes de criar duplicata.
- MCP `claude-mem:search` para checar memória de sessões passadas relacionadas ao tópico.

---

## Pattern de referência

[[References/Karpathy LLM Wiki - Personal Knowledge Base]] no vault.
Gist original: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

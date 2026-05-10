# MySkills Constitution

> Documento canônico das regras de curadoria do marketplace `myskills`.
> Lido por Claude Code em sessões dentro deste repo para rotear
> automaticamente comandos como "sobe a skill X aqui".

**Versão:** 1.1 (2026-05-10)

---

## Packages top-level

| Package | Escopo |
|---|---|
| `design` | UI/UX, design system, taste, mockups, prototipagem visual. |
| `copy` | Copywriting, headlines, escrita persuasiva, edição. |
| `marketing` | SEO, CRO, tráfego pago, email, social, growth. |
| `programming` | Backend, frontend (web e mobile), testing, debugging, infra, stacks. |
| `workflow` | Meta-workflow: planning, memória, multi-phase, autonomous loops, multi-agent orchestration. |

Skills autorais do Felipe que **não** entram em packages: agents
(`commit-crafter`, `jira-linker`, `pr-writer`), commands (`branch`,
`commit`, `pr`, `review`, `wt`), rules (`branches`, `commits`,
`context7`, `language`, `workflow`). Permanecem na raiz e são
consumidas via `~/.claude/CLAUDE.md` global.

---

## Regra A — Localização única

Uma skill mora em **exatamente um** package. Critério de tie-break para
skills cross-domínio:

1. Se a skill é sobre uma **stack/tecnologia** → `programming`.
2. Se a skill é sobre um **objetivo de negócio** (vender, escrever, atrair) → `marketing` ou `copy`.
3. Se a skill é sobre **estética visual** → `design`.
4. Em empate genuíno, vai para o package onde já há mais skills do mesmo autor/marketplace upstream.

### Exemplos de classificação

| Skill | Package | Justificativa |
|---|---|---|
| `frontend-patterns` | `programming` | Stack/tecnologia (Regra A.1). |
| `huashu-design` | `design` | Estética visual / prototipagem (Regra A.3). |
| `seo` | `marketing` | Objetivo de negócio: tráfego (Regra A.2). |
| `api-design` | `programming` | Stack (REST) — não é objetivo de negócio. |
| `tdd` | `programming` | Stack/processo de engenharia. |

---

## Regra B — Top-level por default; mid-level por crescimento

Novas skills entram nos 4 packages raiz: `design`, `copy`, `marketing`,
`programming`.

Mid-level (ex: `programming-frontend-mobile`) só nasce quando:

- Package raiz tem **>15 skills** **AND**
- Existe um agrupamento natural com **≥5 skills** de coesão clara

Quando criado, o mid-level é um **novo plugin no marketplace**
(`plugins/programming-frontend-mobile/`), não um sub-diretório dentro
do raiz. Skills migradas saem do raiz; o README do raiz ganha
referência cruzada: "veja também `programming-frontend-mobile@myskills`".

Promoção é breaking change: bump major do plugin pai (1.x → 2.0).

---

## Regra C — Frontmatter estendido em SKILL.md

Toda skill no repo (qualquer package) tem frontmatter declarando origem:

```yaml
---
name: minha-skill
description: |
  Use quando ... Triggers em "X", "Y", "Z".
source: authored                      # authored | dependency | standalone-setup
upstream: null                        # null | "<plugin>@<marketplace>" | URL
license: MIT                          # SPDX identifier (se aplicável)
added: YYYY-MM-DD
---
```

- `source: authored` → conteúdo no repo, autoria do Felipe.
- `source: dependency` → arquivo é stub documentando que a skill real
  vem via `dependencies` cross-marketplace. O stub explica como
  instalar manualmente caso a dep falhe.
- `source: standalone-setup` → idem stub, mas a instalação é via
  `/<package>-setup`.

---

## Regra D — README de package padronizado

Cada `plugins/<nome>/README.md` segue o template:

```markdown
# Package: <nome>

<Descrição de uma linha sobre o escopo.>

## Skills autorais incluídas
- skill-x — descrição curta

## Dependências de plugins (auto-instaladas)
- <plugin> @ <marketplace> — descrição

## Setup adicional (3rd-party standalone)
Rode `/<nome>-setup` para instalar:
- nome-skill — fonte: github.com/...

## Como instalar
## Como remover
```

---

## Regra E — Esta Constituição é a fonte da verdade

- Referenciada explicitamente no `CLAUDE.md` da raiz do repo.
- Lida por Claude Code nas primeiras tool calls de qualquer sessão
  dentro do repo.
- Mudanças nas regras (A–E) são commits `docs:` com discussão prévia
  no spec/plano correspondente em `docs/superpowers/`.

---

## Procedimento "sobe essa skill aqui"

Quando o usuário pede para adicionar uma skill ao MySkills, Claude segue:

1. **Origem:** a skill é autoral, dependency de marketplace conhecido,
   ou standalone (npx/git clone)?
2. **Classificação:** aplica Regra A. Se ambíguo, usa AskUserQuestion.
3. **Aplicação:**
   - Autoral → cria `plugins/<pkg>/skills/<skill>/SKILL.md` com
     frontmatter Regra C.
   - Dependency → adiciona em `plugins/<pkg>/.claude-plugin/plugin.json`.
   - Standalone → adiciona linha em `plugins/<pkg>/commands/setup.md`.
4. **README:** atualiza `plugins/<pkg>/README.md` (Regra D).
5. **Commit:** `feat(<pkg>): Adiciona skill <nome>` — segue padrão Felipe
   (conventional commits + corpo PT-BR).

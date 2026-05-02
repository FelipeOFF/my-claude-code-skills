# My Claude Code Skills

A curated collection of **130+ skills** installed in my Claude Code setup. This list is meant to help teammates and collaborators quickly replicate the same environment.

> **What are skills?** Skills are reusable prompt modules that teach Claude Code how to approach specific tasks — from debugging to design systems to deployment. They live in `~/.claude/skills/` or are installed via plugins and marketplaces.

---

## Table of Contents

- [Quick Setup](#quick-setup)
- [Plugins & Marketplaces](#plugins--marketplaces)
- [Codex (OpenAI)](#codex-openai)
- [GSD — Get Shit Done](#gsd--get-shit-done)
- [Obsidian Skills](#obsidian-skills)
- [UI/UX Pro Max](#uiux-pro-max)
- [21st.dev — Magic MCP](#21stdev--magic-mcp)
- [Design Resources & Inspiration](#design-resources--inspiration)
- [ECC — Everything Claude Code](#ecc--everything-claude-code)
- [Stitch Skills (Google Labs)](#stitch-skills-google-labs)
- [Matt Pocock Skills](#matt-pocock-skills)
- [Huashu Design](#huashu-design)
- [Community Skills](#community-skills)
- [Marketing Skills](#marketing-skills)
- [Custom Skills](#custom-skills)
- [Personal Rules, Commands & Agents](#personal-rules-commands--agents)
- [ByteRover](#byterover)
- [Installation Guide](#installation-guide)

---

## Quick Setup

Run these commands to replicate this full setup:

```bash
# 1. GSD (Get Shit Done) — meta-prompting & spec-driven dev
npx -y get-shit-done-cc@latest --global

# 2. Obsidian Skills — markdown, bases, canvas, CLI
npx skills add git@github.com:kepano/obsidian-skills.git -y

# 3. UI/UX Pro Max — design intelligence
npm install -g uipro-cli && uipro init --ai claude

# 4. Frontend Project Style — configurable design system
npx skills add git@github.com:FelipeOFF/frontend-project-style-skill.git

# 5. Plugins (run inside Claude Code)
# /plugin marketplace add superpowers
# /plugin install superpowers@superpowers
# /plugin marketplace add claude-plugins-official
# /plugin install frontend-design
# /plugin install agent-sdk-dev
# /plugin install stripe
# /plugin marketplace add thedotmack
# /plugin install claude-mem
# /plugin marketplace add firebase
# /plugin install firebase
# /plugin marketplace add openai-codex
# /plugin install codex@openai-codex
# /plugin marketplace add nowork-studio/toprank
# /plugin install toprank
# /plugin install claude-code-setup@claude-plugins-official

# 6. Skills via npx skills (Stitch, Matt Pocock, Huashu)
npx skills add git@github.com:google-labs-code/stitch-skills.git -y
npx skills add git@github.com:mattpocock/skills.git -y
npx skills add git@github.com:alchaincyf/huashu-design.git -y
```

---

## Plugins & Marketplaces

Installed via Claude Code's `/plugin` command system.

### Superpowers (v5.0.0)

> **Source:** [github.com/obra/superpowers](https://github.com/obra/superpowers)
> **Marketplace:** [github.com/obra/superpowers-marketplace](https://github.com/obra/superpowers-marketplace)

| Skill | When to Use |
|-------|-------------|
| `brainstorming` | Before any creative work — features, components, modifications |
| `writing-plans` | When you have specs/requirements for a multi-step task |
| `executing-plans` | When you have a written plan to execute with review checkpoints |
| `systematic-debugging` | When encountering any bug, test failure, or unexpected behavior |
| `test-driven-development` | When implementing any feature or bugfix, before writing code |
| `dispatching-parallel-agents` | When facing 2+ independent tasks without shared state |
| `subagent-driven-development` | When executing plans with independent tasks in the current session |
| `verification-before-completion` | Before claiming work is complete, fixed, or passing |
| `requesting-code-review` | When completing tasks or before merging |
| `receiving-code-review` | When receiving code review feedback, before implementing suggestions |
| `writing-skills` | When creating or editing skills |
| `finishing-a-development-branch` | When implementation is complete and you need to integrate |
| `using-git-worktrees` | When starting feature work that needs isolation |

### Frontend Design

> **Source:** Anthropic Official Marketplace

| Skill | When to Use |
|-------|-------------|
| `frontend-design` | Creating distinctive, production-grade frontend interfaces |

### Agent SDK Dev

> **Source:** Anthropic Official Marketplace

| Skill | When to Use |
|-------|-------------|
| `new-sdk-app` | Create a new Claude Agent SDK application |
| `agent-sdk-verifier-ts` | Verify TypeScript Agent SDK apps |
| `agent-sdk-verifier-py` | Verify Python Agent SDK apps |

### Stripe

> **Source:** Anthropic Official Marketplace

| Skill | When to Use |
|-------|-------------|
| `test-cards` | Display Stripe test card numbers |
| `explain-error` | Explain Stripe error codes with solutions |
| `stripe-best-practices` | Implementing payment processing, subscriptions, webhooks |

### Claude Mem

> **Source:** [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

| Skill | When to Use |
|-------|-------------|
| `make-plan` | Create phased implementation plans with documentation discovery |
| `mem-search` | Search persistent cross-session memory |
| `smart-explore` | Token-optimized structural code search using tree-sitter AST |
| `do` | Execute phased plans using subagents |

### LSP Plugins (TypeScript / Rust)

> **Source:** Anthropic Official Marketplace

| Plugin | Purpose |
|--------|---------|
| `typescript-lsp` | TypeScript language server integration |
| `rust-analyzer-lsp` | Rust language server integration |

### Firebase

> **Source:** Google/Firebase Marketplace

Full Firebase toolset: Auth, Firestore, Realtime Database, Storage, Remote Config, Messaging, and project management.

### TopRank

> **Source:** [github.com/nowork-studio/toprank](https://github.com/nowork-studio/toprank)
> **Install:** `/plugin marketplace add nowork-studio/toprank` then `/plugin install toprank`

Suite de skills focada em SEO técnico, on-page e Google Ads — auditoria, pesquisa de keywords, geração de conteúdo otimizado, structured data e gerenciamento de campanhas pagas dentro do Claude Code.

| Skill | Description |
|-------|-------------|
| `seo-analysis` | Auditoria SEO completa integrando Google Search Console, GA4 e Bing |
| `keyword-research` | Descoberta, análise e priorização de keywords |
| `content-writer` | Escreve blog posts, landing pages e conteúdo otimizado para SEO |
| `meta-tags-optimizer` | Otimiza title tags, meta descriptions e Open Graph |
| `schema-markup-generator` | Gera JSON-LD structured data |
| `ads` | Gerencia campanhas Google Ads — performance, keywords, bidding |
| `ads-audit` | Auditoria de conta Google Ads e contexto de negócio |
| `ads-copy` | Gera e roda A/B test em copy de Google Ads |
| `ads-landing` | Diagnostica e pontua landing pages de Google Ads |
| `setup-cms` | Conecta um CMS às ferramentas SEO |
| `gemini` | Segunda opinião cross-model usando Google Gemini |
| `toprank-upgrade` | Atualiza o plugin toprank para a última versão |

### Claude Code Setup

> **Source:** Anthropic Official Marketplace ([claude-plugins-official](https://github.com/anthropics/claude-plugins))
> **Install:** `/plugin install claude-code-setup@claude-plugins-official`

| Skill | When to Use |
|-------|-------------|
| `claude-automation-recommender` | Analisa o codebase e recomenda automações sob medida — hooks, skills, MCP servers, subagents e slash commands. Read-only, não modifica arquivos. |

---

## Codex (OpenAI)

> **Marketplace:** `openai-codex`
> **Install:** `/plugin install codex@openai-codex`

Delegate investigations and second-opinion implementations to the Codex CLI.

| Skill | Description |
|-------|-------------|
| `rescue` | Delegate investigation, fix requests, or follow-up rescue work to the Codex rescue subagent |
| `setup` | Check whether the local Codex CLI is ready and optionally toggle the stop-time review gate |
| `gpt-5-4-prompting` | Internal guidance for composing Codex / GPT-5.4 prompts |
| `codex-result-handling` | Internal guidance for presenting Codex helper output back to the user |
| `codex-cli-runtime` | Internal helper contract for calling the codex-companion runtime |

---

## GSD — Get Shit Done

> **Version:** 1.25.1
> **Source:** [github.com/glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done)
> **Install:** `npx -y get-shit-done-cc@latest --global`

A meta-prompting, context engineering, and spec-driven development system.

### Project Setup

| Command | Description |
|---------|-------------|
| `/gsd:new-project` | Initialize a new project with deep context gathering |
| `/gsd:new-milestone` | Start a new milestone cycle |
| `/gsd:map-codebase` | Analyze codebase with parallel mapper agents |
| `/gsd:settings` | Configure workflow toggles and model profile |
| `/gsd:set-profile` | Switch model profile (quality/balanced/budget/inherit) |

### Planning

| Command | Description |
|---------|-------------|
| `/gsd:discuss-phase` | Gather context through adaptive questioning before planning |
| `/gsd:plan-phase` | Create detailed phase plan (PLAN.md) with verification loop |
| `/gsd:research-phase` | Research how to implement a phase (standalone) |
| `/gsd:add-phase` | Add phase to end of current milestone |
| `/gsd:insert-phase` | Insert urgent work as decimal phase (e.g., 72.1) |
| `/gsd:remove-phase` | Remove a future phase and renumber |
| `/gsd:list-phase-assumptions` | Surface Claude's assumptions about a phase |
| `/gsd:ui-phase` | Generate UI design contract (UI-SPEC.md) for frontend phases |

### Execution

| Command | Description |
|---------|-------------|
| `/gsd:execute-phase` | Execute all plans with wave-based parallelization |
| `/gsd:autonomous` | Run all remaining phases autonomously |
| `/gsd:quick` | Execute a quick task with GSD guarantees |
| `/gsd:do` | Route freeform text to the right GSD command |

### Verification & Testing

| Command | Description |
|---------|-------------|
| `/gsd:verify-work` | Validate built features through conversational UAT |
| `/gsd:validate-phase` | Retroactively audit and fill Nyquist validation gaps |
| `/gsd:add-tests` | Generate tests based on UAT criteria and implementation |
| `/gsd:ui-review` | Retroactive 6-pillar visual audit of frontend code |
| `/gsd:audit-milestone` | Audit milestone completion against original intent |

### Project Management

| Command | Description |
|---------|-------------|
| `/gsd:progress` | Check project progress, show context, route to next action |
| `/gsd:stats` | Display project statistics — phases, plans, requirements, git metrics |
| `/gsd:note` | Zero-friction idea capture (append, list, promote) |
| `/gsd:add-todo` | Capture idea or task as todo |
| `/gsd:check-todos` | List pending todos and select one to work on |
| `/gsd:pause-work` | Create context handoff when pausing mid-phase |
| `/gsd:resume-work` | Resume work from previous session with full context |
| `/gsd:plan-milestone-gaps` | Create phases to close gaps from milestone audit |
| `/gsd:complete-milestone` | Archive completed milestone and prepare for next |

### Maintenance

| Command | Description |
|---------|-------------|
| `/gsd:debug` | Systematic debugging with persistent state |
| `/gsd:health` | Diagnose planning directory health |
| `/gsd:cleanup` | Archive accumulated phase directories |
| `/gsd:update` | Update GSD to latest version |
| `/gsd:reapply-patches` | Reapply local modifications after update |
| `/gsd:help` | Show available commands and usage guide |
| `/gsd:join-discord` | Join the GSD Discord community |

---

## Obsidian Skills

> **Source:** [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
> **Install:** `npx skills add git@github.com:kepano/obsidian-skills.git -y`

| Skill | Description |
|-------|-------------|
| `obsidian-markdown` | Create/edit Markdown with Obsidian syntax — wikilinks, embeds, callouts, properties |
| `obsidian-bases` | Create/edit `.base` files with views, filters, formulas, and summaries |
| `obsidian-cli` | Interact with Obsidian vaults via CLI — notes, tasks, properties, plugin dev |
| `json-canvas` | Create/edit `.canvas` files with nodes, edges, groups, and connections |
| `defuddle` | Extract clean markdown from web pages, removing clutter to save tokens |

---

## UI/UX Pro Max

> **Source:** [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> **Install:** `npm install -g uipro-cli && uipro init --ai claude`

AI-powered design intelligence for building professional UIs:

- **67 UI styles** — glassmorphism, brutalism, neumorphism, dark mode variants, and more
- **96 color palettes** aligned with product categories
- **57 font pairings** from Google Fonts
- **161 industry-specific reasoning rules** (SaaS, fintech, healthcare, e-commerce)
- **13 supported tech stacks** (React, Next.js, Vue, Svelte, SwiftUI, Flutter, etc.)
- **25 chart types** for data visualization

Integrates with [21st.dev](https://21st.dev/) MCP for component search, examples, and inspiration.

---

## 21st.dev — Magic MCP

> **Source:** [21st.dev](https://21st.dev/)
> **MCP Tool:** Available as `mcp__magic__21st_magic_component_builder`, `mcp__magic__21st_magic_component_inspiration`, `mcp__magic__21st_magic_component_refiner`, and `mcp__magic__logo_search`

AI-powered component generation and design inspiration platform. Provides:

| Tool | Description |
|------|-------------|
| `21st_magic_component_builder` | Generate production-ready UI components from natural language descriptions |
| `21st_magic_component_inspiration` | Browse and get inspiration from a curated library of UI components |
| `21st_magic_component_refiner` | Refine and improve existing components with AI assistance |
| `logo_search` | Search for logos and brand assets |

Works as an MCP server connected to Claude Code, providing real-time component generation and design system integration.

---

## Design Resources & Inspiration

> Coleção curada de sites, plataformas e repositórios usados como referência de **design** — inspiração visual, bibliotecas de componentes, builders no-code/AI, design systems, agregadores de UI mobile/web e ferramentas de bridge entre design e código.

Não são skills nem plugins instaláveis — são **fontes externas** consultadas durante o trabalho de UI/UX para colher referências, baixar padrões, gerar componentes ou estudar interações.

### Plataformas & Marketplaces

| Recurso | Tipo | Descrição |
|---------|------|-----------|
| [21st.dev](https://21st.dev/) | Component marketplace + MCP | Marketplace de componentes UI gerados/curados por IA. Integra-se ao Claude Code via `mcp__magic__*` para gerar, refinar e buscar componentes a partir de linguagem natural. Também expõe `logo_search` para assets de marca. |
| [motionsites.ai](https://motionsites.ai/) | Galeria de sites com animação | Showcase curado de sites focados em **motion design** e micro-interações. Útil para benchmarking de animações, transições e storytelling visual em landing pages. |
| [Mobbin](https://mobbin.com/discover/apps/web/latest) | Library de UI patterns | Maior biblioteca pública de **screens reais** de apps mobile e web — fluxos de onboarding, checkout, paywall, settings, empty states. Filtrável por indústria, plataforma e padrão de UX. Referência canônica para benchmarking de fluxos. |
| [Webflow](https://webflow.com/?r=0) | No-code visual builder | Ferramenta visual para construir sites production-grade com controle pixel-perfect sobre layout, animações e CMS. Útil como referência de capabilities (o que é possível sem código) e para protótipos hi-fi entregáveis. |
| [Aura](https://www.aura.build/) | AI website builder | Builder de websites movido a IA — gera landing pages, portfolios e sites institucionais a partir de prompts. Boa referência para entender o estado atual de **AI-native site generation** e para gerar baselines rápidos. |
| [Asimov Academy — SD](https://sd.asimov.academy/) | Curso/recurso de Design | Material e curso da Asimov Academy focado em design (`sd` = Software Design / Stable Diffusion / Skill Design, conforme contexto). Referência para fundamentos e workflows de design assistido por IA em PT-BR. |

### Design Systems & Registries

| Recurso | Tipo | Descrição |
|---------|------|-----------|
| [designdotmd.directory](https://designdotmd.directory/#/) | Diretório `design.md` | Diretório de arquivos `design.md` — padrão emergente de **design-as-code** onde decisões de design (tokens, princípios, componentes) ficam versionadas em markdown legível por agentes de IA. Útil para estudar como outros times documentam design para consumo por LLMs. |
| [monet-design / monet-registry](https://github.com/monet-design/monet-registry) | Component registry | Registry de componentes do design system **Monet** — distribuição via CLI no estilo `shadcn/ui` (copy-paste de componentes versionados com tokens). Referência para construir registries próprios e padrões de distribuição de componentes. |

### Bridges entre Design e Código

| Recurso | Tipo | Descrição |
|---------|------|-----------|
| [picasso-claude-design-claude-code-bridge-loop](https://github.com/RazvanGabrielNiculae/picasso-claude-design-claude-code-bridge-loop) | Workflow / repositório | Implementação de **loop bridge** entre Claude (design) e Claude Code (implementação) — o agente de design produz especificações que o agente de código consome, com feedback iterativo. Padrão excelente para automatizar o pipeline design → código. |

### Ferramentas de Coleta e APIs

| Recurso | Tipo | Descrição |
|---------|------|-----------|
| [aayushsoam/motionsites.ai](https://github.com/aayushsoam/motionsites.ai) | Repositório fonte | Código-fonte público do agregador motionsites.ai. Útil para entender como construir um diretório curado de sites com motion design e como organizar metadata/tags de animação. |
| [asimov-academy/Website-Downloader](https://github.com/asimov-academy/Website-Downloader) | CLI tool | Ferramenta para **baixar sites inteiros** (HTML, CSS, JS, assets) para análise offline. Ideal para dissecar referências de design, estudar implementações e alimentar agentes de IA com contexto visual completo de um site. |
| [underthestars-zhy/MobbinAPI](https://github.com/underthestars-zhy/MobbinAPI) | API não-oficial | Wrapper não-oficial para acessar dados do Mobbin programaticamente. Permite scriptar busca de screens, exportar referências e alimentar pipelines de inspiração automatizados. **Atenção:** uso sujeito aos ToS do Mobbin. |

### Como uso no fluxo

1. **Inspiração & benchmarking** → Mobbin (fluxos), motionsites.ai (animação), Webflow showcase (capabilities)
2. **Componentes prontos** → 21st.dev (via MCP no Claude Code), Monet Registry
3. **Design-as-code** → designdotmd.directory para padrões de `DESIGN.md` consumíveis por agentes
4. **Pipelines automatizados** → picasso bridge loop (design ↔ código), Website-Downloader + MobbinAPI para coleta
5. **Geração rápida** → Aura (AI builder), 21st Magic MCP (componentes sob demanda), skill Stitch (telas hi-fi)

---

## ECC — Everything Claude Code

> **Source:** [github.com/anthropics/ecc](https://github.com/anthropics/ecc)
> **Monorepo:** [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)

A large collection of general-purpose development skills.

### API & Architecture

| Skill | Description |
|-------|-------------|
| [`api-design`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/api-design) | REST API patterns — resource naming, status codes, pagination, error responses |
| [`backend-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/backend-patterns) | Backend architecture, API design, database optimization (Node.js, Express, Next.js) |
| [`frontend-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/frontend-patterns) | React, Next.js, state management, performance optimization |
| [`coding-standards`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/coding-standards) | Universal coding standards for TypeScript, JavaScript, React, Node.js |

### Python

| Skill | Description |
|-------|-------------|
| [`python-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/python-patterns) | Pythonic idioms, PEP 8, type hints, best practices |
| [`python-testing`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/python-testing) | pytest, TDD, fixtures, mocking, parametrization, coverage |

### Django

| Skill | Description |
|-------|-------------|
| [`django-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/django-patterns) | Django architecture, DRF, ORM, caching, signals, middleware |
| [`django-security`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/django-security) | Authentication, authorization, CSRF, SQL injection, XSS prevention |
| [`django-tdd`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/django-tdd) | Testing with pytest-django, factory_boy, mocking, coverage |
| [`django-verification`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/django-verification) | Migrations, linting, tests, security scans, deployment readiness |

### C++

| Skill | Description |
|-------|-------------|
| [`cpp-coding-standards`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/cpp-coding-standards) | C++ Core Guidelines — modern, safe, idiomatic practices |
| [`cpp-testing`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/cpp-testing) | GoogleTest/CTest, failing/flaky tests, coverage/sanitizers |

### Databases

| Skill | Description |
|-------|-------------|
| [`postgres-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/postgres-patterns) | PostgreSQL query optimization, schema design, indexing, security |
| [`clickhouse-io`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/clickhouse-io) | ClickHouse analytics, query optimization, data engineering |
| [`database-migrations`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/database-migrations) | Schema changes, data migrations, rollbacks, zero-downtime deployments |

### Testing & Quality

| Skill | Description |
|-------|-------------|
| [`tdd-workflow`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/tdd-workflow) | TDD with 80%+ coverage — unit, integration, E2E |
| [`e2e-testing`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/e2e-testing) | Playwright, Page Object Model, CI/CD, artifact management |
| [`verification-loop`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/verification-loop) | Comprehensive verification system for Claude Code sessions |
| [`eval-harness`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/eval-harness) | Eval-driven development (EDD) framework |

### DevOps & Infrastructure

| Skill | Description |
|-------|-------------|
| [`docker-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/docker-patterns) | Docker/Compose for local dev, container security, networking |
| [`deployment-patterns`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/deployment-patterns) | CI/CD pipelines, health checks, rollback strategies |
| [`security-review`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/security-review) | Security checklist for auth, user input, secrets, API endpoints |
| [`security-scan`](https://github.com/affaan-m/agentshield) | AgentShield config scanning for `~/.claude/` |

### AI & LLM

| Skill | Description |
|-------|-------------|
| [`cost-aware-llm-pipeline`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/cost-aware-llm-pipeline) | Model routing by task complexity, budget tracking, prompt caching |
| [`regex-vs-llm-structured-text`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/regex-vs-llm-structured-text) | Decision framework: regex vs LLM for parsing structured text |

### Content & Writing

| Skill | Description |
|-------|-------------|
| [`article-writing`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/article-writing) | Long-form content with distinctive voice |
| [`content-engine`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/content-engine) | Multi-platform content systems (X, LinkedIn, TikTok, YouTube) |
| [`investor-materials`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/investor-materials) | Pitch decks, one-pagers, memos, financial models |
| [`investor-outreach`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/investor-outreach) | Cold emails, warm intros, follow-ups for fundraising |
| [`market-research`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/market-research) | Market sizing, competitor analysis, industry intelligence |

### Workflow & Meta

| Skill | Description |
|-------|-------------|
| [`search-first`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/search-first) | Research-before-coding workflow |
| [`iterative-retrieval`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/iterative-retrieval) | Progressive context retrieval pattern |
| [`continuous-learning`](https://github.com/blader/claude-code-continuous-learning-skill) | Auto-extract patterns from sessions |
| [`continuous-learning-v2`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/continuous-learning-v2) | Instinct-based learning with confidence scoring |
| [`strategic-compact`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/strategic-compact) | Manual context compaction at logical intervals |
| [`content-hash-cache-pattern`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/content-hash-cache-pattern) | SHA-256 content hash caching for expensive file processing |
| [`configure-ecc`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/configure-ecc) | Interactive ECC installer |
| [`project-guidelines-example`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/project-guidelines-example) | Example project-specific skill template |
| [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) | HTML presentations from scratch or PowerPoint conversion |
| [`nutrient-document-processing`](https://github.com/affaan-m/everything-claude-code/tree/main/skills/nutrient-document-processing) | Convert, OCR, redact and extract data from PDFs/Office docs via Nutrient |

---

## Stitch Skills (Google Labs)

> **Source:** [github.com/google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
> **Install:** `npx skills add git@github.com:google-labs-code/stitch-skills.git -y`

Suite oficial do Google Stitch para gerar telas hi-fi, design systems e front-end pronto a partir de prompts de design. Integra-se ao Stitch MCP.

| Skill | Description |
|-------|-------------|
| [`stitch-design`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/stitch-design) | Entry point unificado — enhance prompt, sintetiza `.stitch/DESIGN.md` e gera/edita telas via Stitch MCP |
| [`stitch-loop`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/stitch-loop) | Loop iterativo de design + revisão até atingir qualidade alvo |
| [`enhance-prompt`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/enhance-prompt) | Transforma ideias vagas de UI em prompts polidos e otimizados para Stitch |
| [`design-md`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/design-md) | Analisa projetos Stitch e sintetiza `DESIGN.md` consumível por agentes |
| [`taste-design`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/taste-design) | Semantic Design System — força tipografia, cor calibrada, micro-motion e padrões anti-genéricos |
| [`react-components`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/react-components) | Converte designs Stitch em componentes React modulares |
| [`shadcn-ui`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/shadcn-ui) | Integra e usa shadcn/ui em projetos a partir do design |
| [`remotion`](https://github.com/google-labs-code/stitch-skills/tree/main/skills/remotion) | Gera vídeos walkthrough a partir de designs Stitch via Remotion |

---

## Matt Pocock Skills

> **Source:** [github.com/mattpocock/skills](https://github.com/mattpocock/skills)
> **Author:** [Matt Pocock](https://github.com/mattpocock)
> **Install:** `npx skills add git@github.com:mattpocock/skills.git -y`

Coleção focada em TDD, planning e workflows de issue/PRD para times que vivem no GitHub.

| Skill | Description |
|-------|-------------|
| [`tdd`](https://github.com/mattpocock/skills/tree/main/tdd) | TDD com loop red-green-refactor — usar para features, bug fixes e testes de integração |
| [`grill-me`](https://github.com/mattpocock/skills/tree/main/grill-me) | Entrevista o usuário sem dó até resolver cada ramo da árvore de decisão de um plano |
| [`design-an-interface`](https://github.com/mattpocock/skills/tree/main/design-an-interface) | Gera múltiplos designs de interface radicalmente diferentes via sub-agents paralelos |
| [`request-refactor-plan`](https://github.com/mattpocock/skills/tree/main/request-refactor-plan) | Cria plano detalhado de refactor com commits pequenos via entrevista, e abre como issue |
| [`improve-codebase-architecture`](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture) | Encontra oportunidades de aprofundamento na arquitetura usando `CONTEXT.md` e ADRs |
| [`triage-issue`](https://github.com/mattpocock/skills/tree/main/triage-issue) | Triagem de bug — explora codebase, encontra root cause e cria issue com plano de fix em TDD |
| [`to-prd`](https://github.com/mattpocock/skills/tree/main/to-prd) | Transforma o contexto da conversa atual num PRD e abre como issue no GitHub |
| [`to-issues`](https://github.com/mattpocock/skills/tree/main/to-issues) | Quebra um plano/spec/PRD em issues independentes usando tracer-bullet vertical slices |
| [`migrate-to-shoehorn`](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn) | Migra arquivos de teste de `as` casts para `@total-typescript/shoehorn` |
| [`scaffold-exercises`](https://github.com/mattpocock/skills/tree/main/scaffold-exercises) | Estrutura diretórios de exercícios com seções, problems, solutions e explainers |
| [`edit-article`](https://github.com/mattpocock/skills/tree/main/edit-article) | Edita e aprimora artigos — reestrutura seções, melhora clareza, aperta a prosa |

---

## Huashu Design

> **Source:** [github.com/alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)
> **Install:** `npx skills add git@github.com:alchaincyf/huashu-design.git -y`

| Skill | Description |
|-------|-------------|
| [`huashu-design`](https://github.com/alchaincyf/huashu-design) | 花叔Design — protótipos hi-fi em HTML, demos interativos, slides, animações, exploração de variantes de design e expert review. Inclui workflows de Junior Designer, anti-AI-slop, validação Playwright e exportação de animações HTML para MP4/GIF. |

---

## Community Skills

General-purpose skills without explicit origin metadata. Installed via `~/.claude/skills/` or `~/.agents/skills/`.

### Development

| Skill | Description |
|-------|-------------|
| `fullstack-developer` | React, Node.js, databases, full-stack architecture |
| `python-expert` | Senior Python development — clean, efficient code |
| `frontend-testing` | Vitest + React Testing Library |
| `frontend-code-review` | Frontend file review checklist (`.tsx`, `.ts`, `.js`) |
| `backend-code-review` | Backend file review checklist (`.py`) |
| `code-reviewer` | General code review — security, performance, best practices |
| `component-refactoring` | React component complexity reduction |
| `debugger` | Systematic debugging and root cause analysis |
| `orpc-contract-first` | oRPC contract-first API patterns |

### Platform-Specific

| Skill | Description |
|-------|-------------|
| `liquid-glass-design` | iOS 26 Liquid Glass design system (SwiftUI, UIKit, WidgetKit) |
| `foundation-models-on-device` | Apple FoundationModels framework for on-device LLM (iOS 26+) |
| `feature-flags` | Feature flag states, channel comparison, `@gate` pragmas |
| `flags` | Feature flag debugging across release channels |
| `flow` | Flow type checking for React code |
| `test` | Run tests for React core (source, www, stable, experimental) |
| `fix` | Lint errors, formatting, pre-commit checks |
| `verify` | Validate changes before committing |
| `extract-errors` | Adding new error messages to React |
| `find-skills` | Discover and install new agent skills |

### Research & Analysis

| Skill | Description |
|-------|-------------|
| `academic-researcher` | Literature reviews, paper analysis, scholarly writing |
| `deep-research` | Multi-source research with citations |
| `data-analyst` | SQL, pandas, statistical analysis |
| `fact-checker` | Systematic fact verification |
| `decision-helper` | Structured decision-making frameworks |
| `visualization-expert` | Chart selection and data visualization guidance |

### Writing & Communication

| Skill | Description |
|-------|-------------|
| `technical-writer` | Documentation, API references, guides |
| `editor` | Proofreading — clarity, grammar, style |
| `email-drafter` | Professional email composition |
| `content-creator` | Blog/social media content |
| `meeting-notes` | Structured meeting summaries with action items |

### Business & Strategy

| Skill | Description |
|-------|-------------|
| `strategy-advisor` | Strategic thinking and business decisions |
| `project-planner` | Task breakdowns, timelines, dependencies |
| `sprint-planner` | Agile sprint planning, story estimation |
| `ux-designer` | User research, wireframing, prototyping |
| [`design-advisor`](https://github.com/FelipeOFF/design-advisor-skill) | Industry-specific UI/UX design recommendations with 550+ rules, 50 color palettes, 30+ font pairings |

### Utilities

| Skill | Description |
|-------|-------------|
| `visa-doc-translate` | Translate visa docs to bilingual English PDF |
| [`1password`](https://developer.1password.com/docs/cli/get-started/) | Set up and use the 1Password CLI (`op`) — install, sign in, read/inject/run secrets |
| `context7-mcp` | Heuristics for when to call the Context7 MCP for up-to-date library/framework docs |

---

## Marketing Skills

> **Source:** [github.com/coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
> **Author:** [Corey Haines](https://corey.co)

Coleção de skills voltadas para marketing — CRO, copywriting, SEO, analytics e growth engineering. Todas as skills usam `product-marketing-context` como base compartilhada de posicionamento, audiência e produto.

### SEO & Content

| Skill | Description |
|-------|-------------|
| [`seo-audit`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/seo-audit) | Auditar, revisar ou diagnosticar problemas de SEO no site |
| [`ai-seo`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) | Otimizar conteúdo para AI search engines e citações de LLMs |
| [`site-architecture`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/site-architecture) | Planejar hierarquia de páginas, navegação, URLs e internal linking |
| [`programmatic-seo`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/programmatic-seo) | Criar páginas SEO em escala usando templates e dados |
| [`schema-markup`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/schema-markup) | Adicionar, corrigir ou otimizar schema markup e structured data |
| [`content-strategy`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/content-strategy) | Planejar estratégia de conteúdo e definir tópicos a cobrir |
| [`aso-audit`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/aso-audit) | Auditar ou otimizar listing de App Store / Google Play |

### CRO (Conversion Rate Optimization)

| Skill | Description |
|-------|-------------|
| [`page-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/page-cro) | Otimizar qualquer página de marketing — home, landing, pricing |
| [`signup-flow-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/signup-flow-cro) | Otimizar signup, registration, trial activation |
| [`onboarding-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/onboarding-cro) | Otimizar onboarding pós-signup, ativação e time-to-value |
| [`form-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/form-cro) | Otimizar forms que não sejam signup — lead capture, contato, checkout |
| [`popup-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/popup-cro) | Criar/otimizar popups, modais, overlays, slide-ins e banners |
| [`paywall-upgrade-cro`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paywall-upgrade-cro) | Criar/otimizar paywalls, upgrade screens, upsell modals |

### Content & Copy

| Skill | Description |
|-------|-------------|
| [`copywriting`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) | Escrever ou reescrever copy de marketing para qualquer página |
| [`copy-editing`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing) | Editar, revisar ou melhorar copy de marketing existente |
| [`cold-email`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cold-email) | Escrever cold emails B2B e sequências de follow-up |
| [`email-sequence`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/email-sequence) | Criar ou otimizar drip campaigns e email flows de lifecycle |
| [`social-content`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social-content) | Criar, agendar e otimizar conteúdo social (LinkedIn, X, Instagram) |

### Paid & Measurement

| Skill | Description |
|-------|-------------|
| [`paid-ads`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/paid-ads) | Campanhas pagas em Google Ads, Meta, LinkedIn, X |
| [`ad-creative`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ad-creative) | Gerar, iterar ou escalar ad creative — headlines, copy, frames |
| [`ab-test-setup`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ab-test-setup) | Planejar, desenhar e implementar A/B tests e programas de experimentação |
| [`analytics-tracking`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/analytics-tracking) | Configurar, melhorar ou auditar analytics e measurement |

### Growth & Retention

| Skill | Description |
|-------|-------------|
| [`referral-program`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/referral-program) | Criar, otimizar ou analisar programas de referral e affiliate |
| [`free-tool-strategy`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/free-tool-strategy) | Planejar free tools para lead gen, SEO e distribuição |
| [`churn-prevention`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/churn-prevention) | Reduzir churn, cancellation flows, save offers, recuperação de payment |
| [`community-marketing`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/community-marketing) | Construir e alavancar comunidades online para growth |
| [`lead-magnets`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/lead-magnets) | Criar, planejar e otimizar lead magnets para email capture |

### Sales & GTM

| Skill | Description |
|-------|-------------|
| [`revops`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/revops) | Revenue operations, lead lifecycle, handoff marketing↔sales |
| [`sales-enablement`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/sales-enablement) | Sales collateral — pitch decks, one-pagers, objection handling |
| [`launch-strategy`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/launch-strategy) | Planejar product launches e feature announcements |
| [`pricing-strategy`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/pricing-strategy) | Decisões de pricing, packaging e monetization |
| [`competitor-alternatives`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-alternatives) | Páginas de comparação e alternativas para SEO e sales |
| [`competitor-profiling`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-profiling) | Pesquisar, perfilar e analisar competidores a partir de URLs |
| [`directory-submissions`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/directory-submissions) | Submeter produto em diretórios (startup, SaaS, AI, MCP, review sites) |

### Strategy & Research

| Skill | Description |
|-------|-------------|
| [`product-marketing-context`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/product-marketing-context) | Documento base de contexto de produto — lido por todas as outras skills |
| [`marketing-ideas`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-ideas) | Brainstorm de ideias e estratégias de marketing para SaaS |
| [`marketing-psychology`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-psychology) | Aplicar princípios psicológicos e behavioral science ao marketing |
| [`customer-research`](https://github.com/coreyhaines31/marketingskills/tree/main/skills/customer-research) | Conduzir, analisar e sintetizar customer research |

---

## Custom Skills

Skills created specifically for my workflow.

| Skill | Description | Repo |
|-------|-------------|------|
| [`frontend-project-style`](https://github.com/FelipeOFF/frontend-project-style-skill) | Configurable design system and style guide for frontend projects. Auto-generates `PROJECT_STYLE.md` with your design tokens on first use. | [FelipeOFF/frontend-project-style-skill](https://github.com/FelipeOFF/frontend-project-style-skill) |
| [`design-advisor`](https://github.com/FelipeOFF/design-advisor-skill) | Industry-specific UI/UX design recommendations with 550+ rules, 50 color palettes, 30+ font pairings, and real component examples. | [FelipeOFF/design-advisor-skill](https://github.com/FelipeOFF/design-advisor-skill) |
| [`obscura`](https://github.com/FelipeOFF/obscura-skill) | Teaches Claude how to use [Obscura](https://github.com/h4ckf0r0day/obscura) — the Rust-based headless browser (~30 MB) for web scraping and AI agents, with Puppeteer/Playwright over CDP and built-in stealth. | [FelipeOFF/obscura-skill](https://github.com/FelipeOFF/obscura-skill) |
| [`sleepwell`](https://github.com/FelipeOFF/sleepwell) | Native Claude Code plugin for autonomous overnight loops. Disciplined iteration (isolated branch, atomic commit per iter, automatic rollback) plus adaptive behavior (5 modes including experimental `wave`, optional voice matching, cross-run meta-learning, token/cost telemetry with Claude/Codex detection). Runs **inside** the CC session — keeps prompt cache warm and MCPs alive. Language- and stack-agnostic. | [FelipeOFF/sleepwell](https://github.com/FelipeOFF/sleepwell) |

---

## Personal Rules, Commands & Agents

The `rules/`, `commands/`, and `agents/` directories in this repo are **reusable templates** you can drop into `~/.claude/` to enforce consistent git workflows, commit formats, branch naming, and PR discipline across every project.

They are designed to be **project-agnostic**: they use `PROJ-123` as a placeholder for your Jira prefix, and assume nothing about your language stack or editor.

### What's in the box

| Path | Purpose |
|---|---|
| [`rules/commits.md`](./rules/commits.md) | Conventional Commits + Jira format (`<type>(<JIRA>): <title>` + detailed body) |
| [`rules/branches.md`](./rules/branches.md) | Branch naming (`<type>/<JIRA>/<slug>`) with validation regex |
| [`rules/workflow.md`](./rules/workflow.md) | Git hygiene, worktrees, checkpointing, verification-before-done |
| [`rules/language.md`](./rules/language.md) | Template for pinning a non-English default response language |
| [`rules/context7.md`](./rules/context7.md) | When to use the Context7 MCP for live library / framework / SDK docs |
| [`commands/commit.md`](./commands/commit.md) | `/commit` — drafts a commit, extracts Jira from branch, requires approval |
| [`commands/branch.md`](./commands/branch.md) | `/branch` — creates a validated branch from loose args |
| [`commands/pr.md`](./commands/pr.md) | `/pr` — opens PR via `gh` with structured Summary/Changes/Test plan |
| [`commands/review.md`](./commands/review.md) | `/review` — runs lint + type-check + tests for the detected stack |
| [`commands/wt.md`](./commands/wt.md) | `/wt` — creates a `git worktree` for isolated parallel work |
| [`agents/commit-crafter.md`](./agents/commit-crafter.md) | Subagent that builds Conventional Commits + Jira messages |
| [`agents/pr-writer.md`](./agents/pr-writer.md) | Subagent that writes structured PR bodies from `git diff` |
| [`agents/jira-linker.md`](./agents/jira-linker.md) | Lightweight subagent that detects Jira codes from branch/commit/prompt |

### How to install

```bash
# Clone or copy just the folders you want
git clone https://github.com/FelipeOFF/my-claude-code-skills.git /tmp/mccs
mkdir -p ~/.claude/rules ~/.claude/commands ~/.claude/agents
cp /tmp/mccs/rules/*.md    ~/.claude/rules/
cp /tmp/mccs/commands/*.md ~/.claude/commands/
cp /tmp/mccs/agents/*.md   ~/.claude/agents/
```

Then reference the rules from your `~/.claude/CLAUDE.md`:

```markdown
@~/.claude/rules/commits.md
@~/.claude/rules/branches.md
@~/.claude/rules/workflow.md
```

### Customizing

- **Jira prefix**: search-replace `PROJ-` in `rules/commits.md`, `rules/branches.md` and the agents with your org prefix (e.g., `ENG-`, `API-`).
- **Language**: edit `rules/language.md` and rename it to reflect your preferred language.
- **Allowed types**: `rules/commits.md` ships with the full Conventional Commits set — trim it if your org uses a smaller vocabulary.

### Why rules + commands + agents together?

- **Rules** are static constraints loaded into every session (single source of truth).
- **Commands** (`/commit`, `/pr`, ...) give you muscle-memory triggers for the workflows that enforce the rules.
- **Agents** give those workflows isolated context windows so they don't pollute your main conversation.

This mirrors the Command → Agent → Skill orchestration pattern popularized by [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice).

---

## ByteRover

> **Source:** [github.com/trietdeptrai/Byterover-Claude-Codex-Collaboration-](https://github.com/trietdeptrai/Byterover-Claude-Codex-Collaboration-)
> **Installed in:** `~/.claude/skills/byterover/`

| Skill | Description |
|-------|-------------|
| `byterover` | Knowledge management for AI agents. Uses `brv` CLI to store and retrieve project patterns, decisions, and architectural rules in `.brv/context-tree`. |

---

## Installation Guide

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed and authenticated
- Node.js 18+ and npm
- Git

### Step-by-Step

```bash
# 1. Install GSD
npx -y get-shit-done-cc@latest --global

# 2. Install Obsidian Skills
npx skills add git@github.com:kepano/obsidian-skills.git -y

# 3. Install UI/UX Pro Max
npm install -g uipro-cli
uipro init --ai claude

# 4. Install Frontend Project Style
npx skills add git@github.com:FelipeOFF/frontend-project-style-skill.git

# 5. Install Design Advisor
npx skills add git@github.com:FelipeOFF/design-advisor-skill.git

# 6. Install Stitch / Matt Pocock / Huashu skill collections
npx skills add git@github.com:google-labs-code/stitch-skills.git -y
npx skills add git@github.com:mattpocock/skills.git -y
npx skills add git@github.com:alchaincyf/huashu-design.git -y

# 7. Install Obscura skill (web scraping & E2E with Rust headless browser)
npx skills add git@github.com:FelipeOFF/obscura-skill.git -y
```

Then inside Claude Code:

```
# 6. Install marketplace plugins
/plugin marketplace add superpowers
/plugin install superpowers@superpowers

/plugin marketplace add claude-plugins-official
/plugin install frontend-design
/plugin install agent-sdk-dev
/plugin install stripe

/plugin marketplace add thedotmack
/plugin install claude-mem

/plugin marketplace add firebase
/plugin install firebase

/plugin marketplace add openai-codex
/plugin install codex@openai-codex

/plugin marketplace add nowork-studio/toprank
/plugin install toprank

/plugin install claude-code-setup@claude-plugins-official
```

### Verify Installation

```bash
# Check skills directory
ls ~/.claude/skills/

# Check plugins
ls ~/.claude/plugins/cache/

# Check GSD version
cat ~/.claude/get-shit-done/VERSION
```

---

## License

MIT — Feel free to use this list as a starting point for your own Claude Code setup.

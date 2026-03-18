# My Claude Code Skills

A curated collection of **130+ skills** installed in my Claude Code setup. This list is meant to help teammates and collaborators quickly replicate the same environment.

> **What are skills?** Skills are reusable prompt modules that teach Claude Code how to approach specific tasks — from debugging to design systems to deployment. They live in `~/.claude/skills/` or are installed via plugins and marketplaces.

---

## Table of Contents

- [Quick Setup](#quick-setup)
- [Plugins & Marketplaces](#plugins--marketplaces)
- [GSD — Get Shit Done](#gsd--get-shit-done)
- [Obsidian Skills](#obsidian-skills)
- [UI/UX Pro Max](#uiux-pro-max)
- [21st.dev — Magic MCP](#21stdev--magic-mcp)
- [ECC — Everything Claude Code](#ecc--everything-claude-code)
- [Community Skills](#community-skills)
- [Custom Skills](#custom-skills)
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

### Firebase

> **Source:** Google/Firebase Marketplace

Full Firebase toolset: Auth, Firestore, Realtime Database, Storage, Remote Config, Messaging, and project management.

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

---

## Custom Skills

Skills created specifically for my workflow.

| Skill | Description | Repo |
|-------|-------------|------|
| [`frontend-project-style`](https://github.com/FelipeOFF/frontend-project-style-skill) | Configurable design system and style guide for frontend projects. Auto-generates `PROJECT_STYLE.md` with your design tokens on first use. | [FelipeOFF/frontend-project-style-skill](https://github.com/FelipeOFF/frontend-project-style-skill) |
| [`design-advisor`](https://github.com/FelipeOFF/design-advisor-skill) | Industry-specific UI/UX design recommendations with 550+ rules, 50 color palettes, 30+ font pairings, and real component examples. | [FelipeOFF/design-advisor-skill](https://github.com/FelipeOFF/design-advisor-skill) |

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

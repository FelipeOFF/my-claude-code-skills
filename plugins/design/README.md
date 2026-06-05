# Package: design

Curated skills for visual design, UI/UX, design systems, and taste.

> **Why this package?** LLMs default to generic UI outputs (centered
> hero, blue CTA, lorem ipsum). Every skill here pushes back against
> that — opinionated rules, calibrated palettes, hi-fi prototyping
> tools, and image-generation workflows that produce non-generic results.

## Plugin dependencies (auto-installed)

| Plugin @ Marketplace | Why it's curated |
|---|---|
| `frontend-design` @ `claude-plugins-official` | Production-grade frontend interfaces with high taste; overrides generic LLM defaults for component code. |

## MCP servers (auto-configured)

| MCP | Command | Required env | Why it's curated |
|---|---|---|---|
| `magic` | `npx -y @21st-dev/magic@latest` | `TWENTYFIRST_API_KEY` | Generates production-ready React components from natural language; curated component library and refinement loop. |

> Personal credentials live in your env vars — never committed here.
> Set `TWENTYFIRST_API_KEY` in your shell rc before using.

## Vendored skills (real content in the repo)

Available immediately after `/plugin install design@myskills` — no setup step.

| Skill | Source | Why it's curated |
|---|---|---|
| `stitch-design`, `stitch-loop`, `taste-design`, `design-md`, `enhance-prompt`, `react-components`, `remotion`, `shadcn-ui` | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) (`vendored`) | Google Stitch toolkit: hi-fi screen generation, semantic `DESIGN.md`, iterative loop, prompt enhancement, React/Remotion/shadcn builders. |
| `huashu-design` | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) (`vendored`) | HTML hi-fi prototypes, animations, design variant exploration with Junior Designer workflow + anti-AI-slop checklist. Ships its `references/` + `scripts/` (heavy BGM/showcase media omitted — see `assets/OMITTED-MEDIA.md`). |
| `frontend-project-style` | [FelipeOFF/frontend-project-style-skill](https://github.com/FelipeOFF/frontend-project-style-skill) (`vendored`) | Auto-generates `PROJECT_STYLE.md` with design tokens on first use; per-project style guide that the LLM actually reads. |

## Optional external setup (run `/design-setup`)

Skills that can't be vendored (FelipeOFF repo + npm global binary):

| Skill | Source | Why it's curated |
|---|---|---|
| `design-advisor` | [FelipeOFF/design-advisor-skill](https://github.com/FelipeOFF/design-advisor-skill) | 550+ industry-specific UX rules, 50 color palettes, 30+ font pairings; structured advice instead of vibes. |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (`uipro-cli`) | 67 UI styles, 96 palettes, 161 industry-specific reasoning rules, 13 stacks; lookup-driven design intelligence. |

> `design-an-interface` (mattpocock) stays available on demand but isn't
> vendored — `npx skills add git@github.com:mattpocock/skills.git -y`.

## Local-only skills (no public source mapped)

Documented as part of the author's curation. They live in
`~/.claude/skills/` when imported manually. Each pushes against a
specific LLM default:

- `design-taste-frontend` — Senior UI/UX engineer persona; metric-based rules, strict component architecture, hardware-accel CSS.
- `extract-design-system` — pulls primitives from a public website into starter token files.
- `high-end-visual-design` — agency-level rules: exact fonts, spacing, shadows, card structures, animations that make sites feel expensive.
- `imagegen-frontend-mobile` — mobile app image generation with phone-mockup framing, multi-screen consistency.
- `imagegen-frontend-web` — landing page image direction: one horizontal image **per section**, varied composition, no compressed boards.
- `industrial-brutalist-ui` — style pack: Swiss typographic + military terminal, rigid grids, analog degradation.
- `liquid-glass-design` — iOS 26 Liquid Glass system (SwiftUI/UIKit/WidgetKit) with morphing/blur primitives.
- `minimalist-ui` — clean editorial palette, warm monochrome, flat bento grids — no gradients, no heavy shadows.
- `stitch-design-taste` — semantic design system for Stitch generating agent-friendly `DESIGN.md` enforcing strict typography, calibrated color, perpetual micro-motion.

## How to install

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install design@myskills
/design-setup   # optional — installs only design-advisor + ui-ux-pro-max (external)
```

## How to remove

```bash
/plugin uninstall design@myskills
```

> Cross-marketplace dependencies are **not** auto-removed —
> they may be in use by other installed packages.

---

## 🇧🇷 Resumo em PT-BR

Package `design` = curadoria de UI/UX para fugir dos defaults genéricos
de LLM. Inclui o plugin `frontend-design` (cross-marketplace, auto-instalado)
e o MCP da 21st.dev Magic (gera React components — precisa de
`TWENTYFIRST_API_KEY` pessoal).

**Vendorizadas** (conteúdo real no repo, prontas no install): o bundle
Stitch da Google Labs (`stitch-design`, `stitch-loop`, `taste-design`,
`design-md`, `enhance-prompt`, `react-components`, `remotion`, `shadcn-ui`),
o `huashu-design` (protótipos HTML com workflow anti-AI-slop) e a autoral
`frontend-project-style`.

Via `/design-setup` (opcional) entram só as externas: `design-advisor`
(550+ regras de UX, autoral do Felipe) e `ui-ux-pro-max` (design
intelligence por lookup — 67 estilos, 96 paletas, via `uipro-cli`). O
`design-an-interface` da Matt Pocock fica disponível sob demanda.

As skills locais (sem repo público) cobrem style packs (industrial-brutalist,
minimalist, liquid-glass), image generation (mobile + web), e regras
de taste de agência high-end. Cada uma override um default específico
do LLM — não estão aqui pra encher catálogo, estão pra resolver problemas
que o autor sentiu na pele em projetos reais.

# Package: marketing

Curated skills for digital marketing — SEO, CRO, paid traffic, email, social.

> **Why this package?** Light curation for now. The author kept only
> SEO-focused tools that survived the cleanup. CRO/paid/email skills
> from the original catalog were quarantined — none earned a permanent
> slot under the "actually used" filter.

## Plugin dependencies (auto-installed)

| Plugin @ Marketplace | Why it's curated |
|---|---|
| `toprank` @ `nowork-studio` | SEO ranking analysis and marketing toolkit for keyword tracking and SERP intelligence. |

## MCP servers (auto-configured)

_None yet._

## Standalone setup (run `/marketing-setup`)

Skill instalada individualmente via `npx skills add --skill <name>` —
pulls just the skill, not the parent bundle.

| Skill | Source | Why it's curated |
|---|---|---|
| `seo` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/seo) | Technical SEO audit: on-page checks, structured data validation, Core Web Vitals review, sitemap/robots inspection. |

## How to install

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install marketing@myskills
```

## How to remove

```bash
/plugin uninstall marketing@myskills
```

---

## 🇧🇷 Resumo em PT-BR

Package `marketing` = SEO essencial. Inclui o plugin `toprank` da
nowork-studio (análise de ranking SEO e ferramentas de marketing)
como dependência cross-marketplace, e a skill `seo` (auditoria
técnica) instalada standalone via `/marketing-setup` direto do repo
`affaan-m/everything-claude-code` — sem dependência do bundle inteiro.

CRO, paid traffic, email e social do catálogo antigo foram pra
quarentena no cleanup — não ficaram porque o autor não usa ativamente.
A lista pode crescer quando uma skill nova passar no filtro.

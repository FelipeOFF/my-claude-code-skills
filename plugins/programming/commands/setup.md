---
name: programming-setup
description: Instala skills standalone do package programming (3rd-party fora de marketplaces)
---

# /programming-setup

Execute os comandos abaixo via Bash em ordem. Após cada bloco, confirme com `/find-skills`.

## 1. Matt Pocock skills (TDD + workflow)

Bundle inclui `tdd`, `to-prd`, `design-an-interface` (este último é do package design — vem junto).

```bash
npx skills add git@github.com:mattpocock/skills.git -y
```

## 2. Obscura (scraping/E2E com headless browser Rust)

```bash
npx skills add git@github.com:FelipeOFF/obscura-skill.git -y
```

## 3. Render Plans to HTML (autoral do Felipe)

Renderiza artifacts de planejamento (PLAN.md, REVIEW.md, REQUIREMENTS.md, tasks.md, etc.) como dashboard HTML self-contained com sidebar nav, status pills, mermaid e syntax highlighting.

```bash
npx skills add git@github.com:FelipeOFF/render-plans-to-html.git -y
```

---

> Skills locais sem fonte pública (`backend-code-review`, `frontend-code-review`, `code-reviewer`, `debugger`, `defuddle`, `frontend-testing`, `fuzzing-dictionary`, `fuzzing-obstacles`, `property-based-testing`, `context7-mcp`) ficam documentadas no README — são bundles do harness do Felipe sem distribuição pública mapeada.

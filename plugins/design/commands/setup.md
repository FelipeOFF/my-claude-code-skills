---
name: design-setup
description: Instala as poucas skills externas do package design (não-vendorizáveis)
---

# /design-setup

As skills Stitch (`stitch-design`, `stitch-loop`, `taste-design`, `design-md`,
`enhance-prompt`, `react-components`, `remotion`, `shadcn-ui`), `huashu-design`
e `frontend-project-style` agora são **vendorizadas** — conteúdo real no repo,
prontas após `/plugin install design@myskills`. Este comando instala só o que
não dá pra vendorizar.

## 1. Design Advisor (autoral do Felipe)

550+ regras de UX por indústria, 50 paletas, 30+ pares de fonte.

```bash
npx skills add git@github.com:FelipeOFF/design-advisor-skill.git -y
```

## 2. UI/UX Pro Max (binário npm global)

```bash
npm install -g uipro-cli
uipro init --ai claude
```

---

> `design-an-interface` (Matt Pocock) não é vendorizada; instale sob demanda com
> `npx skills add git@github.com:mattpocock/skills.git -y` se precisar gerar N
> designs paralelos.
>
> Skills locais sem fonte pública (`design-taste-frontend`, `extract-design-system`,
> `high-end-visual-design`, `imagegen-frontend-mobile`, `imagegen-frontend-web`,
> `industrial-brutalist-ui`, `liquid-glass-design`, `minimalist-ui`,
> `stitch-design-taste`) ficam documentadas no README do package.
>
> Caso uma fonte standalone fique indisponível, abra issue em `FelipeOFF/my-claude-code-skills`.

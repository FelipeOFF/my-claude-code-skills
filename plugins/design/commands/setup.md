---
name: design-setup
description: Instala skills standalone do package design (3rd-party fora de marketplaces)
---

# /design-setup

Execute os comandos abaixo via Bash em ordem. Após cada bloco, confirme com `/find-skills` que as skills apareceram.

## 1. Frontend Project Style (autoral do Felipe)

```bash
npx skills add git@github.com:FelipeOFF/frontend-project-style-skill.git -y
```

## 1b. Design Advisor (autoral do Felipe)

```bash
npx skills add git@github.com:FelipeOFF/design-advisor-skill.git -y
```

## 2. Stitch bundle (Google Labs)

Inclui `stitch-design`, `stitch-loop`, `taste-design`, `design-md`, `enhance-prompt` e outras.

```bash
npx skills add git@github.com:google-labs-code/stitch-skills.git -y
```

## 3. Huashu Design (alchaincyf)

```bash
npx skills add git@github.com:alchaincyf/huashu-design.git -y
```

## 4. Matt Pocock skills (cross-package)

Bundle inclui `design-an-interface` (design) + `tdd` e `to-prd` (programming). Quem instala apenas `design@myskills` ainda assim recebe `tdd`/`to-prd` no harness — é como o repo é distribuído.

```bash
npx skills add git@github.com:mattpocock/skills.git -y
```

## 5. UI/UX Pro Max

```bash
npm install -g uipro-cli
uipro init --ai claude
```

---

> Skills locais sem fonte pública (`design-taste-frontend`, `extract-design-system`, `high-end-visual-design`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `industrial-brutalist-ui`, `liquid-glass-design`, `minimalist-ui`, `stitch-design-taste`) não são instaladas por este comando — ficam documentadas no README do package.

> Caso uma fonte standalone fique indisponível, abra issue em `FelipeOFF/my-claude-code-skills`.

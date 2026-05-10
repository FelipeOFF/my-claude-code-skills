---
name: workflow-setup
description: Instala skills standalone do package workflow (3rd-party fora de marketplaces)
---

# /workflow-setup

Execute via Bash. Confirme com `/find-skills gsd` ao final.

## 1. GSD — Get Shit Done (bundle de 64 skills de gerenciamento de fases)

```bash
npx skills add git@github.com:glittercowboy/get-shit-done.git -y
```

Inclui toda a família `gsd-*` (planejamento, execução, verificação, debug,
review, milestones, workstreams, etc.).

## 2. find-skills (Vercel Labs)

Skill que ensina como descobrir e instalar outras skills via `npx skills find/add`.

```bash
npx skills add github:vercel-labs/skills --skill find-skills
```

## 3. 1password (OpenClaw)

Set up e uso do 1Password CLI (`op`) — install, signin, ler/injetar/run secrets.

```bash
npx skills add github:openclaw/openclaw --skill 1password
```

---

> Os demais workflow tools (superpowers, claude-mem, octo, codex,
> ralph-specum, sleepwell, agentmemory) vêm como **plugin deps**
> automáticas — não precisa rodar nada além de `/plugin install workflow@myskills`.

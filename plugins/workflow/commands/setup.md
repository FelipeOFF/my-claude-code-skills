---
name: workflow-setup
description: Instala skills standalone do package workflow (3rd-party fora de marketplaces)
---

# /workflow-setup

> **Fallback manual / re-execução.** A instalação destas skills roda automaticamente
> no primeiro `SessionStart` após `/plugin install workflow@myskills`
> (ver `scripts/bootstrap.sh`). Use este comando para forçar re-instalação,
> debugar bootstrap quebrado, ou rodar sem depender do marker.

Execute via Bash. Confirme com `/find-skills gsd` ao final.

> `find-skills` (Vercel Labs) agora é **vendorizada** (conteúdo real no repo) —
> não precisa mais ser instalada aqui.

## 1. GSD — Get Shit Done (bundle de 64 skills de gerenciamento de fases)

```bash
npx skills add git@github.com:glittercowboy/get-shit-done.git -y
```

Inclui toda a família `gsd-*` (planejamento, execução, verificação, debug,
review, milestones, workstreams, etc.).

## 2. 1password (OpenClaw)

Set up e uso do 1Password CLI (`op`) — install, signin, ler/injetar/run secrets.

```bash
npx skills add github:openclaw/openclaw --skill 1password
```

---

> Os demais workflow tools (superpowers, claude-mem, octo, codex,
> ralph-specum, sleepwell) vêm como **plugin deps** automáticas — não
> precisa rodar nada além de `/plugin install workflow@myskills`.

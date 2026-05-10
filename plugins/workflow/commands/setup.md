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

---

> Os demais workflow tools (superpowers, claude-mem, octo, codex,
> ralph-specum, sleepwell, agentmemory) vêm como **plugin deps**
> automáticas — não precisa rodar nada além de `/plugin install workflow@myskills`.

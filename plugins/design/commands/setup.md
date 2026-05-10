---
name: design-setup
description: Instala skills standalone do package design (3rd-party fora de marketplaces)
---

# /design-setup

Execute os passos abaixo via Bash, um por vez, e confirme cada install com `/find-skills`.

1. **frontend-project-style** (skill autoral pública do Felipe):
   ```bash
   npx skills add git@github.com:FelipeOFF/frontend-project-style-skill.git -y
   ```

Após cada install, rode `/find-skills frontend-project-style` (ou termo equivalente) para confirmar que a skill foi reconhecida pelo harness.

> Caso uma fonte standalone fique indisponível, abra issue em
> `FelipeOFF/my-claude-code-skills` para atualizar este setup.

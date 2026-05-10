# Package: design

Curadoria de skills focadas em design visual, UI/UX, design system e taste.

## Dependências de plugins (auto-instaladas)

- `frontend-design` @ `claude-plugins-official` — interfaces frontend production-grade com taste alto, override de defaults genéricos do LLM.

## Setup adicional (3rd-party standalone)

Rode `/design-setup` para instalar:

| Skill | Fonte |
|---|---|
| `frontend-project-style` | [FelipeOFF/frontend-project-style-skill](https://github.com/FelipeOFF/frontend-project-style-skill) |
| `stitch-design`, `stitch-loop`, `taste-design`, `design-md`, `enhance-prompt` | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |
| `huashu-design` | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) |
| `design-an-interface` | [mattpocock/skills](https://github.com/mattpocock/skills) |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (via `uipro-cli`) |

## Skills locais (sem fonte pública mapeada)

Documentadas como parte da curadoria do autor. Ficam em `~/.claude/skills/` quando o usuário as importa manualmente.

- `design-taste-frontend` — Senior UI/UX Engineer; sobrescreve vieses default do LLM com regras métricas.
- `extract-design-system` — extrai primitivas de design de um site público em token files.
- `high-end-visual-design` — ensina a IA a desenhar como agência high-end.
- `imagegen-frontend-mobile` — direção de imagem mobile premium.
- `imagegen-frontend-web` — direção de imagem frontend para web (uma imagem por seção).
- `industrial-brutalist-ui` — interfaces mecânicas raw, Swiss + military terminal.
- `liquid-glass-design` — iOS 26 Liquid Glass design system.
- `minimalist-ui` — interfaces clean editorial, paleta warm monochrome.
- `stitch-design-taste` — semantic design system para Stitch, gera DESIGN.md agent-friendly.

## Como instalar

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install design@myskills
/design-setup   # opcional, instala standalone 3rd-party
```

## Como remover

```bash
/plugin uninstall design@myskills
```

> Dependencies cross-marketplace **não** são removidas automaticamente —
> podem estar em uso por outros packages instalados.

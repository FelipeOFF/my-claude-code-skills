# Package: design

Curadoria de skills focadas em design visual, UI/UX, design system e taste.

## Skills autorais incluídas

_Nenhuma na v0.1. Skills autorais entrarão conforme demanda em PRs subsequentes._

## Dependências de plugins (auto-instaladas)

- `huashu-design` @ `superpowers-marketplace` — protótipos hi-fi em HTML, animações, exploração de variantes.
- `frontend-design` @ `superpowers-marketplace` — interfaces frontend production-grade com taste alto.

## Setup adicional (3rd-party standalone)

Rode `/design-setup` para instalar:

- `frontend-project-style` — fonte: `github.com/FelipeOFF/frontend-project-style-skill`

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

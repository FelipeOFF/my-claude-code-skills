# Package: workflow

Meta-workflow: planejamento de fases, memória persistente, loops autônomos,
debugging multi-sessão, multi-agent orchestration.

## Dependências de plugins (auto-instaladas)

- `superpowers` @ `superpowers-marketplace` — brainstorming, writing-plans, executing-plans, TDD, debugging sistemático.
- `claude-mem` @ `thedotmack` — memória persistente cross-session, smart-explore, knowledge agent.
- `agentmemory` @ `agentmemory` — recall/remember/forget para contexto longo.
- `octo` @ `nyldn-plugins` — orchestration (claude-octopus): personas, providers, multi-flow.
- `codex` @ `openai-codex` — runtime para delegar investigação ao Codex CLI.
- `ralph-specum` @ `smart-ralph` — spec workflow (research → requirements → design → tasks → implement).
- `sleepwell` @ `sleepwell` — autonomous overnight loop com discipline + meta-learning.

## Setup adicional (3rd-party standalone)

Rode `/workflow-setup` para instalar:

| Bundle | Fonte | Skills incluídas |
|---|---|---|
| GSD — Get Shit Done | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | 64 skills `gsd-*` (planejamento, execução, verificação, milestones, workstreams) |

## Como instalar

```bash
/plugin marketplace add FelipeOFF/my-claude-code-skills
/plugin install workflow@myskills
/workflow-setup   # instala bundle GSD via npx
```

## Como remover

```bash
/plugin uninstall workflow@myskills
```

> Dependencies cross-marketplace **não** são removidas automaticamente —
> podem estar em uso por outros packages instalados.

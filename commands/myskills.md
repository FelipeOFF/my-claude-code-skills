---
description: Manager do marketplace pessoal myskills — status de instalação por package, guia de install, e procedimento para adicionar novas skills. Use ao querer saber o que está instalado, instalar um package, ou adicionar uma skill nova.
argument-hint: "[status | install <package> | add <descrição>]"
---

Você é o manager do marketplace pessoal `myskills` de Felipe.
Repo: `~/Projects/my-claude-code-skills`
Constituição: `~/Projects/my-claude-code-skills/docs/CONSTITUTION.md`

## Ação com base nos argumentos

```
$ARGUMENTS
```

Se vazio ou "status" → executar **FLUXO STATUS**.
Se começa com "install" → executar **FLUXO INSTALL**.
Se começa com "add" → executar **FLUXO ADD**.
Se começa com "sync" → executar **FLUXO SYNC**.

---

## FLUXO STATUS

Gerar relatório de instalação do marketplace. Executar em paralelo:

### 1. Checar se o marketplace está registrado
```bash
cat ~/.claude/settings.json | python3 -c "import sys,json; d=json.load(sys.stdin); ms=d.get('extraKnownMarketplaces',{}); print('REGISTRADO' if 'myskills' in ms else 'NÃO REGISTRADO')"
```

### 2. Checar packages instalados (enabledPlugins)
```bash
cat ~/.claude/settings.json | python3 -c "
import sys, json
d = json.load(sys.stdin)
ep = d.get('enabledPlugins', {})
packages = ['design', 'copy', 'marketing', 'programming', 'workflow']
for p in packages:
    key = f'{p}@myskills'
    status = 'INSTALADO' if ep.get(key) else 'não instalado'
    print(f'{p}: {status}')
"
```

### 3. Checar skills standalone instaladas
```bash
# Skills standalone vão para ~/.claude/skills/ (via npx skills add) ou ~/.claude/skills.disabled/
ls ~/.claude/skills/ 2>/dev/null | sort
echo "---disabled---"
ls ~/.claude/skills.disabled/ 2>/dev/null | sort
```

### 4. Checar MCPs myskills-related
```bash
claude mcp list 2>/dev/null | grep -iE "magic|chrome-devtools|react-grab|hostinger|toprank" || echo "(nenhum MCP myskills ativo)"
```

### Apresentar resultado

Montar tabela PT-BR com status por package:

| Package | Plugin | Standalone skills | MCPs |
|---|---|---|---|
| design | ✅/❌ | lista das encontradas | ✅/❌ |
| copy | ✅/❌ | - | - |
| marketing | ✅/❌ | lista | ✅/❌ |
| programming | ✅/❌ | lista | ✅/❌ |
| workflow | ✅/❌ | lista | - |

Depois mostrar: **O que falta instalar** com os comandos exatos.

Packages não instalados → mostrar: `/myskills install <package>`
MCPs faltando → mostrar: `claude mcp add ...` ou `TWENTYFIRST_API_KEY` env var
Standalone faltando → mostrar: `/<package>-setup`

---

## FLUXO INSTALL

Argumento: `install <package>` onde package é design | copy | marketing | programming | workflow.

1. Confirmar que o marketplace está registrado:
   - Se não: `claude plugin marketplace add FelipeOFF/my-claude-code-skills`
   
2. Instalar o package:
   - Orientar o usuário a rodar: `/plugin install <package>@myskills`
   - Explicar que isso instala as dependências de plugins automaticamente.

3. Rodar o setup standalone:
   - Verificar se existe `~/.claude/commands/<package>-setup.md`
   - Se sim, orientar: `/<package>-setup` para instalar as skills 3rd-party.

4. Checar MCPs necessários (ler README do package):
   - Mostrar variáveis de env necessárias e como configurar.

5. Confirmar com status parcial.

---

## FLUXO ADD

Argumento: `add <descrição da skill ou URL>` — adiciona uma skill nova ao repo seguindo a Constituição.

### Passo 1 — Entender a skill
Perguntar ao usuário (se não ficou claro pelo argumento):
- O que a skill faz? (uma frase)
- É autoral, dependency de marketplace, ou standalone (URL/npx)?
- Em qual package vai? (design / copy / marketing / programming / workflow)

### Passo 2 — Classificar (Regra A)
Ler `~/Projects/my-claude-code-skills/docs/CONSTITUTION.md` para decidir package se ambíguo.

### Passo 3 — Aplicar conforme origem

**Se `source: authored`** (conteúdo no repo):
```
Criar ~/Projects/my-claude-code-skills/plugins/<pkg>/skills/<nome>/SKILL.md
```
Frontmatter obrigatório (Regra C):
```yaml
---
name: <nome>
description: |
  Use quando ... Triggers em "X", "Y", "Z".
  NÃO use para: ...
source: authored
upstream: null
license: MIT
added: YYYY-MM-DD
---
```

**Se `source: dependency`** (vem via marketplace):
- Criar stub SKILL.md igual ao `ruflo` (explicando que a real vem via dep).
- Adicionar a dep em `plugins/<pkg>/.claude-plugin/plugin.json`.

**Se `source: standalone-setup`** (npx/git, via setup command):
- Criar stub SKILL.md documentando origem.
- Adicionar linha em `plugins/<pkg>/commands/setup.md`.

### Passo 4 — Atualizar README do package
Abrir `~/Projects/my-claude-code-skills/plugins/<pkg>/README.md` e adicionar entrada na tabela correta (Regra D).

### Passo 5 — Commit
Seguir regra de commits do Felipe:
```
feat(<pkg>): Adiciona skill <nome>

<corpo PT-BR explicando por que a skill foi adicionada e o que ela faz>
```

---

## FLUXO SYNC

Sincronizar o repo local com o GitHub e resolver diferenças.

```bash
cd ~/Projects/my-claude-code-skills && git status && git log --oneline origin/main..HEAD
```

Se há commits locais não pushados: oferecer criar PR.
Se há commits remotos mais novos: `git pull --rebase origin main`.

---

## Regras gerais

- Nunca modificar `docs/CONSTITUTION.md` sem proposta explícita do usuário.
- Sempre manter os READMEs dos packages atualizados após qualquer mudança.
- Todo commit segue o padrão Felipe (conventional + Jira se houver + PT-BR).
- Reportar sempre em PT-BR.

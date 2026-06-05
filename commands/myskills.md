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

Packages não instalados → mostrar sequência exata:
  1. `/plugin install <package>@myskills`
  2. `/reload-plugins`  ← obrigatório antes do próximo passo
  3. `/<package>:setup`
MCPs faltando → mostrar: `claude mcp add ...` ou env var necessária
Standalone não rodado → mostrar: `/<package>:setup` (só funciona após reload)

---

## FLUXO INSTALL

Argumento: `install <package>` onde package é design | copy | marketing | programming | workflow.

1. Confirmar que o marketplace está registrado:
   - Se não: `claude plugin marketplace add FelipeOFF/my-claude-code-skills`
   
2. Instalar o package e recarregar:
   ```
   /plugin install <package>@myskills
   /reload-plugins
   ```
   ⚠️ O `/reload-plugins` é OBRIGATÓRIO — sem ele, o `/<package>:setup` não aparece.

3. Rodar o setup standalone:
   - Só após o reload o comando fica disponível: `/<package>:setup`
   - Exemplo: `/plugin install design@myskills` → `/reload-plugins` → `/design:setup`.

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
- Criar stub SKILL.md de dependency (explicando que a real vem via dep).
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

Auto-sync das skills instaladas localmente com o repo myskills, gerando PR com as diferenças.

### Passo 1 — Inventariar skills instaladas localmente

```bash
# Skills standalone instaladas via skills CLI
ls ~/.claude/skills/ 2>/dev/null | sort

# Skills do myskills repo (já versionadas)
for pkg in design copy marketing programming workflow; do
  echo "=== $pkg ==="
  ls ~/Projects/my-claude-code-skills/plugins/$pkg/skills/ 2>/dev/null
done
```

### Passo 2 — Detectar diferenças

Comparar as duas listas:
- **Skills locais não documentadas no repo** → candidatas a adicionar
- **Skills documentadas no repo mas não instaladas** → candidatas a remover ou marcar como `source: standalone-setup`
- **Skills de plugins (enabledPlugins)** → já documentadas via deps, ignorar

Filtrar falsos positivos: skills do GSD (`gsd-*`), superpowers, octo, claude-mem, codex, ralph-specum, sleepwell **não entram no myskills** — são deps de plugins, não curadoria manual.

### Passo 3 — Para cada nova skill detectada

Aplicar o mesmo fluxo do **FLUXO ADD**:
1. Classificar por Regra A → package correto
2. Criar stub SKILL.md com `source: standalone-setup` (ou `authored` se for autoral)
3. Atualizar README do package
4. Não commitar ainda — acumular todas as mudanças

### Passo 4 — Criar branch e PR

```bash
cd ~/Projects/my-claude-code-skills
git checkout -b chore/sync_skills_$(date +%Y%m%d)
git add -A
git commit -m "chore: Auto-sync skills instaladas localmente

Skills adicionadas: <lista>
Skills removidas: <lista>
Gerado via /myskills sync"
git push origin chore/sync_skills_$(date +%Y%m%d)
gh pr create --title "chore: Auto-sync skills $(date +%Y-%m-%d)" --body "..."
```

### Passo 5 — Mostrar resumo

Listar o que mudou e retornar URL do PR criado.

---

## Regras gerais

- Nunca modificar `docs/CONSTITUTION.md` sem proposta explícita do usuário.
- Sempre manter os READMEs dos packages atualizados após qualquer mudança.
- Todo commit segue o padrão Felipe (conventional + Jira se houver + PT-BR).
- Reportar sempre em PT-BR.

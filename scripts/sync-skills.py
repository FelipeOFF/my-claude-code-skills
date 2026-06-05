#!/usr/bin/env python3
"""sync-skills — sincroniza as skills vendorizadas do myskills com seus upstreams.

Cada skill em `plugins/<pkg>/skills/<name>/` pode ter um `.source.json` (dotfile
de proveniência) que diz exatamente de onde o conteúdo veio. Este comando lê
todos eles e atualiza as skills sem o usuário precisar fazer isso à mão.

Direções (`sync_direction` no .source.json):
  - "pull": o conteúdo mora num repo upstream → re-vendoriza para a pasta da skill.
  - "push": a skill é autoral do myskills, espelhada num repo público → empurra.

Uso:
  python3 scripts/sync-skills.py status                # lista proveniência
  python3 scripts/sync-skills.py check                 # dry-run (mostra o que mudaria)
  python3 scripts/sync-skills.py pull [--apply]        # re-vendoriza upstreams (dry por padrão)
  python3 scripts/sync-skills.py push [--apply]        # espelha autorais p/ repos
Filtros: --skill <nome>  --package <pkg>

Só stdlib. `git` via subprocess. Em --apply de pull, o frontmatter curado do
myskills é preservado; só o corpo + arquivos de suporte são atualizados.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGINS = REPO / "plugins"
FUNC_KEYS = ("allowed-tools", "argument-hint", "disable-model-invocation", "model")
JUNK = {".git", ".DS_Store", "node_modules", "SKILL.md", ".source.json",
        ".gitignore", "package.json", "package-lock.json"}


def run(cmd, cwd=None, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, text=True,
                          capture_output=True)


def discover(pkg=None, skill=None):
    out = []
    for sj in sorted(PLUGINS.glob("*/skills/*/.source.json")):
        meta = json.loads(sj.read_text())
        if pkg and meta.get("package") != pkg:
            continue
        if skill and meta.get("name") != skill:
            continue
        out.append((sj.parent, meta))
    return out


def split_fm(text):
    if text.startswith("---"):
        lines = text.split("\n")
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[1:i], "\n".join(lines[i + 1:]).lstrip("\n")
    return None, text


def fm_keys(fm_lines):
    return {re.match(r"^([A-Za-z][\w-]*)\s*:", ln).group(1)
            for ln in fm_lines if re.match(r"^[A-Za-z][\w-]*\s*:", ln)}


def extract_block(fm_lines, key):
    """Pega 'key:' e suas linhas-filhas (listas YAML indentadas)."""
    out, i = [], 0
    while i < len(fm_lines):
        if re.match(rf"^{re.escape(key)}\s*:", fm_lines[i]):
            out.append(fm_lines[i]); j = i + 1
            while j < len(fm_lines) and re.match(r"^\s+\S", fm_lines[j]) \
                    and not re.match(r"^[A-Za-z][\w-]*\s*:", fm_lines[j]):
                out.append(fm_lines[j]); j += 1
            return out
        i += 1
    return []


def debrand_body(body, patterns):
    """Remove linhas que mencionam a marca de origem (atribuição de bundle)."""
    if not patterns:
        return body, []
    scrubbed, kept = [], []
    for ln in body.split("\n"):
        hit = None
        for p in patterns:
            rx = rf"\b{re.escape(p)}\b" if len(p) <= 4 else re.escape(p)
            if re.search(rx, ln, re.IGNORECASE):
                hit = p; break
        if hit:
            scrubbed.append(ln.strip())
        else:
            kept.append(ln)
    return "\n".join(kept), scrubbed


def render(target_fm, upstream_fm, body):
    """Frontmatter curado do myskills + keys funcionais do upstream + corpo."""
    present = fm_keys(target_fm)
    add = []
    if upstream_fm:
        for k in FUNC_KEYS:
            if k not in present:
                add += extract_block(upstream_fm, k)
    idx = next((i for i, ln in enumerate(target_fm)
                if ln.startswith("added:")), len(target_fm))
    new_fm = target_fm[:idx] + add + target_fm[idx:]
    return "---\n" + "\n".join(new_fm) + "\n---\n\n" + body.rstrip() + "\n"


_CLONES = {}
def clone(url, ref):
    key = (url, ref)
    if key in _CLONES:
        return _CLONES[key]
    d = tempfile.mkdtemp(prefix="syncskill-")
    try:
        run(["git", "clone", "--depth=1", "--branch", ref, url, d])
    except subprocess.CalledProcessError:
        run(["git", "clone", "--depth=1", url, d])
    _CLONES[key] = d
    return d


def src_skill_dir(meta):
    s = meta["source"]
    root = clone(s["url"], s["ref"])
    return Path(root) / s["skill_path"] if s["skill_path"] else Path(root)


def pull_one(skill_dir, meta, apply):
    s = meta["source"]
    src = src_skill_dir(meta)
    src_skill = src / s["skill_file"]
    if not src_skill.is_file():
        return ("ERROR", f"upstream sem {s['skill_file']}")
    up_fm, up_body = split_fm(src_skill.read_text())
    body, scrub = debrand_body(up_body, (meta.get("debrand") or {}).get("patterns") or []) \
        if meta.get("debrand", {}) else (up_body, [])
    tgt_skill = skill_dir / "SKILL.md"
    tgt_fm, _ = split_fm(tgt_skill.read_text())
    new = render(tgt_fm, up_fm, body)
    old = tgt_skill.read_text()
    changed = new.strip() != old.strip()
    if apply and changed:
        tgt_skill.write_text(new)
        # arquivos de suporte
        if s["copy_mode"] == "skill_dir":
            excl = set(s.get("exclude") or [])
            for item in src.iterdir():
                if item.name in JUNK or item.name in excl:
                    continue
                dst = skill_dir / item.name
                if item.is_dir():
                    shutil.rmtree(dst, ignore_errors=True)
                    shutil.copytree(item, dst, ignore=shutil.ignore_patterns(*JUNK))
                else:
                    shutil.copy2(item, dst)
        else:
            excl = list(s.get("exclude") or [])
            for name in (meta.get("support_paths") or []):
                sp = src / name
                if not sp.exists():
                    continue
                dst = skill_dir / name
                if sp.is_dir():
                    shutil.rmtree(dst, ignore_errors=True)
                    shutil.copytree(sp, dst, ignore=shutil.ignore_patterns(*JUNK, *excl))
                else:
                    shutil.copy2(sp, dst)
    tag = "would-update" if changed and not apply else \
          "updated" if changed else "up-to-date"
    extra = f" (debrand: {len(scrub)} linhas)" if scrub else ""
    return (tag, f"{s['repo']}@{s['ref']}{extra}")


def push_one(skill_dir, meta, apply):
    s = meta["source"]
    repo = clone(s["url"], s["ref"])
    src = skill_dir / "SKILL.md"
    dst = Path(repo) / "SKILL.md"
    changed = (not dst.exists()) or dst.read_text().strip() != src.read_text().strip()
    if not changed:
        return ("up-to-date", s["repo"])
    if not apply:
        return ("would-push", s["repo"])
    shutil.copy2(src, dst)
    run(["git", "add", "SKILL.md"], cwd=repo)
    run(["git", "commit", "-m", f"chore: sync {meta['name']} from myskills marketplace"],
        cwd=repo)
    run(["git", "push"], cwd=repo)
    return ("pushed", s["repo"])


def main():
    ap = argparse.ArgumentParser(description="sync-skills")
    ap.add_argument("action", choices=["status", "check", "pull", "push"],
                    nargs="?", default="status")
    ap.add_argument("--apply", action="store_true", help="aplica (default: dry-run)")
    ap.add_argument("--skill")
    ap.add_argument("--package")
    a = ap.parse_args()

    items = discover(a.package, a.skill)
    if not items:
        print("nenhuma skill com .source.json"); return 0

    if a.action == "status":
        w = max(len(m["name"]) for _, m in items)
        for _, m in items:
            s = m["source"]
            db = " [debrand]" if m.get("debrand") else ""
            repo = s.get("repo") or "(autoral, sem upstream)"
            ref = f"@{s['ref']}" if s.get("ref") else ""
            commit = f" :{s['commit'][:7]}" if s.get("commit") else ""
            print(f"{m['name']:<{w}}  {m['sync_direction']:<4}  "
                  f"{repo}{ref}{commit}{db}")
        print(f"\n{len(items)} skills rastreadas")
        return 0

    apply = a.apply
    pulls = [(d, m) for d, m in items if m["sync_direction"] == "pull"]
    pushes = [(d, m) for d, m in items if m["sync_direction"] == "push"]
    do_pull = a.action in ("check", "pull")
    do_push = a.action in ("check", "push")
    changed = 0
    try:
        if do_pull:
            print("== PULL (upstream → myskills) ==")
            for d, m in pulls:
                tag, info = pull_one(d, m, apply and a.action == "pull")
                if tag in ("would-update", "updated"):
                    changed += 1
                print(f"  [{tag:>12}] {m['name']:<28} {info}")
        if do_push:
            print("== PUSH (myskills → repo público) ==")
            for d, m in pushes:
                tag, info = push_one(d, m, apply and a.action == "push")
                if tag in ("would-push", "pushed"):
                    changed += 1
                print(f"  [{tag:>12}] {m['name']:<28} {info}")
    finally:
        for d in _CLONES.values():
            shutil.rmtree(d, ignore_errors=True)
    verb = "aplicadas" if apply else "pendentes (rode com --apply)"
    print(f"\n{changed} mudança(s) {verb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

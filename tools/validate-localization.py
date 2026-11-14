#!/usr/bin/env python3
"""Validate English/default and Simplified-Chinese skill pairs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EN_SKILLS = SKILLS / "en"
CN_SKILLS = SKILLS / "zh-CN"
CATALOG = ROOT / "catalog.yml"
HAN = re.compile(r"[\u3400-\u9fff]")
EXECUTABLE_PARTS = {"scripts", "tools", "runtime"}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter: {path}")
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def executable_files(root: Path, *, localized_name: str | None = None, base_name: str | None = None) -> dict[str, bytes]:
    result = {}
    for path in root.rglob("*"):
        if path.is_file() and any(part in EXECUTABLE_PARTS for part in path.relative_to(root).parts):
            if "node_modules" not in path.parts and "__pycache__" not in path.parts and path.name != "package-lock.json" and path.suffix != ".pyc":
                data = path.read_bytes()
                if localized_name and base_name:
                    data = data.replace(localized_name.encode(), base_name.encode())
                result[str(path.relative_to(root))] = data
    return result


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8")) or {}
catalog_by_id = {item.get("id"): item for item in catalog.get("skills", [])}
catalog_ids = set(catalog_by_id)
bases = sorted(path.name for path in EN_SKILLS.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())
cn_names = sorted(path.name for path in CN_SKILLS.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())

for base in bases:
    entry = catalog_by_id.get(base, {})
    if entry.get("standalone") is True:
        meta = frontmatter(EN_SKILLS / base / "SKILL.md")
        if f"{base}-cn" in cn_names or meta.get("name") != base:
            fail(f"invalid standalone English skill: {base}")
        if entry.get("path") != f"skills/en/{base}" or entry.get("language") != "en":
            fail(f"standalone catalog mismatch: {base}")
        if entry.get("translation_of") or (meta.get("metadata") or {}).get("translation_of"):
            fail(f"standalone skill must not name a translation pair: {base}")
        if HAN.search((EN_SKILLS / base / "SKILL.md").read_text(encoding="utf-8")):
            fail(f"English SKILL.md contains Chinese prose: {base}")
        continue
    cn = f"{base}-cn"
    if cn not in cn_names:
        fail(f"missing Chinese pair for {base}")
    en_dir, cn_dir = EN_SKILLS / base, CN_SKILLS / cn
    en_meta, cn_meta = frontmatter(en_dir / "SKILL.md"), frontmatter(cn_dir / "SKILL.md")
    if en_meta.get("name") != base or cn_meta.get("name") != cn:
        fail(f"frontmatter name mismatch for {base}")
    en_loc, cn_loc = en_meta.get("metadata") or {}, cn_meta.get("metadata") or {}
    if en_loc.get("language") != "en" or en_loc.get("translation_of") != cn:
        fail(f"English locale metadata mismatch for {base}")
    if cn_loc.get("language") != "zh-CN" or cn_loc.get("translation_of") != base:
        fail(f"Chinese locale metadata mismatch for {cn}")
    if HAN.search((en_dir / "SKILL.md").read_text(encoding="utf-8")):
        fail(f"English SKILL.md contains Chinese prose: {base}")
    if not HAN.search((cn_dir / "SKILL.md").read_text(encoding="utf-8")):
        fail(f"Chinese SKILL.md contains no Chinese prose: {cn}")
    if executable_files(en_dir) != executable_files(cn_dir, localized_name=cn, base_name=base):
        fail(f"executable assets differ across locales: {base}")
    for expected in (base, cn):
        if expected not in catalog_ids:
            fail(f"catalog entry missing: {expected}")
        locale = "zh-CN" if expected.endswith("-cn") else "en"
        entry = catalog_by_id[expected]
        if entry.get("path") != f"skills/{locale}/{expected}":
            fail(f"catalog path mismatch: {expected}")
        if entry.get("language") != ("zh-CN" if locale == "zh-CN" else "en"):
            fail(f"catalog language mismatch: {expected}")

standalone = {name for name, entry in catalog_by_id.items() if entry.get("standalone") is True and entry.get("language") == "zh-CN"}
for name in standalone:
    entry = catalog_by_id[name]
    if name not in cn_names or name[:-3] in bases:
        fail(f"standalone skill must be Chinese-only: {name}")
    meta = frontmatter(CN_SKILLS / name / "SKILL.md")
    if meta.get("name") != name or (meta.get("metadata") or {}).get("language") != "zh-CN":
        fail(f"standalone skill metadata mismatch: {name}")
    if entry.get("translation_of") or (meta.get("metadata") or {}).get("translation_of"):
        fail(f"standalone skill must not name a translation pair: {name}")
    if entry.get("path") != f"skills/zh-CN/{name}" or entry.get("language") != "zh-CN":
        fail(f"standalone catalog mismatch: {name}")
    if not HAN.search((CN_SKILLS / name / "SKILL.md").read_text(encoding="utf-8")):
        fail(f"Chinese SKILL.md contains no Chinese prose: {name}")

orphans = [name for name in cn_names if name.endswith("-cn") and name[:-3] not in bases and name not in standalone]
if orphans:
    fail(f"orphan Chinese skills: {', '.join(orphans)}")

actual = set(bases) | set(cn_names)
if actual != catalog_ids:
    fail(f"catalog/package IDs differ: {sorted(actual ^ catalog_ids)}")
for name, entry in catalog_by_id.items():
    if "qa" in entry:
        fail(f"local QA path must not appear in public catalog: {name}")
    version = entry.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"invalid catalog version: {name}")
    meta = frontmatter(ROOT / entry["path"] / "SKILL.md")
    if not isinstance(meta.get("description"), str) or not meta["description"].strip():
        fail(f"missing skill description: {name}")
    source_version = (meta.get("metadata") or {}).get("version")
    if source_version is not None and str(source_version) != version:
        fail(f"catalog/frontmatter version mismatch: {name}")

standalone_en = sum(catalog_by_id[name].get("standalone") is True for name in bases)
print(f"OK: {len(bases) - standalone_en} localization pairs and {len(standalone) + standalone_en} standalone skills validated")

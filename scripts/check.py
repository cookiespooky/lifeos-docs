#!/usr/bin/env python3
"""Проверка мануалов до сборки — то, чего не проверяет движок. Без пакетов.

- у каждой страницы type, slug, title, description; slug — латиница, цифры и дефис;
- у мануала (type: article) — section вида «1 · Название» и order числом;
- главная — одна; разделы с одним номером, но разными названиями — ошибка (опечатка в section).
"""
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
errors, homes, sections = [], 0, {}
files = sorted(CONTENT.rglob("*.md"))
for f in files:
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    rel = f.relative_to(CONTENT)
    if not m:
        errors.append(f"{rel}: нет шапки --- … ---")
        continue
    fm = dict(re.findall(r'^(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))
    for key in ("type", "slug", "title", "description"):
        if not fm.get(key):
            errors.append(f"{rel}: нет поля {key}")
    if fm.get("slug") and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fm["slug"]):
        errors.append(f"{rel}: slug «{fm['slug']}» — только латиница, цифры и дефис")
    t = fm.get("type")
    if t == "home":
        homes += 1
    elif t == "article":
        sec = fm.get("section", "")
        mm = re.fullmatch(r"(\d+) · (.+)", sec)
        if not mm:
            errors.append(f"{rel}: section — вида «1 · Название раздела»")
        else:
            sections.setdefault(mm.group(1), set()).add(sec)
        if not re.fullmatch(r"\d+", fm.get("order", "")):
            errors.append(f"{rel}: order — числом")
    elif t:
        errors.append(f"{rel}: type «{t}» — бывает home и article")
for n, names in sections.items():
    if len(names) > 1:
        errors.append(f"раздел {n} назван по-разному: {', '.join(sorted(names))}")
if homes != 1:
    errors.append(f"главных страниц {homes}, нужна одна (content/home.md)")
for e in errors:
    print("  ✗", e)
print(f"мануалов проверено: {len(files)}, ошибок: {len(errors)}")
sys.exit(1 if errors else 0)

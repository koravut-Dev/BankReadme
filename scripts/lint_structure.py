"""Check that a README follows the standard skeleton and markdown hygiene.

Usage: python scripts/lint_structure.py path/to/README.md [--tier tiny|normal|large]

FAIL lines make the exit code 1. WARN lines are advice. Checks:
  - exactly one H1, heading levels never skip
  - required sections present: install, usage, license (Thai or English names)
  - table of contents present when the page has 7+ H2 sections, and every
    in-page link resolves to a heading (GitHub anchor rules, Thai kept)
  - every fenced code block has a language tag and fences are balanced
  - every image has alt text; no image URL is used twice (alt-less or repeated
    dividers are the usual offender)
  - relative links point to files that exist
  - no empty sections, no leftover placeholders (HERO_URL, TODO, lorem)
"""
import os, re, sys, unicodedata
from collections import Counter

REQUIRED = {
    "install": r"(ติดตั้ง|install|เริ่มต้นใช้งาน|เริ่มต้น|getting started)",
    "usage": r"(วิธีใช้|การใช้งาน|ใช้งาน|วิธีรัน|ลองใน|usage|quick ?start|วิธีอ่าน)",
    "license": r"(ใบอนุญาต|ไลเซนส์|ลิขสิทธิ์|license|licence)",
}
PLACEHOLDERS = re.compile(r"(HERO_URL|STRIP_URL|LIGHT_URL|DARK_URL|DIVIDER_URL|\bTODO\b|\bTBD\b|lorem ipsum|<ชื่อโปรเจกต์>|your[-_ ]project)", re.I)


def gh_anchor(text, seen):
    t = re.sub(r"`([^`]*)`", r"\1", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t).strip().lower()
    keep = []
    for ch in t:
        cat = unicodedata.category(ch)
        if ch in " -" or cat[0] in "LMN" or cat == "Pc":
            keep.append(ch)
    a = "".join(keep).replace(" ", "-")
    n = seen.get(a, 0)
    seen[a] = n + 1
    return a if n == 0 else f"{a}-{n}"


def main(path, tier=None):
    base = os.path.dirname(os.path.abspath(path))
    raw = open(path, encoding="utf-8").read()
    lines = raw.splitlines()
    fails, warns = [], []

    # pass 1: split code blocks from prose, collect fence info
    prose = []
    in_code, fence_open_line = False, 0
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(`{3,}|~{3,})\s*(\S*)", line)
        if m:
            if not in_code:
                in_code, fence_open_line = True, i
                if not m.group(2):
                    fails.append(f"line {i}: code fence has no language tag (use bash, text, json...)")
            else:
                in_code = False
            prose.append("")
            continue
        prose.append("" if in_code else line)
    if in_code:
        fails.append(f"line {fence_open_line}: code fence never closed")

    # headings
    heads = []  # (line, level, text)
    for i, line in enumerate(prose, 1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    h1 = [h for h in heads if h[1] == 1]
    if len(h1) != 1:
        fails.append(f"expected exactly one H1 title, found {len(h1)}")
    prev = 0
    for i, lvl, txt in heads:
        if prev and lvl > prev + 1:
            fails.append(f"line {i}: heading level jumps from H{prev} to H{lvl} ({txt[:40]})")
        prev = lvl

    # required sections
    names = [t for _, _, t in heads]
    for key, pat in REQUIRED.items():
        if not any(re.search(pat, n, re.I) for n in names):
            fails.append(f"missing required section: {key} (heading matching {pat})")

    # empty sections
    for idx, (i, lvl, txt) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(prose) + 1
        body = [l for l in prose[i:end - 1] if l.strip()]
        raw_body = [l for l in lines[i:end - 1] if l.strip()]
        nxt_lvl = heads[idx + 1][1] if idx + 1 < len(heads) else 0
        if not raw_body and not (nxt_lvl > lvl):
            fails.append(f"line {i}: section '{txt[:40]}' is empty")

    # table of contents
    h2 = [h for h in heads if h[1] == 2 and not re.search(r"(สารบัญ|contents)", h[2], re.I)]
    toc = [h for h in heads if re.search(r"(สารบัญ|table of contents|contents)", h[2], re.I)]
    need_toc = len(h2) >= 7 or len(lines) >= 150
    if tier == "tiny":
        need_toc = False
    if tier == "large":
        need_toc = True
    if need_toc and not toc:
        fails.append(f"table of contents (## สารบัญ) required: {len(h2)} sections, {len(lines)} lines")
    if toc and tier == "tiny":
        warns.append("tiny README with a table of contents: consider removing it")

    seen, anchors = {}, set()
    for _, _, t in heads:
        anchors.add(gh_anchor(t, seen))
    for m in re.finditer(r"\]\(#([^)\s]+)\)", "\n".join(prose)):
        target = m.group(1)
        from urllib.parse import unquote
        if unquote(target).lower() not in anchors:
            fails.append(f"dead in-page link: #{unquote(target)}")

    # images
    text = "\n".join(prose)
    imgs = []
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)\s]+)", text):
        imgs.append((m.group(1), m.group(2)))
    for m in re.finditer(r"<img\b[^>]*>", text, re.I):
        tag = m.group(0)
        a = re.search(r'alt="([^"]*)"', tag)
        s = re.search(r'src="([^"]*)"', tag)
        imgs.append((a.group(1) if a else "", s.group(1) if s else ""))
    for alt, src in imgs:
        if not alt.strip():
            fails.append(f"image without alt text: {src[:60]}")
        elif len(alt) > 160:
            warns.append(f"alt text over 160 chars ({len(alt)}): {alt[:40]}...")
    dup = [u for u, c in Counter(s for _, s in imgs).items() if c > 1 and u]
    # a light/dark <picture> pair uses two different URLs, so same URL twice is a real repeat
    for u in dup:
        fails.append(f"same image used more than once: {u[:70]}")

    # relative links
    for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)", text):
        tgt = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", tgt):
            continue
        p = os.path.join(base, tgt.split("#")[0])
        if tgt.split("#")[0] and not os.path.exists(p):
            fails.append(f"relative link target not found: {tgt}")

    # placeholders
    for i, line in enumerate(prose, 1):
        m = PLACEHOLDERS.search(line)
        if m:
            fails.append(f"line {i}: placeholder left in text: {m.group(0)}")

    for w in warns:
        print("WARN", w)
    for f in fails:
        print("FAIL", f)
    print(f"{len(fails)} fail, {len(warns)} warn")
    return 1 if fails else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tier = None
    if "--tier" in sys.argv:
        tier = sys.argv[sys.argv.index("--tier") + 1]
        args = [a for a in args if a != tier]
    if len(args) != 1:
        sys.exit(__doc__)
    sys.exit(main(args[0], tier))

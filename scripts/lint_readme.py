"""Flag README text that reads as AI-written: emoji, marketing filler, stock phrases.

Usage: python scripts/lint_readme.py path/to/README.md
Exit code 1 if anything is flagged. Code blocks and image URLs are skipped.
This is a blunt tool: read each hit and decide, don't blindly delete.
"""
import re, sys

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B50\U00002B06\U0000FE0F\U0000200D\U00002190-\U000021FF\U00002705\U0000274C]"
)
PHRASES = [
    # Thai filler
    "ยินดีต้อนรับ", "ทรงพลัง", "ครบครัน", "ไร้รอยต่อ", "ยกระดับ", "ปฏิวัติ", "เหนือชั้น", "สุดยอด",
    "มาเริ่มกัน", "ลองดูเลย", "ขอให้สนุกกับ", "ไม่ใช่แค่", "อำนวยความสะดวก", "ตอบโจทย์", "เหมาะสำหรับทุก",
    # English filler
    "powerful", "seamless", "blazing", "cutting-edge", "cutting edge", "robust", "elegant", "game-changer",
    "happy coding", "let's get started", "contributions are welcome", "not just", "streamline", "leverage",
    "effortless", "next-level", "state-of-the-art", "delve",
]


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def main(path):
    raw = open(path, encoding="utf-8").read()
    hits = 0
    body = strip_code(raw)
    for n, line in enumerate(body.splitlines(), 1):
        low = line.lower()
        for m in EMOJI.finditer(line):
            print("emoji   line~%d: %r in %r" % (n, m.group(), line.strip()[:70])); hits += 1; break
        for p in PHRASES:
            if p.lower() in low:
                print("phrase  line~%d: %r in %r" % (n, p, line.strip()[:70])); hits += 1
        if line.count("—") >= 2:
            print("dashes  line~%d: %d em dashes in %r" % (n, line.count("—"), line.strip()[:70])); hits += 1
    bullets = [l for l in body.splitlines() if re.match(r"\s*[-*] \*\*[^*]+\*\*\s*[:：]", l)]
    if len(bullets) >= 4:
        print("pattern %d bullets use '**Bold label**: text' (vary the form)" % len(bullets)); hits += 1
    alerts = len(re.findall(r"> \[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]", body))
    if alerts > 2:
        print("pattern %d alert boxes (keep to 2 real ones)" % alerts); hits += 1
    print("%d style issue(s)" % hits)
    return 1 if hits else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

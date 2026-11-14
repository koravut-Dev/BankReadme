"""Check every hyperweave.app image URL in a README actually renders.

HyperWeave answers HTTP 200 even for broken requests (the body is an
"error-state" / "NO SIGNAL" SVG), so a status-only check passes broken images.
Also flags /v1/a/<digest> handles, which 404 on the public site, and prints the
reason text from an error SVG so you can fix the field it names.

Some mistakes render a normal-looking image with no error (an unknown icon id,
a profile card for a user that does not exist, a data= token whose package is
missing and shows "-"). Those cannot be detected here, so the script prints a
CHECK line for each icon, card, chart and data= URL: confirm the identifier
against the manifest or git remote and open the image once.

Usage: python scripts/check_images.py path/to/README.md
Exit code 1 if any image is broken. CHECK lines do not affect the exit code.
"""
import html, re, sys, urllib.request

MANUAL = [
    (r"/v1/icon/", "icon id exists?"),
    (r"/v1/card/", "username exists?"),
    (r"/v1/chart/", "owner/repo exists and has enough stars?"),
    (r"[?&]data=", "data token shows a real value, not '-'?"),
]


def reason(body):
    texts = [html.unescape(t).strip() for t in re.findall(r">([^<>]{6,300})<", body)]
    texts = [t for t in texts if t and "NO SIGNAL" not in t and not re.fullmatch(r"ERR_\d+", t)]
    return texts[0].replace("\n", " ")[:160] if texts else ""


def main(path):
    text = open(path, encoding="utf-8").read()
    urls = list(dict.fromkeys(re.findall(r'https://hyperweave\.app/[^\s)"\'<>]+', text)))
    bad = 0
    manual = []
    for u in urls:
        short = u if len(u) < 110 else u[:107] + "..."
        if "/v1/a/" in u:
            print("BAD   handle URL (404 publicly):", short)
            bad += 1
            continue
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "readme-image-check"})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode("utf-8", "ignore")
                status = r.status
        except Exception as e:
            print("BAD   fetch failed (%s):" % e, short)
            bad += 1
            continue
        if status != 200 or "error-state" in body or "NO SIGNAL" in body or "<svg" not in body:
            why = reason(body)
            print("BAD   error SVG / status %s:" % status, short)
            if why:
                print("      reason:", why)
            bad += 1
        else:
            print("ok    %6d bytes" % len(body), short)
            for pat, note in MANUAL:
                if re.search(pat, u):
                    manual.append((note, short))
    for note, short in manual:
        print("CHECK %s %s" % (note, short))
    print("%d image(s), %d broken" % (len(urls), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

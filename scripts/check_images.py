"""Check every hyperweave.app image URL in a README actually renders.

HyperWeave answers HTTP 200 even for broken requests (the body is an
"error-state" / "NO SIGNAL" SVG), so a status-only check passes broken images.
Also flags /v1/a/<digest> handles, which 404 on the public site.

Usage: python scripts/check_images.py path/to/README.md
Exit code 1 if any image is broken.
"""
import re, sys, urllib.request

def main(path):
    text = open(path, encoding="utf-8").read()
    urls = list(dict.fromkeys(re.findall(r'https://hyperweave\.app/[^\s)"\'<>]+', text)))
    bad = 0
    for u in urls:
        short = u if len(u) < 110 else u[:107] + "..."
        if "/v1/a/" in u:
            print("BAD   handle URL (404 publicly):", short); bad += 1; continue
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "readme-image-check"})
            with urllib.request.urlopen(req, timeout=20) as r:
                body = r.read().decode("utf-8", "ignore")
                status = r.status
        except Exception as e:
            print("BAD   fetch failed (%s):" % e, short); bad += 1; continue
        if status != 200 or "error-state" in body or "NO SIGNAL" in body or "<svg" not in body:
            print("BAD   error SVG / status %s:" % status, short); bad += 1
        else:
            print("ok    %6d bytes" % len(body), short)
    print("%d image(s), %d broken" % (len(urls), bad))
    return 1 if bad else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))

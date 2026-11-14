---
name: repo-readme-hyperweave
description: Reads a code repository end to end (manifests, entry points, scripts, folder layout, CI, license, git remote), picks a visual personality that fits the project, and writes a lively, well-designed README.md in friendly Thai using HyperWeave visuals (animated hero, badge strip, dividers, architecture diagram, tech-stack matrix) plus GitHub-native touches (alerts, collapsibles, step lists). Use this skill whenever the user asks to make, rewrite, refresh or beautify a README, "ทำ readme", "เขียน readme สวยๆ", "อ่าน repo แล้วทำ readme", "ทำหน้า repo ให้ดูน่าสนใจ/ไม่เรียบ", or mentions HyperWeave / hw_compose with a repo, even if they never say the word "skill". Also use it to give a project overview page generated from the code itself.
---

# repo-readme-hyperweave

Turn a repo into a README that a newcomer understands in 30 seconds and that has a *personality*, not a template look. Three halves: **understand the repo honestly**, **choose a design direction that fits it**, **write it in friendly Thai**.

The reader just landed on the repo and asks: "What is this? Is it for me? How do I run it?" Everything serves that person. Design makes them stay; correctness makes them trust. A gorgeous README with a wrong install command is worse than a plain one.

## Step 0: Check before you start

1. **Which repo?** Default is the current working directory. No code (no manifest, no sources)? Say so and ask.
2. **Existing README?** Read it first (it often holds the project's purpose). Never overwrite silently: save the old one as `README.old.md` before writing `README.md`, or write `README.new.md` if the user wants to compare. Say which you did.
3. **Private or confidential repo?** Every label you put in an image is encoded into a public URL on `hyperweave.app`. Fine for open-source. For a private, client or internal repo (bank, medical, company code) ask once before building visuals, and if the user agrees keep labels generic (layer names, not customer names, hostnames, secrets or internal URLs). Never put credentials, tokens, internal hostnames or personal data in any image.
4. **Tools.** `hw_compose`, `hw_validate`, `hw_discover` may be deferred: load with ToolSearch (query `hyperweave`). If HyperWeave is unavailable, still deliver the README with plain-markdown fallbacks (see the end) and say the visuals are missing.

## Step 1: Read the repo (facts only)

Collect evidence before writing a sentence. Use Glob/Grep/Read roughly in this order and stop when the checklist is answerable:

- **Identity**: manifest (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, `*.csproj`, `composer.json`, `Gemfile`...), existing README, `LICENSE`, `CHANGELOG`.
- **How to run**: manifest scripts, `Makefile`, `Dockerfile`, `docker-compose.yml`, `.env.example`, CI workflows (CI shows commands that really work).
- **Shape**: top-level folders, entry points, routes/controllers/CLI commands, migrations, config.
- **Tests**: test folders and the command that runs them.
- **Git remote**: `git remote get-url origin` → owner/repo for live GitHub badges and for any `npx ... add owner/repo`, `git clone` or link to the repo. No remote or not GitHub → static badges only, and **never guess the owner**: the name in `LICENSE` or the folder name is not the GitHub owner/repo, and a wrong `npx skills add` or `git clone` line sends readers to someone else's repo or to a 404. Check the manifest `repository` field too. If the owner is still unknown, write the command with a plainly marked placeholder (`<owner>/<repo>`) or use a method that needs no owner (copy the folder), and tell the user in the final message to fill it in.
- **Personality clues**: what kind of thing is it (CLI, web app, API, library, game, data/ML, infra, docs)? Who uses it (hobbyists, developers, businesses)? Is there an existing brand color/logo/name playfulness?

Checklist (write "ไม่พบข้อมูล" in notes, never guess):
1. What problem does it solve, for whom, in one sentence?
2. Main features (3–6), each traceable to code.
3. Tech stack, with versions only if the manifest states them.
4. Requirements to run (runtime versions, services, env vars).
5. Exact install / run / test commands that exist in this repo.
6. Architecture: the 3–7 main pieces and how data moves.
7. Folder map of the important directories.
8. License; contributing guidelines present or not.

Do not invent features, benchmarks, screenshots, user counts, roadmap items, or badges for things the repo lacks (no coverage badge without coverage tooling, no "build passing" without CI). Where code and old README disagree (README says "stores in localStorage", code is a stub), the code wins for what exists today; keep the claim only if it is clearly the intent, label it honestly (e.g. "กำลังพัฒนา"), and mention the mismatch in your final message. Limitations you verified from code or by running it deserve a short "ข้อควรรู้" note (e.g. only a-z0-9 are kept, so Thai-only input gives an empty result).

## Step 2: Fix the structure first, then choose a design direction

**Standard first, design second.** Read [references/readme-structure.md](references/readme-structure.md) now. It lists the standard sections in order (title and tagline, badges, intro, สารบัญ, เกี่ยวกับโปรเจกต์, ฟีเจอร์, เทคโนโลยีที่ใช้, เริ่มต้นใช้งาน, วิธีใช้, โครงสร้างโปรเจกต์, สถาปัตยกรรม, ทดสอบ, ข้อจำกัด, ร่วมพัฒนา, ใบอนุญาต, ผู้พัฒนา), which ones each repo size and type needs, and the markdown hygiene rules. Decide the size tier (tiny, normal, large) and the repo type from your Step 1 notes and write the section list down before you touch HyperWeave. Readers scan for install, usage and license in familiar places, so the skeleton is what makes a README feel professional; the visuals only decorate it. A section the repo cannot back up is omitted, not padded.

A flat README comes from using one genome, one tone, and the same shape for every section. Fix that by picking a **direction** that matches the project's personality, then varying *shape and rhythm* inside it. Pick one, say which in your notes, and stay with it.

| Direction | Fits | Hero / strip | Body visuals | Voice |
|---|---|---|---|---|
| **Playful** | apps, games, UI libs, hobby projects, creative tools | `automata` with two tones (e.g. `variant=teal&pair=violet`, `variant=amber&pair=magenta`; the first tone goes in `variant`, the second in `pair`), motion `rimrun` or `chromatic-pulse` | `primer` `dusk`/`cream` diagram | relaxed and friendly, short casual sentences |
| **Hacker** | CLIs, dev tools, infra, security tooling | `brutalist` (`celadon` emerald, `signal`, `ember`), motion `corner-trace` | `primer` `noir` twin diagram, monospace-flavored tables | terse, confident, command-first |
| **Premium** | SDKs, platforms, B2B products, design systems | `chrome` (`horizon`, `abyssal`, `lightning`), motion `chromatic-pulse` | `primer` `porcelain`/`petrol` twin | polished, benefit-led |
| **Calm** | internal tools, docs, business/finance apps, anything regulated | `primer` `porcelain`/`cream`, static | same genome throughout | plain, careful, no hype |

The trick that makes it feel designed rather than themed: **dark, animated hero + light-adaptive body**. The hero and badge strip carry the color and motion (one accent family), the diagram and matrix are calm `primer` twins that work on both GitHub themes, and the dividers echo the hero's accent. Only the hero (and at most one more visual) gets motion; motion everywhere is noise, adds weight, and some readers disable it.

Rhythm and shape (what removes the "same box repeated" feeling):
- Alternate visual types down the page: hero → strip → text → divider → diagram → text → matrix → collapsible. Never two of the same visual back to back.
- Mix prose forms: a one-paragraph "ทำไมถึงมี" intro, a feature list, numbered steps with code blocks, a table, a GitHub alert, a `<details>` section. Each section a different shape.
- GitHub alerts add color without images: `> [!TIP]`, `> [!NOTE]`, `> [!WARNING]`. Use at most 2, only where they carry real information (a prerequisite, a gotcha), never as decoration.
- `<details><summary>` for long, optional material (full env table, folder tree, FAQ) so the first screen stays light.
- Start `## วิธีใช้` with a short `### ลองใน 30 วินาที` block holding the smallest runnable example (for a tiny repo this is most of the page). Section names and order come from the skeleton; do not invent extra top-level sections.
- No emoji or icon characters in headings, bullets or badges. Color, layout and the HyperWeave visuals carry the personality; emoji read as machine-made.
- One plain tagline near the top that says what the project does. Don't add forced jokes, puns or mascot names: personality comes from a specific, honest voice, not decoration.

Budget: tiny repo (a handful of files) 1–2 visuals, with a strip that doubles as the hero; normal app 4–6; never more than ~8. On a tiny repo get the variety from prose shapes (a 30-second try-it block, alert, collapsible table, a bit of humor) rather than extra images; the "no two same visuals in a row" rule applies only when there are several visuals, so one divider is fine.

## Step 3: Build the visuals (stateless URLs, not `/v1/a/` handles)

**Critical:** `hw_compose` returns `url: https://hyperweave.app/v1/a/<sha256>`. In testing those URLs returned **HTTP 404** from the public site (they live only in the MCP server's local cache), and different genomes of the same strip even produced the same id. Never put them in a README. Instead build **stateless URLs from the public URL grammar**, which load for anyone and encode everything in the link. Use `hw_compose`/`hw_validate` only to try a spec and read errors or the markdown shadow; the thing you embed is the grammar URL.

Read [references/hyperweave-catalog.md](references/hyperweave-catalog.md) before you choose visuals. It maps each repo fact to the right visual (strip, badge with live data, star chart, profile card, icon, marquee, matrix, divider, and all twelve diagram topologies), gives the smallest working spec for each topology, the 59 diagram presets, the divider whitelist per genome, and the failures that render a normal-looking image so no checker catches them.

URL patterns (base `https://hyperweave.app`; `{motion}` is `static` or one the genome allows; percent-encode path segments and query values, including `+` as `%2B` and Thai/UTF-8 text):

| Visual | URL |
|---|---|
| Badge | `/v1/badge/{title}/{value}/{genome}.{motion}?variant=...` |
| Strip (hero / badge row) | `/v1/strip/{title}/{genome}.{motion}?value=KEY:val,KEY:val&variant=...&pair=...` |
| Marquee | `/v1/marquee/{title}/{genome}.{motion}?variant=...` (also `data=` tokens) |
| Icon (a tool's logo) | `/v1/icon/{glyph}/primer.static?shape=circle\|square&variant=...` |
| Profile card (a person's profile README) | `/v1/card/{username}/primer.static?variant=...` |
| Star history (public GitHub repo with real stars) | `/v1/chart/stars/{owner}/{repo}/primer.static?variant=...` |
| Diagram preset | `/v1/diagram/{preset}/primer.static?variant=...&face=light\|dark` (59 names in the catalog) |
| Divider (genome-specific) | `/v1/divider/{slug}/{genome}.static` with `aura` (primer), `seam` or `sigil` (brutalist), `dissolve` (automata), `band` (chrome); other slugs return an error SVG |
| Divider (generic, safest) | `/a/inneraura/dividers/{block\|current\|takeoff\|void\|zeropoint}` — works for any README but ignores your accent color |
| Diagram | `/v1/diagram/custom/primer.static?variant=...&face=light\|dark&spec=<base64url JSON>` |
| Matrix | `/v1/matrix/custom/primer.static?variant=...&face=light\|dark&spec=<base64url JSON>` |
| Live data (public GitHub only) | strip/badge `data=gh:owner/repo.stars,gh:owner/repo.forks`; `pypi:`/`npm:`/`crates:` only if the package is truly published under that name |

Genome facts (verified): `primer` (light, 8 variants noir/carbon/space/anvil/porcelain/cream/dusk/petrol; the only one that does diagrams; motions static, chromatic-pulse, corner-trace), `brutalist` (dark; variants like celadon, signal, ember, onyx; many motions), `chrome` (dark metallic; horizon, abyssal, lightning, graphite, moth), `automata` (dark cellular; 16 tones, give two tones as `variant=<tone1>&pair=<tone2>`; `pair=teal%2Bviolet`, `pair=teal,violet` and `pair=teal:violet` all return an error SVG; motions static, chromatic-pulse, rimrun, corner-trace). Dividers are whitelisted per genome (`aura` primer, `seam` and `sigil` brutalist, `dissolve` automata, `band` chrome); a slug from another genome fails, and the error lists the allowed ones. `hw_discover` with `what: "all"` can crash on Windows with a charmap error, so ask one selector at a time (`genomes`, `diagram`, `matrix`). The `glyphs` list can come back empty, so do not depend on a glyph id.

Building the `spec=` link (works for diagram and matrix; the decoded JSON must stay under 8 KB, so keep labels short):

```python
import json, base64
spec = {"topology": "pipeline", "title": "ลำดับการทำงาน",
        "nodes": [{"label": "ผู้ใช้", "desc": "เปิดเว็บ"},
                  {"label": "API", "desc": "รับคำสั่งซื้อ"},
                  {"label": "ฐานข้อมูล", "desc": "เก็บออเดอร์"}]}
b = base64.urlsafe_b64encode(json.dumps(spec, ensure_ascii=False).encode()).decode().rstrip("=")
print("https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=" + b)
```

Thai text in labels renders correctly (tested). Generate each URL with a script like this rather than by hand; one typo in base64 means a broken image. Edges are objects with `source` and `target` node ids (plus optional `label`, `relation`). To fetch a URL for checking, use Python (`urllib`) or pass the URL straight to `curl`; piping it through `xargs curl` can silently return nothing.

**Diagram topology** (the picture should show the mechanism, not just list boxes):
- one direction request → processing → storage: `pipeline`; one entry to many: `fanout`; many into one: `fanin`
- layered app (UI / API / DB): `pipeline` with `"orientation": "vertical"`, or the preset `stack` (there is no `stack` topology; `topology: "stack"` returns ERR_422); free dependency graph: `dag` (needs `edges`); folder/package hierarchy: `tree`
- lifecycle with states: `state-machine`; something everything touches: `hub`; separate services with ownership rows: `lanes` (4 or more nodes, each with a `category`); call order: `sequence`
- retry, review or improve cycle: `cycle` with `"orientation": "ring"` or `"orbit"`; a loop with exits: a `loop-*` preset; old versus new, or two options: `comparison`

Twelve topologies exist in total; the catalog has the rules and smallest working spec for each. When a custom spec fails, the error SVG states the reason in its text (for example `orientation 'horizontal' is not legal for cycle`); read it from the body and fix that field.

If no topology honestly fits, skip the diagram; a made-up flow misleads readers. Edges reference node ids (`n0`, `n1`, ...), not labels; for plain `pipeline`, `fanout`, `fanin` omit `edges` and they are derived. Spell edges out for `dag`, `hub`, `tree`, `cycle`, `comparison`, `sequence`, `state-machine`, `lanes`.

Matrix: the label column is implicit. Declare only the non-label columns in `columns`, each as an object with both `id` and `label` (a column without `id` fails with ERR_422 `matrix.columns.0.id Field required`), and give each row a `label` plus one cell per declared column (a "ชั้น / เทคโนโลยี / หน้าที่" table = `label` is the ชั้น, `columns` has two entries). Declaring the label column too fails with "expected N (one per non-label column)" via `hw_compose`, or ERR_422 via the URL. Try the spec once with `hw_compose` and `render_target: "markdown"` to check the shape cheaply. A cell is written `{"value": "..."}` (plain text kind). On Windows, native Python needs `D:/...` style paths; Git Bash `/d/...` paths fail inside Python. When the code is only stubs, label the diagram in the prose as the intended design, not as how it works today. Light and dark matrix faces came out byte-identical in one run, so look at both faces before relying on a `<picture>` pair; if they match, use a single face that works on both themes.

Light/dark pair for README (GitHub switches by theme): build the same diagram twice with `face=light` and `face=dark`:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="DARK_URL">
  <img alt="แผนภาพ: ผู้ใช้ → API → ฐานข้อมูล" src="LIGHT_URL">
</picture>
```

Hero for the chosen direction. The title must be a real markdown `# ` heading (the page's only H1) and the tagline plain text, so the page has a title, a search snippet and a table-of-contents target even if images fail. Images go around them, not instead of them:

```markdown
<div align="center">

![ชื่อโปรเจกต์: คำอธิบายสั้นๆ](HERO_URL)

# ชื่อโปรเจกต์

**ประโยคเดียวที่บอกว่าโปรเจกต์นี้ทำอะไร**

![ข้อมูลโปรเจกต์: เวอร์ชัน, ภาษา, ใบอนุญาต](STRIP_URL)

</div>

ย่อหน้าแนะนำ 2 ถึง 3 ประโยค: โปรเจกต์นี้คืออะไร ใช้กับใคร รับอะไรเข้า คืนอะไรออก
```

**A 200 is not enough.** For unsupported combinations the public server returns HTTP 200 with an *error-state SVG* (seen with dividers: on `automata` only `dissolve` worked; on `brutalist`, `/v1/divider/block/brutalist.static` returned a "NO SIGNAL / ERR_404" error SVG with status 200 even though it looks like a valid URL; `primer` accepts `aura`). So for every URL, fetch the body and check it has none of `error-state` or `NO SIGNAL`, and does contain your expected text (a title or metric). One-liner: `curl -s URL | grep -c -E "error-state|NO SIGNAL"` should print `0`. If a divider errors, use the generic `/a/inneraura/dividers/<slug>` form or `primer`/`aura`. A status-only check (`curl -sI`) will pass broken images, so do not rely on it. Some mistakes render a normal image with no error: an unknown icon id, a profile card for a user that does not exist, a `data=` token for a package or repo that is missing (it shows `-`). Take owner, repo, package and icon names from the manifest and `git remote`, and open card, chart and icon images yourself.

Diagrams and matrices fade in even when "static": a screenshot right after load looks washed out. Wait about 3 seconds before judging contrast. On Windows run Python with `PYTHONUTF8=1`, or printing Thai raises a cp874 error.

**Run the bundled checker on the finished README** (it fetches each hyperweave.app URL, rejects error SVGs and `/v1/a/` handles, and exits 1 if anything is broken):

```bash
PYTHONUTF8=1 python <skill-dir>/scripts/check_images.py README.md
```

Fix every `BAD` line (the `reason:` line under it quotes the server's own message) and rerun until it reports 0 broken. Each `CHECK` line is an image the script cannot judge (icon, profile card, star chart, live `data=` token): confirm the identifier against the manifest or `git remote`, open the image once, and make sure a live value is a real number, not `-`.

**Then look at the images yourself** before you finish. Open at least the hero, one divider and the diagram: with the built-in browser (`navigate` to the URL, then `get_page_text`/screenshot) or `curl -sI URL` expecting `200`. Check contrast too: a light-face diagram can look washed out on a white page, in which case switch variant (try `cream`, `petrol` or `dusk` for light, `noir` for dark) and recheck. Two hero marquee quirks seen in testing: `items_total: 0` came back both with a pipe-separated title and with `data="text:..."`, so confirm the marquee shows text when you open it; if not, use a strip as the hero.

## Step 4: Write the Thai prose

Write the way a friendly senior teammate explains the project to a new colleague.

- **Common words.** ใช้ "ติดตั้ง", "รัน", "ตั้งค่า", "ไฟล์", "โฟลเดอร์", "ฐานข้อมูล". Keep technical terms Thai developers say in English as-is (API, endpoint, commit, branch, Docker, token, build, deploy); don't transliterate awkwardly and don't translate into formal Thai nobody says.
- **Short sentences, active voice, one idea each.** Lead with what the reader gets: "รันครั้งเดียวก็ได้หน้าเว็บขึ้นที่ localhost:3000".
- **Tone follows the direction** (Playful: relaxed; Hacker: terse; Premium: benefit-led; Calm: plain). Never royal/bureaucratic, never hype ("ที่สุดในโลก"), no ครับ/ค่ะ in every line.
- **Avoid anything that reads as AI-written.** Readers spot it instantly and stop trusting the page. Specifically:
  - No emoji or decorative symbols anywhere (headings, bullets, alerts, taglines). No checkmark/rocket/sparkle characters.
  - No marketing filler: "ยินดีต้อนรับสู่", "ทรงพลัง", "ครบครัน", "ไร้รอยต่อ", "ยกระดับ", "ปฏิวัติ", "เหนือชั้น", "สุดยอด", "powerful", "seamless", "blazing fast", "cutting-edge", "robust", "elegant".
  - No stock openers or closers: "มาเริ่มกันเลย", "ลองดูเลย", "ขอให้สนุกกับการเขียนโค้ด", "Happy coding", "Let's get started", "Contributions are welcome!" with nothing behind it.
  - No "ไม่ใช่แค่ X แต่ยัง Y" / "not just X, but Y" patterns, no tidy triplets of adjectives, no rhetorical questions as headings.
  - No bullet lists where every item is `**Bold label**: sentence`; vary the form, and bold only what a skimmer needs (commands, warnings).
  - No stack of em dashes joining clauses; use a plain full stop or a comma.
  - Don't describe the project in the abstract ("a solution designed to streamline workflows"). Say what it takes in and gives back, with a real example.
  - Be specific and a little imperfect: real file names, real limits ("ยังไม่รองรับ Windows"), a short honest "ยังไม่ได้ทำ" list beats a polished feature wall.
  - Don't use alerts (`> [!NOTE]`) as decoration; keep them for a real prerequisite or gotcha, at most 2.
  Run `scripts/lint_readme.py` (Step 5) to catch the mechanical ones.
- **Consistent terms**: one word per concept (always "ตั้งค่า", not mixed with "คอนฟิก"). If the repo already has Thai UI text or docs, reuse its vocabulary; the `thai-word-check` skill, if available, is made for this.
- **Code, commands, paths, env var names stay exactly as in the repo**, in fenced blocks with a language tag, one command per block so each copies cleanly. Every command must exist in the repo; mark standard-but-not-in-repo commands (e.g. `docker compose up -d`) as such or leave them out. A library listed in the manifest but never imported should not appear as a feature.
- Explain *why* briefly where a step isn't obvious ("ต้องมี Node 20 ขึ้นไป เพราะใช้ fetch ที่มากับ Node"); skip theory.
- Tables for env vars and commands; bullets for features; split paragraphs past ~4 lines. Put a space between Thai and embedded English words/code (e.g. "ใน terminal", not "ในterminal").
- Emoji: none (see the AI-tells list above).

Offer an English README (`README.en.md` with a language-switch link) only if the user asks.

## Step 5: Check, then report

Re-read the README as a newcomer:

1. Every command, path, script name and env var exists in the repo (Grep what you're unsure of; run safe example commands when possible).
2. Every image URL is a stateless grammar URL (no `/v1/a/`), and the ones you opened returned 200 and looked right; no `*_URL` placeholders left.
3. No claim, badge or feature the repo can't back up.
4. The design reads as one direction (accent family, one motion hero) but the sections have varied shapes.
5. The page still works with images off: headings, commands and text carry all essential information (alt text is meaningful Thai).
6. Thai is natural and terms are consistent.
7. The structure follows `references/readme-structure.md`: the sections the repo backs are all there, in the standard order, with the standard Thai headings; `ติดตั้ง`, `วิธีใช้` and `ใบอนุญาต` are present; the table of contents exists when required and every link resolves.
8. Run both linters and fix every hit (or consciously keep one, e.g. a quoted command containing a flagged word). The structure linter checks headings, table-of-contents anchors, code-fence language tags, alt text, duplicate images, relative links and placeholders; the style linter checks emoji and AI-sounding phrases:

```bash
PYTHONUTF8=1 python <skill-dir>/scripts/lint_structure.py README.md
PYTHONUTF8=1 python <skill-dir>/scripts/lint_readme.py README.md
```

Final message to the user (Thai, brief): where the file is, which size tier and sections you used (and which standard sections you left out because the repo has nothing for them), which direction you chose and why, what visuals were added, what is marked TODO/unknown or mismatched with the old README, whether the old README was kept, which images you opened to verify, and one line that images are served from hyperweave.app (offer a PNG/SVG export if they want them self-hosted).

## Fallbacks

- HyperWeave down, or images fail to verify: use plain markdown (`#` title, text badges like **License:** MIT, a markdown table for the stack, a fenced ASCII diagram). `hw_compose` with `render_target: "markdown"` returns a text shadow of a matrix or diagram, a good drop-in.
- Repo too small (one script): hero strip, what/why, usage, limitations, license; no diagram, no matrix, one divider at most.
- Monorepo: a top-level README with a package table linking to each package; offer per-package READMEs afterward.
- Huge repo: sample manifests, entry points and top-level folders; say what you didn't read.

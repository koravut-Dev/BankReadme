# Standard README skeleton

Read this in Step 2, before choosing visuals. A README people trust has a predictable skeleton: they know where install, usage and license live without hunting. Design (hero, diagram, rhythm) sits on top of this skeleton, never replaces it. The skeleton follows the Standard Readme spec, GitHub's own README guidance and the common open-source templates, adapted to Thai headings.

## Contents
- [Order of sections](#order-of-sections)
- [Which sections for which repo size](#which-sections-for-which-repo-size)
- [What goes in each section](#what-goes-in-each-section)
- [Table of contents rules](#table-of-contents-rules)
- [Markdown hygiene](#markdown-hygiene)
- [Repo types](#repo-types)

## Order of sections

Use these headings, in this order, skipping those the repo cannot back up (never fill a section with guesses). Keep one Thai name per section so the page and the table of contents match.

| # | Heading (Thai, keep as written) | English meaning | Source of truth in the repo |
|---|---|---|---|
| 0 | `# <ชื่อโปรเจกต์>` then one-line tagline, badges | Title, tagline, badges | manifest name/description, license, CI |
| 1 | (short intro paragraph, no heading) | What it is, for whom, 2 to 3 sentences | manifest, entry points, old README |
| 2 | `## สารบัญ` | Table of contents | see rules below |
| 3 | `## เกี่ยวกับโปรเจกต์` | Background: the problem and why this exists | old README, code comments |
| 4 | `## ฟีเจอร์` | Features, 3 to 6 bullets, each traceable to code | routes, commands, modules |
| 5 | `## เทคโนโลยีที่ใช้` | Tech stack | manifest dependencies |
| 6 | `## เริ่มต้นใช้งาน` containing `### สิ่งที่ต้องมี`, `### ติดตั้ง`, `### ตั้งค่า` | Getting started: prerequisites, install, configure | engines, Dockerfile, `.env.example`, CI |
| 7 | `## วิธีใช้` | Usage with a real command and its real output | scripts, CLI entry, routes |
| 8 | `## โครงสร้างโปรเจกต์` | Project structure (folder tree, `<details>` if long) | top-level folders |
| 9 | `## สถาปัตยกรรม` | Architecture diagram plus 2 to 4 sentences | only when a topology honestly fits |
| 10 | `## ทดสอบ` | How to run tests | test script, test folder, CI |
| 11 | `## ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ` | Known limits, roadmap | stubs, TODOs, verified gaps |
| 12 | `## ร่วมพัฒนา` | Contributing | `CONTRIBUTING.md`, test command |
| 13 | `## ใบอนุญาต` | License, link to `LICENSE` | `LICENSE` file |
| 14 | `## ผู้พัฒนา` | Maintainers / credits | manifest author, git remote owner |

`ติดตั้ง`, `วิธีใช้` and `ใบอนุญาต` are always present. Everything else follows the size table.

## Which sections for which repo size

| Size | Rule of thumb | Required | Skip |
|---|---|---|---|
| Tiny | under about 10 files, one script or one small package | title, tagline, intro, ติดตั้ง, วิธีใช้, ข้อจำกัด (if any), ใบอนุญาต | สารบัญ, สถาปัตยกรรม, โครงสร้าง, ผู้พัฒนา |
| Normal | an app, API, library or CLI with folders | everything in the table that the repo backs, สารบัญ included once the page has 7 or more sections | สถาปัตยกรรม when no topology fits; ทดสอบ when there are no tests |
| Large | monorepo, many packages, or a long README | all of Normal, a package table linking each package, a FAQ in `<details>` | nothing the repo backs |

Tiny does not mean bare: a 30-second try-it block and a real limits note still apply.

## What goes in each section

- **Title and tagline.** `# ` heading in markdown, so the page has a real title even if images fail. The tagline says what the project takes in and gives back, in one sentence.
- **Badges.** Only for things that exist: license (LICENSE file), language or runtime version (manifest), CI status (workflow file present), package version (manifest, only if truly published). A badge row is one line of images, not a wall. No coverage badge without coverage tooling.
- **Intro.** What it is and who it is for, concrete. Name the real inputs and outputs, for example "รับชื่อสินค้าแล้วคืน slug ที่ใช้ใน URL ได้".
- **เกี่ยวกับโปรเจกต์.** The problem in two or three sentences, then why this approach. Skip if the intro already says it.
- **ฟีเจอร์.** Bullets, each one visible in the code (a route, command, module). Vary the form of bullets; do not make every one `**Label**: sentence`.
- **เทคโนโลยีที่ใช้.** A matrix or table with versions only where the manifest states them. A dependency never imported is not a feature.
- **สิ่งที่ต้องมี.** Runtime versions (and why), services (database, cache), accounts, tools.
- **ติดตั้ง.** Numbered steps, one command per fenced block with a language tag, every command taken from the repo (scripts, Makefile, CI). Mark standard commands not in the repo (`docker compose up -d`) as such. Any command that names the repo (`git clone`, `npx skills add`, `pip install git+...`) uses the owner and name from `git remote get-url origin` or the manifest `repository` field, never a guess from `LICENSE` or the folder name; with no remote, use a marked `<owner>/<repo>` placeholder and say so in the final message.
- **ตั้งค่า.** A table of environment variables from `.env.example`: name, example value (fake), meaning. Never real secrets.
- **วิธีใช้.** The smallest runnable example with its real or clearly labelled expected output. For libraries show an import and one call; for CLIs show command and output; for APIs show a request and response.
- **โครงสร้างโปรเจกต์.** A tree of important folders with one short note each. Put it in `<details>` when longer than about 12 lines.
- **สถาปัตยกรรม.** The diagram, then a short walk-through of one request or one data path. Label it as the intended design if the code is stubs.
- **ทดสอบ.** The exact test command and what it covers. Omit when there are no tests; say so under ข้อจำกัด.
- **ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ.** Verified limits from code or by running it (a short honest list beats a feature wall).
- **ร่วมพัฒนา.** If `CONTRIBUTING.md` exists, link it. If not, give a three-step flow built from facts in the repo: fork and branch, run the test command, open a pull request. No invented policies, no code of conduct claim without the file.
- **ใบอนุญาต.** License name as written in `LICENSE`, linked with a relative path. If there is no license file, write "ยังไม่ได้ระบุใบอนุญาต" and say so in the final message.
- **ผู้พัฒนา.** Author from the manifest or the git remote owner. Omit when unknown.

## Table of contents rules

- Include `## สารบัญ` when the page has 7 or more `##` sections or about 150 or more lines. Tiny READMEs skip it.
- Place it after the intro and before `เกี่ยวกับโปรเจกต์`.
- Link every `##` section and the important `###` ones, as a plain nested list.
- GitHub builds anchors by lowercasing the heading, dropping punctuation, and turning spaces into hyphens; Thai letters and tone marks stay. Duplicate headings get `-1`, `-2` suffixes. Example: `## เริ่มต้นใช้งาน` becomes `#เริ่มต้นใช้งาน`, `## ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ` becomes `#ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ`.
- Run `scripts/lint_structure.py`: it recomputes the anchors and fails on any dead link.

## Markdown hygiene

- Exactly one `# ` heading. Heading levels never skip (no `##` straight to `####`).
- Every fenced block has a language tag (`bash`, `json`, `text`, `python`...). Use `text` for output and trees.
- Every image has meaningful alt text in Thai, short (under about 120 characters), and an image is never used twice (a repeated divider counts).
- Relative links (`LICENSE`, `CONTRIBUTING.md`, `docs/...`) point at files that exist.
- Paragraphs under about 4 lines; one blank line between blocks; Thai and English words separated by a space.
- No section left empty or holding only a placeholder.

## Repos that are mostly stubs

When the code is placeholders (empty handlers, comments only, a dependency never imported), keep the standard sections but tell the truth inside them instead of dropping the skeleton:

- Title the feature section `ฟีเจอร์ที่วางแผนไว้` and say in the first line that the code does not run these yet.
- Under `สถาปัตยกรรม` caption the diagram as the intended design, not what runs today.
- Under `ทดสอบ` write what exists ("ยังไม่มีไฟล์ทดสอบ" even if CI runs a test command) and the command that is wired up, so the reader is not misled.
- Put every verified gap (build breaks, unused dependency, missing entry file) in `ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ`, not scattered through the page.
- Use at most one warning alert near the top to say the project is early.

## Repo types

Adjust, do not drop, the skeleton:

- **CLI or script:** วิธีใช้ is the star: command, flags table, example output. Often Tiny.
- **Web app or API:** full skeleton; ตั้งค่า table; สถาปัตยกรรม with the real data path; ทดสอบ.
- **Library or SDK:** ติดตั้ง via the package manager, วิธีใช้ with import and a call, an API summary table; badge for the published version only if published.
- **Collection of skills, plugins or templates:** replace ฟีเจอร์ with a catalog table (name, what it does, how to call it), keep ติดตั้ง and วิธีใช้ (the first thing to say to try it), add a short "ถ้าไม่ทำงาน" section.
- **Monorepo:** top-level README with a package table linking each package README; the per-package READMEs follow the skeleton.
- **Docs or data repo:** replace ติดตั้ง and วิธีใช้ with "วิธีอ่าน / วิธีใช้ข้อมูล" but keep the heading names so the structure check still passes (`วิธีใช้` is mandatory).

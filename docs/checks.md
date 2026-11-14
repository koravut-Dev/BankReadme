# Checks, layout and tests

## The three check scripts

The skill runs these before it hands a README back. You can run them yourself. On Windows set `PYTHONUTF8=1`, or printing Thai fails with an encoding error.

```bash
PYTHONUTF8=1 python scripts/check_images.py README.md
```

```bash
PYTHONUTF8=1 python scripts/lint_structure.py README.md --tier normal
```

```bash
PYTHONUTF8=1 python scripts/lint_readme.py README.md
```

| Script | What it checks | Fails when |
|---|---|---|
| `check_images.py` | Every hyperweave.app link loads and is not an error image. Prints the reason an error image gives. Prints a `CHECK` line for icons, cards, charts and live data, which it cannot judge. | a `/v1/a/` link, an error image, a failed fetch |
| `lint_structure.py` | One H1, no skipped heading levels, install, usage and license sections, a table of contents when needed and working links in it, a language tag on every code block, alt text, no repeated image, working relative links, no leftover placeholder | any FAIL line |
| `lint_readme.py` | Emoji, marketing filler and phrases that sound machine-written | any hit |

`--tier tiny` turns off the table-of-contents rule for small repos.

## Project layout

```text
SKILL.md                         the steps Claude follows when the skill runs
references/readme-structure.md   standard sections, by repo size and type
references/hyperweave-catalog.md what HyperWeave can draw and how to ask for it
scripts/check_images.py          image link check
scripts/lint_structure.py        structure check
scripts/lint_readme.py           wording and emoji check
evals/                           4 test cases (prompt, case.yaml, graders)
```

Claude reads `SKILL.md` and `references/` when the skill runs. `evals/` is only for testing the skill.

## Tests

`evals/` holds four example repos: a small CLI, a shop API, a notes app whose old README disagrees with its code, and a collection of 11 skills. Each case has numbered checks in `graders/`. They run with the skill-creator skill, which is a separate tool.

On the latest run the new version passed all checks and the previous version passed about 80%. Each case ran once, so treat that as a rough signal, not a measured rate.

## Working on the skill

There is no `CONTRIBUTING.md`. To change the skill:

1. Edit `SKILL.md`, `references/readme-structure.md` or `references/hyperweave-catalog.md`.
2. Run the cases in `evals/` with skill-creator and compare with the version before your change.
3. If you edit a script, run it on one README that should pass and one that should fail, and confirm it still tells them apart.

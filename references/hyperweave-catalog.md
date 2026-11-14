# HyperWeave catalog for README work

Read this in Step 3 when you pick visuals. Everything marked "probed" was fetched from the public server on 2026-11-14 and rendered; everything else comes from the HyperWeave README (v0.4.7). Base URL `https://hyperweave.app`. Percent-encode path and query values.

## Contents
- [Pick the visual from the repo fact](#pick-the-visual-from-the-repo-fact)
- [Frame types and URLs](#frame-types-and-urls)
- [Diagram topologies](#diagram-topologies)
- [Presets](#presets)
- [Dividers per genome](#dividers-per-genome)
- [Live data tokens](#live-data-tokens)
- [Silent failures](#silent-failures)
- [Self-hosting the images](#self-hosting-the-images)

## Pick the visual from the repo fact

| What the repo shows | Visual | Notes |
|---|---|---|
| name, version, runtime, license | `strip` as hero and badge row | values from the manifest only |
| public GitHub repo with real stars or forks | `strip` or `badge` with `data=gh:owner/repo.stars` | owner and repo from `git remote`, never guessed |
| public GitHub repo with real history | `chart` star history | only when there are enough stars to draw a curve |
| a person's profile README | `card` | `/v1/card/{username}/...` for that user only |
| request flows through stages | `diagram` `pipeline` | |
| UI / API / DB layers | `diagram` `pipeline` vertical, or preset `stack` | |
| one thing used by many | `diagram` `fanout`; many feeding one: `fanin` | |
| central module everything touches | `diagram` `hub` | first node is the hub |
| services with ownership rows | `diagram` `lanes` | at least 4 nodes, each with a `category` |
| lifecycle / status values | `diagram` `state-machine` | |
| retry, review or improve cycle | `diagram` `cycle` (orientation `ring` or `orbit`) | for a loop with exits use a `loop-*` preset |
| call order between components | `diagram` `sequence` | |
| folder or package hierarchy | `diagram` `tree` | each non-root node has one parent |
| two options or old vs new | `diagram` `comparison` | two nodes |
| dependency graph | `diagram` `dag` | needs `edges` |
| stack list, env vars, command table, feature grid | `matrix` | label column implicit |
| a logo for a tool in the stack | `icon` | brand glyph id, see silent failures |
| section break | `divider` | whitelist below |
| release news, tag cloud | `marquee` | motion only if it is the one animated visual |
| live build state | `badge` with `state=passing` | only when CI exists |

If nothing in the right column is backed by the repo, skip the visual.

## Frame types and URLs

| Frame | URL pattern | Probed |
|---|---|---|
| badge | `/v1/badge/{title}/{value}/{genome}.{motion}?variant=...&state=passing` | yes |
| badge with live data | `/v1/badge/{title}/{genome}.static?data=gh:owner/repo.stars` | yes |
| strip | `/v1/strip/{title}/{genome}.{motion}?value=KEY:val,KEY:val&variant=...` or `?data=...` | yes |
| marquee | `/v1/marquee/{title}/{genome}.{motion}?data=text:NEW,text:RELEASE` | yes |
| divider | `/v1/divider/{slug}/{genome}.static` or `/a/inneraura/dividers/{slug}` | yes |
| icon | `/v1/icon/{glyph}/primer.static?shape=circle\|square&variant=noir` | yes |
| card | `/v1/card/{username}/primer.static?variant=porcelain` | yes |
| chart | `/v1/chart/stars/{owner}/{repo}/primer.static?variant=porcelain` | yes |
| matrix | `/v1/matrix/custom/primer.static?variant=...&face=light\|dark&spec=<base64url>` | yes |
| diagram (custom) | `/v1/diagram/custom/primer.static?variant=...&face=light\|dark&spec=<base64url>` | yes |
| diagram (preset) | `/v1/diagram/{preset}/primer.static?variant=...&face=light\|dark` | yes |
| receipt | agent session telemetry; not for READMEs | no |

Genomes: `primer` (8 variants: light porcelain, cream, dusk, petrol; dark noir, carbon, space, anvil; the only genome for diagram, matrix, card, chart, icon in primer style), `brutalist`, `automata` (two tones as `variant=teal&pair=violet`), `chrome` (horizon, abyssal, lightning, graphite, moth). For GitHub bake a light and a dark file and let `<picture>` choose; a `prefers-color-scheme` rule inside one SVG follows the reader's operating system, not the GitHub theme toggle.

## Diagram topologies

All twelve render. Edges reference node ids. Specs below are the smallest ones that rendered (probed); every one needs `title` and `nodes` with `id`, `label`, optional `desc`. An edge is `{"source": "a", "target": "b"}` with optional `label`, `label_style`, `relation`, `kind` (sequence only: `call` or `return`). A matrix column is `{"id": "fit", "label": "เหมาะกับ"}`; both fields are required.

| Topology | Rules (from the server's own messages) | Smallest working spec |
|---|---|---|
| `pipeline` | edges derived; orientation horizontal or vertical | 3 nodes, no edges |
| `fanout` | first node is the source; orientation horizontal, bilateral, upward, downward, radial | 1 source + 2 to 4 targets, no edges |
| `fanin` | many into the last node; horizontal only | 4 nodes, no edges |
| `hub` | every edge touches the hub, the first node declared | hub + 3 satellites, edges hub to each |
| `dag` | any edge allowed; horizontal or vertical; a cycle becomes a state machine | needs `edges` |
| `tree` | every non-root node has exactly one parent edge; horizontal or radial | root + 3 children |
| `lanes` | at least 4 nodes, each with `category`; categories become bands | 4 nodes, 4 categories, chain edges |
| `state-machine` | self-loops and back-edges allowed | 3 nodes, edges incl. a back-edge |
| `sequence` | edges in declaration order connect lifelines; edge `kind` is `call` or `return` | 3 lifelines, 4 labelled edges |
| `cycle` | orientation must be `ring` or `orbit` (not `horizontal`) | 3 nodes, closed edges, `"orientation": "ring"` |
| `comparison` | two nodes, horizontal only | 2 nodes with `desc` |
| `loop` | one `circuit:return` edge, strict station and exit rules | use a `loop-*` preset instead of a custom spec |

There is no `stack` topology: `topology: "stack"` returns ERR_422. A preset named `stack` exists, and `pipeline` with `"orientation": "vertical"` gives layers. When a custom spec fails, the error SVG states the reason in its text (for example `orientation 'horizontal' is not legal for cycle`); read it from the body, fix the field, retry.

Node options worth using: `glyph` (brand logo id), `kind` (core mark such as database, server, shield), `role: "hero"` for the focal node, `chips` (small labels in the card), `node_style` (`card`, `card+glyph`, `pill`, `text`), edge `relation` (`assert` solid, `drift` dashed, `flow` animated, `bypass`), edge `label` with `label_style: "chip"`. Keep one animated element per README.

## Presets

Render by name without writing a spec: `/v1/diagram/{preset}/primer.static?variant=porcelain`. Probed: `stack`, `pipeline-head`, `dag-tiers`, `cycle-ring`, `hub-axial`, `comparison`, `loop-flywheel`, `sm-retry`, `tree`, `sequence`. All 59 names: comparison, cycle-circles, cycle-flow, cycle-orbit, cycle-ring, dag-balanced, dag-bottleneck, dag-gate, dag-join, dag-mesh, dag-mesh-billing, dag-providers, dag-tiers, fanin, fanin-knot, fanout-beam, fanout-bilateral, fanout-bilateral-pair, fanout-bilateral-trio, fanout-downward, fanout-horizontal, fanout-radial, hub-axial, hub-bilateral, hub-text, hub-tiles, hub-verbs, hub-zones, lanes, loop-flywheel, loop-flywheel-accumulate, loop-flywheel-horizontal, loop-hillclimb, loop-hillclimb-turn, loop-nested, loop-nested-laps, loop-retry, loop-retry-budget, loop-retry-unrolled, loop-runloop, loop-shuttle, loop-shuttle-swimlane, loop-shuttle-vertical, loop-tap, pipeline-circles, pipeline-head, pipeline-roundtrip, pipeline-row, scatter-gather, sequence, sm-loop, sm-recursive, sm-retry, sm-terminal, stack, tree, tree-health, tree-radial, tree-radial-health.

A preset shows sample content, not the repo's. Use a preset only for a generic picture (for example a retry loop that really is generic) and say so; for the project's own architecture write a custom spec.

## Dividers per genome

| Genome | Slugs that work (probed) |
|---|---|
| primer | `aura` |
| brutalist | `seam`, `sigil` (`block` returns an error SVG) |
| automata | `dissolve` |
| chrome | `band` |
| any (generic, ignores accent) | `/a/inneraura/dividers/{block\|current\|takeoff\|void\|zeropoint}` |

Match the divider to the hero genome so the page keeps one accent family; use the generic form only when no genome slug fits. Never use the same divider URL twice (the structure linter flags repeats).

## Live data tokens

`data=` takes comma-separated tokens: `text:...`, `kv:...`, or `provider:identifier.metric` such as `gh:owner/repo.stars`, `gh:owner/repo.forks`, `gh:owner/repo.contributors`, `gh:owner/repo.last_push`, `gh:owner/repo.language`, `pypi:pkg.version`, `pypi:pkg.downloads`, `npm:`, `crates:`. Rules:

- `gh:` only when `git remote get-url origin` is a public GitHub repo, with that exact owner and name.
- `pypi:`, `npm:`, `crates:` only when the package is really published under that name; check the registry first.
- Values are cached 5 to 10 minutes; a failed fetch shows `-`, never an invented number. A README must still make sense with `-` in a slot, so keep the plain facts in the text as well.

## Silent failures

These render a normal-looking image (no error SVG), so `check_images.py` cannot catch them. Verify them by reading the body text or opening the image:

- an unknown icon `glyph` still renders an icon (a fallback mark)
- a card for a username that does not exist still renders a card
- a `data=` token for a missing package or repo renders `-`

Confirm the identifier from the repo (manifest, remote) before using it, and for card and chart open the image once.

## Self-hosting the images

Public URLs are the default because they need no build step. If the user wants no external dependency, compose once with the CLI (`uv tool install hyperweave`, then `hyperweave compose ... --format svg -o assets/name.svg`, `--faces` writes a light and dark pair, `--format svg-static` removes animation for renderers that do not run CSS, `--format png` needs the `raster` extra) and point the README at `assets/` instead. Say in the final message that this is available; do not do it unasked.

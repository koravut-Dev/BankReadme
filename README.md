<div align="center">

![repo-readme-hyperweave: a skill that reads a repo and writes a Thai README](https://hyperweave.app/v1/strip/repo-readme-hyperweave/automata.rimrun?value=OUTPUT%3AREADME.md%2CLANGUAGE%3AThai%2CVISUALS%3AHyperWeave&variant=teal&pair=violet)

# repo-readme-hyperweave

**A Claude skill that reads a repo and writes its README in Thai, with a standard section layout and images that actually load.**

</div>

Ask "make a README for this repo" and the skill reads the manifest, scripts, CI and folders first, then writes. The result is a `README.md` with the standard sections, only commands that exist in the repo, and visuals from [HyperWeave](https://github.com/InnerAura/hyperweave). Three scripts check the images, the structure and the wording before it hands the file back.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://hyperweave.app/v1/diagram/custom/primer.static?variant=noir&face=dark&spec=eyJ0b3BvbG9neSI6ICJwaXBlbGluZSIsICJ0aXRsZSI6ICJXaGF0IHRoZSBza2lsbCBkb2VzIiwgIm5vZGVzIjogW3siaWQiOiAiYSIsICJsYWJlbCI6ICJSZWFkIHRoZSByZXBvIiwgImRlc2MiOiAibWFuaWZlc3QsIHNjcmlwdHMsIENJIn0sIHsiaWQiOiAiYiIsICJsYWJlbCI6ICJQaWNrIHRoZSBsYXlvdXQiLCAiZGVzYyI6ICJzdGFuZGFyZCBzZWN0aW9ucyJ9LCB7ImlkIjogImMiLCAibGFiZWwiOiAiUGljayBhIHN0eWxlIiwgImRlc2MiOiAiNCBzdHlsZXMifSwgeyJpZCI6ICJkIiwgImxhYmVsIjogIkJ1aWxkIHRoZSBpbWFnZXMiLCAiZGVzYyI6ICJsaW5rcyB0aGF0IGxvYWQifSwgeyJpZCI6ICJlIiwgImxhYmVsIjogIldyaXRlIGluIFRoYWkiLCAiZGVzYyI6ICJwbGFpbiB3b3JkcyJ9LCB7ImlkIjogImYiLCAibGFiZWwiOiAiQ2hlY2siLCAiZGVzYyI6ICIzIHNjcmlwdHMifV19">
  <img alt="The six steps of the skill: read the repo, pick the layout, pick a style, build the images, write in Thai, check" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJwaXBlbGluZSIsICJ0aXRsZSI6ICJXaGF0IHRoZSBza2lsbCBkb2VzIiwgIm5vZGVzIjogW3siaWQiOiAiYSIsICJsYWJlbCI6ICJSZWFkIHRoZSByZXBvIiwgImRlc2MiOiAibWFuaWZlc3QsIHNjcmlwdHMsIENJIn0sIHsiaWQiOiAiYiIsICJsYWJlbCI6ICJQaWNrIHRoZSBsYXlvdXQiLCAiZGVzYyI6ICJzdGFuZGFyZCBzZWN0aW9ucyJ9LCB7ImlkIjogImMiLCAibGFiZWwiOiAiUGljayBhIHN0eWxlIiwgImRlc2MiOiAiNCBzdHlsZXMifSwgeyJpZCI6ICJkIiwgImxhYmVsIjogIkJ1aWxkIHRoZSBpbWFnZXMiLCAiZGVzYyI6ICJsaW5rcyB0aGF0IGxvYWQifSwgeyJpZCI6ICJlIiwgImxhYmVsIjogIldyaXRlIGluIFRoYWkiLCAiZGVzYyI6ICJwbGFpbiB3b3JkcyJ9LCB7ImlkIjogImYiLCAibGFiZWwiOiAiQ2hlY2siLCAiZGVzYyI6ICIzIHNjcmlwdHMifV19">
</picture>

## Install

1. Open `repo-readme-hyperweave.skill` and press Save skill, or copy this folder to where Claude reads skills (for Claude Code that is `~/.claude/skills/`, the usual location, not defined in this repo):

   ```bash
   cp -r repo-readme-hyperweave ~/.claude/skills/
   ```

2. Start a new session so Claude loads the skill.

You need Python 3 for the check scripts and internet access, because `check_images.py` fetches each image from hyperweave.app. The HyperWeave MCP is optional.

## Usage

Open Claude in the repo you want a README for and type:

```text
Read this repo and make a Thai README with hyperweave
```

When it finishes, the skill tells you which size and sections it used, which style it picked and why, and what in the old README did not match the code. An existing README is kept as `README.old.md`.

The skill picks one of four styles to match the project:

| Style | Fits | Look |
|---|---|---|
| Playful | apps, games, UI libraries, hobby projects | `automata` with two tones, moving header |
| Hacker | CLIs, developer tools, infrastructure | `brutalist` green, trace line around the edge |
| Premium | SDKs, platforms, B2B products | `chrome` metal |
| Calm | internal tools, docs, finance | `primer` light, still |

See [GALLERY.md](GALLERY.md) for every kind of image it can make, and [docs/checks.md](docs/checks.md) for the check scripts, the project layout and the tests.

## Limitations

- Every image is served from hyperweave.app, and label text becomes part of a public URL. For a private repo the skill asks first. If that site is down, the images do not load.
- An icon, profile card or live data token with a wrong name still renders a normal-looking image, so the check script cannot catch it. The skill tells you to confirm those names and open the image.
- The Premium (`chrome`) style has not been tried on a real repo yet.
- The skill description in `SKILL.md` has not been tuned for triggering. If Claude does not pick the skill by itself, name it in your message.
- The check scripts catch known filler words and emoji, not whether the Thai sounds natural. A person still has to read it.

## License

MIT, see [LICENSE](LICENSE).

# Leader Key · Cursor harness (macOS)

[![CI](https://github.com/shahzebqazi/leaderkey/actions/workflows/ci.yml/badge.svg)](https://github.com/shahzebqazi/leaderkey/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Executive summary

- **Validated JSON** — Examples and a **recommended root template** are checked in CI for structure and duplicate keys per group (aligned with Leader Key’s rules).
- **Documented conflicts** — Common macOS chords used by command actions are called out so you can avoid fighting the system.
- **Cursor Glass–aligned docs** — Short, scannable guides; no chain-of-thought in user-facing pages. Works well with Cursor **3+** and the **Agent Window**.

**[Leader Key](https://github.com/mikker/LeaderKey)** is a menu bar app for leader-style shortcuts (apps, URLs, commands, nested groups). This repo does **not** ship the app; it ships **rules**, **examples**, and **tests**.

## Quick links

| Resource | Description |
|----------|-------------|
| [User guide](docs/user-guide.md) | Install, config paths, template workflow, backups |
| [Hotkey conflicts](docs/hotkey-conflicts.md) | macOS shortcuts that overlap with template patterns |
| [UX research outline](docs/ux-research.md) | Prompts for your own notes |
| [Paper (draft): Leader Key hotkeys](docs/paper-leader-key-hotkeys.md) | Position paper: Omarchy, RTS, ergonomics, mnemonic map |
| [Scripts (roadmap)](scripts/README.md) | Reserved for future automation |

## Examples

| File | Role |
|------|------|
| [examples/config.default.from-upstream.json](examples/config.default.from-upstream.json) | **Upstream default** from Leader Key’s `defaultConfig` (Terminal, app groups, Raycast URLs) |
| [config/templates/recommended-root.template.json](config/templates/recommended-root.template.json) | **Sanitized template** — generic paths and labels; edit before use |

## GitHub Pages

Static showcase: **[docs/index.html](docs/index.html)** — enable **Pages** → **Deploy from a branch** → **`/docs`** on `main` if you want `https://<user>.github.io/leaderkey/`.

## Development

```bash
python3 -m unittest discover -s tests -v
```

### Roadmap (slices)

1. **Done** — Rules, docs, examples, CI, Glass-style README and Pages shell.
2. **Next** — Scripted install/backup/Nix/XDG/Cursor CLI flows **after** dedicated research (see `scripts/README.md`).
3. **Your input** — Fill in [docs/ux-research.md](docs/ux-research.md) when you have study notes.

## License

MIT — see [LICENSE](LICENSE). Upstream Leader Key remains under its own license; the default JSON excerpt is credited in the user guide.

# Leader Key · Cursor harness (macOS)

[![CI](https://github.com/shahzebqazi/ai-agent-leaderkey/actions/workflows/ci.yml/badge.svg)](https://github.com/shahzebqazi/ai-agent-leaderkey/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Executive summary

- **Validated JSON** — Examples and a **recommended root template** are checked in CI for structure and duplicate keys per group (aligned with Leader Key’s rules).
- **Scripts** — Backup, restore, and `leaderkey://` helpers for macOS (`scripts/`); run via `python3 scripts/...` from the repo root (see [user guide](docs/user-guide.md)).
- **Documented conflicts** — Common macOS chords used by command actions are noted in [hotkey-conflicts.md](docs/hotkey-conflicts.md).
- **Cursor Glass–aligned docs** — Short, scannable guides. Works with Cursor **3+** and the **Agent Window**.

**[Leader Key](https://github.com/mikker/LeaderKey)** is a menu bar app for leader-style shortcuts. This repo ships **rules**, **examples**, **tests**, and **scripts**—not the Leader Key app binary.

**GitHub:** [`shahzebqazi/ai-agent-leaderkey`](https://github.com/shahzebqazi/ai-agent-leaderkey). After a rename/move, set `git remote set-url origin` to this URL if needed.

## Quick links

| Resource | Description |
|----------|-------------|
| [User guide](docs/user-guide.md) | Install, config paths, scripts, backups |
| [Hotkey conflicts](docs/hotkey-conflicts.md) | macOS shortcuts that overlap with template patterns |
| [UX research](docs/ux-research.md) | Scope, Shortcuts comparison, future uses |
| [Paper (draft)](docs/paper-leader-key-hotkeys.md) | Omarchy, RTS, ergonomics, mnemonic map |
| [Scripts](scripts/README.md) | Backup, restore, `leaderkey_open` |

## Examples

| File | Role |
|------|------|
| [examples/config.default.from-upstream.json](examples/config.default.from-upstream.json) | **Upstream default** from Leader Key’s `defaultConfig` |
| [config/templates/recommended-root.template.json](config/templates/recommended-root.template.json) | **Sanitized template** — edit before use |

## GitHub Pages

Static showcase: **[docs/index.html](docs/index.html)** — enable **Pages** → branch **`main`** → folder **`/docs`** for `https://shahzebqazi.github.io/ai-agent-leaderkey/`.

## Development

```bash
python3 -m unittest discover -s tests -v
```

### Roadmap

1. **Done** — Rules, docs, examples, CI, scripts (backup/restore/open), tests.
2. **Deferred** — Nix/XDG/xonsh/Cursor CLI apply-config (see [scripts/README.md](scripts/README.md)).
3. **Closing a milestone** — Follow [docs/milestone-review.md](docs/milestone-review.md): review live config, sanitize `config/templates/recommended-root.template.json`, run tests, approve, push.

## License

MIT — see [LICENSE](LICENSE). Upstream Leader Key remains under its own license.

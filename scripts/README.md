# Scripts

| Script | Purpose |
|--------|---------|
| `leaderkey_backup.py` | Copy `config.json` to `--dest` with a UTC timestamp (macOS only). |
| `leaderkey_restore.py` | Restore from a backup JSON; requires `--force` if destination exists. |
| `leaderkey_open.py` | `reveal` \| `reload` \| `settings` → `open leaderkey://…` |

Run with `python3 scripts/<name>.py` from the repo root. See [docs/user-guide.md](../docs/user-guide.md).

**Deferred (separate spec):** Nix/Homebrew wrappers, XDG-style notes, xonsh aliases, Cursor CLI apply-config flows.

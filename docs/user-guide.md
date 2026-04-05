# Leader Key user guide

This repository helps you manage **[Leader Key](https://github.com/mikker/LeaderKey)** configurations with **validated examples**, **hotkey conflict notes**, and **Cursor** rules tuned for macOS.

## What you get here

- **Upstream default** — `examples/config.default.from-upstream.json` matches the app’s built-in starter (from the Leader Key source tree).
- **Recommended template** — `config/templates/recommended-root.template.json` is a **sanitized, generic** layout. Edit paths and labels for your machine.
- **Checks** — automated tests ensure JSON shape and **no duplicate keys** within each group.

## Install Leader Key

- **Homebrew**: `brew install leader-key`
- **Releases**: [GitHub Releases](https://github.com/mikker/LeaderKey/releases)

After install, grant **Accessibility** and, if prompted, **Input Monitoring** under **System Settings → Privacy & Security**.

## Where the config lives

- Reveal in Finder: `open "leaderkey://config-reveal"`
- Typical path: `~/Library/Application Support/Leader Key/config.json`

Always **back up** before replacing `config.json`.

## Scripts (macOS)

From the repository root, using the **integrated terminal** (no `PATH` changes required if you invoke Python by path or `python3`):

```bash
# Back up live config to ./backups/config-<UTC-timestamp>.json
python3 scripts/leaderkey_backup.py --dest backups

# Optional: explicit config path
python3 scripts/leaderkey_backup.py --dest backups --config "$HOME/Library/Application Support/Leader Key/config.json"
```

```bash
# Restore from a backup (refuses if destination exists unless --force)
python3 scripts/leaderkey_restore.py backups/config-20260101-120000.json --force
```

```bash
# Open Leader Key URL schemes (Finder reveal, reload, settings)
python3 scripts/leaderkey_open.py reveal
python3 scripts/leaderkey_open.py reload
python3 scripts/leaderkey_open.py settings
```

Scripts check **`sys.platform == "darwin"`**; on other OSes they exit with an error.

## Using the template

1. Copy `config/templates/recommended-root.template.json` or merge sections in the app.
2. Replace placeholder paths (terminal app, profiles, `~/Developer`, DAW paths).
3. Reload: `python3 scripts/leaderkey_open.py reload` or `open "leaderkey://config-reload"`.

See [hotkey-conflicts.md](hotkey-conflicts.md) before assigning keys that mirror system shortcuts.

## Backups

- Use `leaderkey_backup.py` or copy `config.json` to private storage.
- For sharing publicly, remove machine-specific paths and internal hostnames.

## Cursor

Open this repository in **Cursor 3+** so `.cursor/rules/` apply. Use the **Agent Window** for multi-step edits.

**Typical agent workflow:** Ask the agent to change your **local** `config.json` (reveal with `open "leaderkey://config-reveal"`), reload Leader Key, and try the new bindings. When you are happy with behavior, have the agent (or you) mirror a **sanitized** subset into `config/templates/recommended-root.template.json` if you want it on GitHub, run `python3 -m unittest discover -s tests -v`, then commit and push. Never publish machine-specific paths or secrets in the template.

## Further reading

- [Hotkey conflicts](hotkey-conflicts.md)
- [UX research](ux-research.md)

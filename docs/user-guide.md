# Leader Key user guide

This repository helps you manage **[Leader Key](https://github.com/mikker/LeaderKey)** configurations with **validated examples**, **hotkey conflict notes**, and **Cursor** rules tuned for macOS.

## What you get here

- **Upstream default** — `examples/config.default.from-upstream.json` matches the app’s built-in starter (from the Leader Key source tree).
- **Recommended template** — `config/templates/recommended-root.template.json` is a **sanitized, generic** layout derived from a real-world root config (machine-specific paths and one licensed app path were generalized). Paths and labels are placeholders you should edit for your machine.
- **Checks** — automated tests ensure JSON shape and **no duplicate keys** within each group (aligned with Leader Key’s validator behavior).

## Install Leader Key

- **Homebrew**: `brew install leader-key`
- **Releases**: [GitHub Releases](https://github.com/mikker/LeaderKey/releases)

After install, grant **Accessibility** and, if prompted, **Input Monitoring** under **System Settings → Privacy & Security**.

## Where the config lives

- Reveal in Finder: `open "leaderkey://config-reveal"`
- Typical path: `~/Library/Application Support/Leader Key/config.json`

Always **back up** before replacing `config.json`.

## Using the template

1. Copy `config/templates/recommended-root.template.json` to a safe path or merge sections into your existing config in the app.
2. Replace placeholder paths (for example `~/Developer/dotfiles`, terminal app name, and third-party apps).
3. Reload: `open "leaderkey://config-reload"` or use the in-app reload control.

See [hotkey-conflicts.md](hotkey-conflicts.md) before assigning keys that mirror system shortcuts.

## Backups

- Export or copy `config.json` to a private git repo, encrypted storage, or dated files outside the app bundle.
- For sharing publicly, remove machine-specific paths, account names, and internal hostnames.

## Cursor

Open this repository in **Cursor 3+** so `.cursor/rules/` apply. Use the **Agent Window** for multi-step edits while keeping your config under version control.

## Further reading

- [Hotkey conflicts](hotkey-conflicts.md) — macOS shortcuts that overlap with common Leader Key patterns.
- [UX research (outline)](ux-research.md) — fill in with your own notes.

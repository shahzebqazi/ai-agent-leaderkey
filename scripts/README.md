# Scripts

This folder is reserved for **automation** (install, backup, sync, Nix, XDG-style layout, Cursor CLI integration).

## Status

Nothing here is implemented yet. The project is using **documented examples**, **tests**, and **manual workflows** first.

## When to build scripts

When you are ready, ask to implement scripts in small slices. Good candidates (after research):

- Guarded entry points (fail fast on wrong OS or missing Leader Key).
- Optional **xonsh** aliases that wrap safe operations.
- Backup / restore of `config.json` with timestamps.
- Hooks for a **Cursor** CLI agent to apply a reviewed config.

Until then, use the [user guide](../docs/user-guide.md) and URL schemes such as `leaderkey://config-reveal` and `leaderkey://config-reload`.

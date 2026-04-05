## Learned User Preferences

- Prefer human-facing documentation written for readers, not as logs of agent reasoning or internal work steps.
- Scaffold new users toward confident, power-user-style Leader Key workflows using this repository’s Cursor rules and guides.
- **Agent workflow:** When asked to change the map, apply edits to the **live Leader Key config** on disk first (typically `~/Library/Application Support/Leader Key/config.json`), reload in the app, and confirm behavior. **Only after it works**, promote changes to the repo: run tests, update the **sanitized** `config/templates/recommended-root.template.json` if sharing publicly, then commit and push to GitHub.

## Learned Workspace Facts

- This repository is a Cursor-oriented harness for Leader Key on macOS: configuration, installation, troubleshooting, and safe export or sharing of configs.
- Cursor rules live under `.cursor/rules/`; use `leader-key-macos.mdc` for Leader Key behavior and macOS troubleshooting, and `cursor-glass.mdc` for documentation tone and GitHub Pages style.
- Human guides live in `docs/`; run `python -m unittest discover -s tests -v` before pushing configuration changes.
- Example JSON and sanitized templates live under `examples/` and `config/templates/`.
- GitHub remote for this project: **`shahzebqazi/ai-agent-leaderkey`**.

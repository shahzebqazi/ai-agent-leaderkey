# Milestone review (Slice 5)

Before you tag a release or call the harness “done” for a milestone:

1. **Review your live config** — `open "leaderkey://config-reveal"` or open `~/Library/Application Support/Leader Key/config.json`. Confirm keys, labels, and paths you are willing to share.
2. **Update the public template** — Edit `config/templates/recommended-root.template.json` with **sanitized** paths (placeholders like `~/Developer/dotfiles`, generic app names). Remove secrets and internal hostnames.
3. **Validate** — From the repo root: `python3 -m unittest discover -s tests -v`
4. **Commit and push** — After you approve the diff, push to `main` on **`shahzebqazi/ai-agent-leaderkey`** (or your fork).

If your personal map is too sensitive, ship a **minimal** launch-only subset in the template and keep your full map local.

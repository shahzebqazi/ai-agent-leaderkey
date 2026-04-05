#!/usr/bin/env python3
"""Open Leader Key URL schemes via macOS `open` (reveal, reload, settings)."""

from __future__ import annotations

import argparse
import subprocess
import sys


URLS = {
    "reveal": "leaderkey://config-reveal",
    "reload": "leaderkey://config-reload",
    "settings": "leaderkey://settings",
}


def run_open(subcommand: str) -> None:
    if sys.platform != "darwin":
        raise OSError("leaderkey-open: requires macOS")
    url = URLS.get(subcommand)
    if not url:
        raise ValueError(f"unknown subcommand: {subcommand}")
    subprocess.run(["open", url], check=True)


def main() -> None:
    p = argparse.ArgumentParser(description="Open Leader Key URL schemes")
    p.add_argument(
        "command",
        choices=list(URLS.keys()),
        help="reveal (Finder), reload config, or open settings",
    )
    args = p.parse_args()
    try:
        run_open(args.command)
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
    except subprocess.CalledProcessError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

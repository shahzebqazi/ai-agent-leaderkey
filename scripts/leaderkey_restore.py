#!/usr/bin/env python3
"""Restore Leader Key config.json from a backup file (macOS only)."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def default_config_path() -> Path:
    return Path.home() / "Library/Application Support/Leader Key/config.json"


def run_restore(
    backup_file: Path,
    *,
    force: bool,
    config_path: Path | None = None,
) -> Path:
    if sys.platform != "darwin":
        raise OSError("leaderkey-restore: requires macOS")
    if not backup_file.is_file():
        raise FileNotFoundError(f"backup not found: {backup_file}")
    dest = config_path or default_config_path()
    if dest.exists() and not force:
        raise FileExistsError(
            f"refusing to overwrite {dest} without --force (backup current config first)"
        )
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(backup_file, dest)
    return dest


def main() -> None:
    p = argparse.ArgumentParser(description="Restore Leader Key config from a backup JSON file")
    p.add_argument("backup", type=Path, help="Path to a backed-up config JSON")
    p.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing config.json without prompting",
    )
    p.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Override destination config path",
    )
    args = p.parse_args()
    try:
        out = run_restore(args.backup, force=args.force, config_path=args.config)
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except FileExistsError as e:
        print(e, file=sys.stderr)
        sys.exit(3)
    print(out)


if __name__ == "__main__":
    main()

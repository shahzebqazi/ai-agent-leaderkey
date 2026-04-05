#!/usr/bin/env python3
"""Back up Leader Key config.json to a timestamped file (macOS only)."""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def default_config_path() -> Path:
    return Path.home() / "Library/Application Support/Leader Key/config.json"


def copy_config_to_backup(config_path: Path, dest_dir: Path) -> Path:
    """Copy config to dest_dir/config-YYYYMMDD-HHMMSS.json. Does not check OS."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out = dest_dir / f"config-{ts}.json"
    shutil.copy2(config_path, out)
    return out


def run_backup(dest_dir: Path, config_path: Path | None = None) -> Path:
    if sys.platform != "darwin":
        raise OSError("leaderkey-backup: requires macOS")
    src = config_path or default_config_path()
    if not src.is_file():
        raise FileNotFoundError(f"config not found: {src}")
    return copy_config_to_backup(src, dest_dir)


def main() -> None:
    p = argparse.ArgumentParser(description="Back up Leader Key config.json")
    p.add_argument(
        "--dest",
        type=Path,
        default=Path("backups"),
        help="Directory for timestamped backups (created if missing)",
    )
    p.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Override path to config.json (default: Application Support)",
    )
    args = p.parse_args()
    try:
        out = run_backup(args.dest, args.config)
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    print(out)


if __name__ == "__main__":
    main()

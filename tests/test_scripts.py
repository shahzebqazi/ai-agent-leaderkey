"""Tests for scripts/leaderkey_*.py (portable logic + platform guards)."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class TestBackupCore(unittest.TestCase):
    def test_copy_config_to_backup_creates_timestamped_file(self) -> None:
        from scripts.leaderkey_backup import copy_config_to_backup

        with tempfile.TemporaryDirectory() as raw:
            td = Path(raw)
            cfg = td / "config.json"
            cfg.write_text('{"type":"group","actions":[]}', encoding="utf-8")
            dest = td / "out"
            out = copy_config_to_backup(cfg, dest)
            self.assertTrue(out.is_file())
            self.assertEqual(out.read_text(encoding="utf-8"), cfg.read_text(encoding="utf-8"))
            self.assertTrue(out.name.startswith("config-"))


class TestBackupRun(unittest.TestCase):
    def test_run_backup_requires_darwin(self) -> None:
        from scripts.leaderkey_backup import run_backup

        if sys.platform == "darwin":
            self.skipTest("use mocked test on macOS")
        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaises(OSError):
                run_backup(Path(raw) / "b")

    @mock.patch("scripts.leaderkey_backup.sys.platform", "darwin")
    def test_run_backup_mocked_darwin(self) -> None:
        from scripts.leaderkey_backup import run_backup

        with tempfile.TemporaryDirectory() as raw:
            td = Path(raw)
            support = td / "Library/Application Support/Leader Key"
            support.mkdir(parents=True)
            cfg = support / "config.json"
            cfg.write_text('{"type":"group","actions":[]}', encoding="utf-8")
            with mock.patch("scripts.leaderkey_backup.default_config_path", return_value=cfg):
                out = run_backup(td / "backups")
            self.assertTrue(out.is_file())


class TestRestoreRun(unittest.TestCase):
    @mock.patch("scripts.leaderkey_restore.sys.platform", "darwin")
    def test_run_restore_refuses_without_force_if_exists(self) -> None:
        from scripts.leaderkey_restore import run_restore

        with tempfile.TemporaryDirectory() as raw:
            td = Path(raw)
            dest = td / "Library/Application Support/Leader Key/config.json"
            dest.parent.mkdir(parents=True)
            dest.write_text("{}", encoding="utf-8")
            bak = td / "bak.json"
            bak.write_text('{"type":"group","actions":[]}', encoding="utf-8")
            with mock.patch("scripts.leaderkey_restore.default_config_path", return_value=dest):
                with self.assertRaises(FileExistsError):
                    run_restore(bak, force=False)


class TestLeaderkeyOpen(unittest.TestCase):
    @mock.patch("scripts.leaderkey_open.subprocess.run")
    @mock.patch("scripts.leaderkey_open.sys.platform", "darwin")
    def test_run_open_reveal(self, mock_run: mock.MagicMock) -> None:
        from scripts.leaderkey_open import run_open

        run_open("reveal")
        mock_run.assert_called_once_with(
            ["open", "leaderkey://config-reveal"], check=True
        )


if __name__ == "__main__":
    unittest.main()

"""Validate Leader Key JSON examples: structure, duplicate keys per group, action types."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_TYPES = frozenset({"group", "application", "url", "command", "folder"})


def load_json(rel: str) -> dict:
    path = ROOT / rel
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_group(group: dict, path: str, *, is_root: bool) -> list[str]:
    errors: list[str] = []
    if group.get("type") != "group":
        errors.append(f"{path}: root must have type 'group'")
        return errors

    actions = group.get("actions")
    if not isinstance(actions, list):
        errors.append(f"{path}: 'actions' must be a list")
        return errors

    keys_seen: dict[str, int] = {}
    for i, item in enumerate(actions):
        p = f"{path}.actions[{i}]"
        t = item.get("type")
        if t not in VALID_TYPES:
            errors.append(f"{p}: invalid type {t!r}")
            continue
        if t == "group":
            errors.extend(validate_group(item, p, is_root=False))
            key = item.get("key")
        else:
            key = item.get("key")
            if "value" not in item or not isinstance(item["value"], str):
                errors.append(f"{p}: action needs string 'value'")

        if key is not None and key != "":
            if key in keys_seen:
                errors.append(
                    f"{path}: duplicate key {key!r} (indices {keys_seen[key]} and {i})"
                )
            else:
                keys_seen[key] = i
            if len(key) != 1:
                errors.append(f"{p}: key should be a single character, got {key!r}")

    if not is_root and "key" in group:
        k = group.get("key")
        if k is not None and k != "" and len(k) != 1:
            errors.append(f"{path}: group key should be a single character, got {k!r}")

    return errors


def validate_root(doc: dict) -> list[str]:
    return validate_group(doc, "root", is_root=True)


class TestConfigExamples(unittest.TestCase):
    def test_upstream_default_example(self) -> None:
        doc = load_json("examples/config.default.from-upstream.json")
        err = validate_root(doc)
        self.assertEqual(err, [], msg="; ".join(err))

    def test_recommended_template(self) -> None:
        doc = load_json("config/templates/recommended-root.template.json")
        err = validate_root(doc)
        self.assertEqual(err, [], msg="; ".join(err))


if __name__ == "__main__":
    unittest.main()

# Hotkey conflicts (macOS)

Leader Key runs **after** the OS and other tools see keyboard input. If a shortcut “does nothing,” check these layers before changing your leader map.

## System shortcuts referenced by this repo’s template

The recommended template includes **command actions** that synthesize these macOS shortcuts:

| Pattern | Default macOS role | Notes |
|--------|---------------------|--------|
| **⌘`** (Command + backtick) | Cycle windows of the front app | Common in multi-window apps. |
| **⌃⌘Space** (Control + Command + Space) | Character Viewer / Emoji & Symbols | Widely used; reassignment in **Keyboard** settings affects behavior. |
| **⌘⌥D** (Command + Option + D) | Show / hide Dock | Can conflict if you rely on the same chord elsewhere. |

If you remap these in **System Settings → Keyboard → Keyboard Shortcuts**, test your Leader Key actions after changes.

## Other common conflicts

- **Function keys** — media keys, Spotlight, or app-specific bindings.
- **⌘Space** — Spotlight or Input Sources; often used as a **leader** elsewhere.
- **Third-party tools** — Karabiner-Elements, BetterTouchTool, Raycast, and browser extensions can consume keys before Leader Key sees them.

## Practical checks

1. In **System Settings → Keyboard**, review **Keyboard Shortcuts** for services that might steal a chord.
2. Temporarily disable other global launchers to see if the leader fires reliably.
3. Prefer **single-character keys** inside groups; validate in the Leader Key UI to catch duplicate bindings within a group.

Research for automation (scripts, Nix, XDG-style paths) is tracked separately; this document stays limited to **documented** system behaviors and the template’s explicit chords.

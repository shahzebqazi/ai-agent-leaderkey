# UX research

**Position paper:** [paper-leader-key-hotkeys.md](paper-leader-key-hotkeys.md) — thesis, Omarchy / RTS framing, ergonomics citations, mnemonic map.

This document captures **scope**, **user assumptions**, and **research directions** for this harness. It complements the paper and [user-guide.md](user-guide.md).

---

## Prompts (answered)

### 1. Who is the primary user?

**Everyone** who wants a keyboard-native launcher habit. **New users** are scaffolded toward power use by a **bundled Cursor agent** (rules and docs in this repo)—not by requiring prior shortcut expertise.

### 2. What is the job-to-be-done?

For the **first release**, the harness targets **app launching only**. Users are **encouraged to contribute** bindings, docs, and ideas for **window management, media, scripting**, and other jobs in later work.

### 3. Where does Leader Key break down?

- **No established cross-app standard** for a leader-style map on macOS.
- **Bleeding edge**: OS updates, permissions (Accessibility, Input Monitoring), and third-party tools can change behavior.
- **Gaps in Apple’s HCI story** for user-owned, **version-controlled** keyboard surfaces versus Spotlight-centric discovery.
- **Small toolkit without vendor docs**: users assemble Terminal, browser, editor, DAW, etc., and must **self-document** conflicts and backups.

### 4. When do you reach for Leader Key vs Spotlight, Raycast, or the Dock?

**For now:** **Leader Key for launching apps** (deterministic, mnemonic chords). **Spotlight / Raycast** remain useful for **search**, **calculations**, and **one-off** retrieval. **Dock** for mouse-driven switching. This division may evolve as the map grows.

---

## Leader Key vs macOS Shortcuts

| | **Leader Key** | **Shortcuts** |
|---|----------------|---------------|
| **Interaction** | **Keyboard-first**: leader chord → sequence → action (optional **groups**). | **Flow-based**: build automations; run from app, Siri, Focus, time, widgets, etc. |
| **Mental model** | **Routing** — same path → same outcome; minimal search. | **Conditionals** — branches, variables, “if,” deep **system** actions. |
| **Config** | **JSON** in one tree; **git-friendly** diffs. | **Library** of shortcuts; sharing as files; different editing model. |
| **Triggers** | Mostly **keyboard** + **`leaderkey://`** URL schemes from scripts. | **Many** trigger types (schedule, location, Focus, …). |
| **Best for** | **Muscle memory**, **nested** menus, **shell** / **URL** / **folder** in one map. | **Scheduled** and **event-driven** automation, **visual** authoring. |

**They are complementary, not substitutes.** Leader Key does **not** replace Shortcuts’ **trigger ecosystem**. You can still **invoke** a Shortcut from a Leader Key **`command`** action (e.g. `shortcuts run "Name"`) so the leader becomes a **keyboard front-end** and Shortcuts remains the **engine** for heavier workflows.

---

## Terminology: “combo”

Binding **many apps** to **one physical button** alone is **not** how Leader Key works. You use a **leader chord** (mode), then **one key per action** (a **sequence**). That is **chord + sequence**, not “one button launches ten apps simultaneously.” In RTS terms it is closer to **menu depth** than a single **combo** keypress.

---

## Profiles (multi-config)

**Assumption for research:** **One user → one primary profile** (one canonical `config.json` per machine) is enough for most people. **Named profiles** (work vs home, teaching demos) are a **possible future** affordance—not required for v1. Document **export/backup** so users can **clone** configs without formal profile UI.

---

## Future uses (beyond app launch)

These use **existing** Leader Key action types (`application`, `url`, `command`, `folder`, `group`). They are **research / roadmap** items, not all in scope for the first release.

1. **URLs and deep links** — `url` actions for `https://…`, `obsidian://…`, `raycast://…`, so the leader opens **targets inside** apps, not only `.app` bundles.
2. **Folders and project roots** — `folder` for repos, scratch, renders; macOS favorites do not give the same **keyboard-first, labeled tree**.
3. **Scripts and hooks** — `command` for shell, `osascript`, or `shortcuts run`; **`leaderkey://config-reload`** after git pull or deploy. Requires sane **PATH** in non-interactive shells (see Leader Key FAQ).
4. **Settings / utilities subtree** — a **group** (e.g. under `u`) for **infrequent** utilities (Disk Utility, Activity Monitor, specific Settings panes via stable links or scripts) without burning **global** shortcuts.
5. **Accessibility** — **Alternate layouts** (Dvorak, Colemak): keys are **logical**; verify what Leader Key receives after layout/OS updates. **Macro pads / foot pedals / one-handed keyboards**: dedicate a **comfortable** leader key to reduce stretch; test with **Sticky Keys** and remappers (Karabiner) if needed.

---

## Your notes

*(Dated studies, interviews, or metrics go here.)*

---

## See also

- [hotkey-conflicts.md](hotkey-conflicts.md)
- [user-guide.md](user-guide.md)

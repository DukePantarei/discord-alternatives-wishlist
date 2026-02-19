#!/usr/bin/env python3
"""
generate_table.py

Reads platforms.json and generates COMPARISON.md.

One table per platform category.
Platforms are ROWS, features are COLUMNS.

Usage:
    python generate_table.py
"""

import json
from pathlib import Path
from collections import defaultdict

INPUT_FILE  = Path("platforms.json")
OUTPUT_FILE = Path("COMPARISON.md")

EMOJI_MAP = {
    "yes":     "✅",
    "no":      "❌",
    "partial": "⚠️",
    "planned": "🗓️",
    "unknown": "❓",
}

CATEGORY_DESCRIPTIONS = {
    "Matrix Clients": (
        "All Matrix clients share the same underlying protocol: federated, "
        "decentralized, and E2EE by default (must be enabled by the client). The differences below are client-level "
        "only. All of them can communicate with each other and with any Matrix homeserver.\n\n"
        "> 💡 A homeserver is required. You can use the free [matrix.org](https://matrix.org) "
        "server or self-host using "
        "[matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy)."
    ),
    "Privacy-Focused Centralized": (
        "These platforms prioritize privacy and are open source, but run on a central server. "
        "Self-hosted instances exist but **cannot communicate with each other**"
        "they are isolated, not federated."
    ),
    "Self-Hosted Platforms": (
        "Designed primarily for self-hosting. Most require technical knowledge to deploy. "
        "None of these federate with each other."
    ),
    "Commercial Alternatives": (
        "Polished commercial products, included for completeness. "
        "Privacy policies and long-term direction may change. "
        "Discord is included here as the baseline for comparison."
    ),
    "Legacy & Niche": (
        "Included for historical context or specific use cases. "
        "Generally not recommended as full Discord replacements for casual communities."
    ),
}

def render_value(value: str) -> str:
    return EMOJI_MAP.get(value.lower(), "❓")

def slugify(text: str) -> str:
    """Convert a category name to a GitHub markdown anchor."""
    return text.lower().replace(" ", "-").replace("&", "").replace("--", "-").strip("-")

def build_category_table(platforms: list, features: list) -> list:
    """
    Build one markdown table for a single category.
    Rows = platforms, columns = features.
    Returns a list of lines.
    """
    lines = []

    # Column headers — Platform name only, then one column per feature
    feature_labels = [f["label"] for f in features]
    header_cells   = ["**Platform**"] + [f"**{lbl}**" for lbl in feature_labels]
    separator      = ["---"] * len(header_cells)

    lines.append("| " + " | ".join(header_cells) + " |")
    lines.append("| " + " | ".join(separator)     + " |")

    # One row per platform
    for p in platforms:
        name_cell = f"[{p['name']}]({p['url']})"

        feature_cells = []
        for f in features:
            fkey  = f["key"]
            raw   = p["features"].get(fkey, "unknown")
            emoji = render_value(raw)
            note  = p.get("feature_notes", {}).get(fkey, "")
            if note:
                emoji += " †"
            feature_cells.append(emoji)

        all_cells = [name_cell] + feature_cells
        lines.append("| " + " | ".join(all_cells) + " |")

    return lines


def build_notes_for_category(platforms: list) -> list:
    """Build the notes block for a single category's platforms.
    Includes Description and Architecture for every platform,
    plus any feature_notes entries marked with †.
    """
    lines = []
    header_printed = False

    for p in platforms:
        desc  = p.get("description", "")
        arch  = p.get("architecture", "")
        notes = p.get("feature_notes", {})

        # Every platform gets a notes entry (for description + architecture)
        if not header_printed:
            lines.append("**† Notes**")
            lines.append("")
            header_printed = True

        lines.append("<details>")
        
        lines.append(f"<summary>{p['name']}</summary>")
        lines.append("")

        if desc:
            lines.append(f"- *Description:* {desc}")
        if arch:
            lines.append(f"- *Architecture:* {arch}")
        for fkey, note_text in notes.items():
            label = fkey.replace("_", " ").title()
            lines.append(f"- *{label}:* {note_text}")
        lines.append("</details>")
        lines.append("")

    return lines


def build_toc(categories: list, grouped: dict) -> list:
    """Build a table of contents linking to each category section."""
    lines = ["## Contents", ""]
    for category in categories:
        if not grouped.get(category):
            continue
        anchor = slugify(category)
        count  = len(grouped[category])
        lines.append(f"- [{category}](#{anchor}) — {count} platform{'s' if count != 1 else ''}")
    lines.append("")
    return lines


def main():
    data       = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    features   = data["features"]
    platforms  = data["platforms"]
    categories = data["categories"]

    grouped = defaultdict(list)
    for p in platforms:
        grouped[p["category"]].append(p)

    lines = []

    # ── File header ──────────────────────────────────────────────────────────
    lines += [
        "# Platform Comparison",
        "",
        "> **Auto-generated from `platforms.json`** do not edit this file directly.",
        "> To update, edit `platforms.json` and re-run `python generate_table.py`",
        "> (or push to main, the GitHub Action will regenerate it automatically).",
        "",
    ]

    # ── Legend ───────────────────────────────────────────────────────────────
    lines += [
        "## Legend",
        "",
        "| Symbol | Meaning |",
        "|---|---|",
        "| ✅ | Fully supported |",
        "| ⚠️ | Partial / limited |",
        "| 🗓️ | Planned |",
        "| ❌ | Not supported |",
        "| ❓ | Unknown |",
        "| † | See notes below the table |",
        "",
    ]

    # ── Table of contents ────────────────────────────────────────────────────
    lines += build_toc(categories, grouped)

    # ── One section per category ─────────────────────────────────────────────
    for category in categories:
        cat_platforms = grouped.get(category, [])
        if not cat_platforms:
            continue

        lines += [
            "---",
            "",
            f"## {category}",
            "",
        ]

        # Category description
        desc = CATEGORY_DESCRIPTIONS.get(category)
        if desc:
            lines.append(desc)
            lines.append("")

        # The table
        lines += build_category_table(cat_platforms, features)
        lines.append("")

        # Notes for this category
        notes = build_notes_for_category(cat_platforms)
        if notes:
            lines += notes

    # ── Footer ────────────────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## Contributing",
        "",
        "See an error or missing platform? Edit `platforms.json` and open a Pull Request.",
        "See [contributing.md](contributing.md) for guidelines.",
        "",
    ]

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"✅ Generated {OUTPUT_FILE} — "
        f"{len(platforms)} platforms across {len(categories)} categories "
        f"with {len(features)} features each."
    )

if __name__ == "__main__":
    main()

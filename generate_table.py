#!/usr/bin/env python3
"""
generate_table.py

Reads platforms.json and generates COMPARISON.md with GROUPED HEADERS.

Features are organized into logical groups with visual separation.
Platforms are ROWS, features are COLUMNS grouped by category.

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

# Define feature groups for organized display
FEATURE_GROUPS = {
    "Privacy & Licensing": [
        "open_source",
        "self_hostable",
        "federated",
        "e2e_encryption",
        "no_ads",
        "no_data_tracking",
        "gdpr_compliant",
        "biometric_age_verification",
        "message_ttl",
    ],
    "Pricing & Licensing": [
        "free_to_use",
        "no_premium_tier",
        "self_hosting_license",
        "freemium_limitations",
        "enterprise_tier",
    ],
    "Platform Support": [
        "web_app",
        "desktop_app",
        "mobile_app",
        "docker_install",
        "mobile_hosting",
    ],
    "Communication": [
        "voice_chat",
        "video_chat",
        "screen_sharing",
        "system_audio_sharing",
        "text_channels",
        "file_sharing",
        "gif_embed_support",
        "threads_forums",
        "persistent_voice_channels",
        "per_user_audio_output",
    ],
    "Server & Admin": [
        "role_management",
        "server_organization",
        "admin_gui",
        "large_community_moderation",
        "invite_links_guest_access",
        "migration_assistant",
        "bridges",
        "discord_api_compatible",
        "community_discovery",
    ],
    "Channels & Content": [
        "docs_wiki_channels",
        "list_task_channels",
        "media_gallery_channels",
        "scheduled_announcements",
        "event_scheduling",
    ],
    "Community Tools": [
        "bots_automation",
        "webhooks",
        "raid_planner",
        "tournament_brackets",
        "rich_calendar_tools",
    ],
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
        "Self-hosted instances exist but **cannot communicate with each other** — "
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
    "Discontinued": (
        "Platforms that are no longer active. Included for historical reference and "
        "feature comparison to show what was possible in the past."
    ),
    "Business Productivity": (
        "Team collaboration tools designed for businesses. NOT Discord alternatives — "
        "included for completeness as they appear in comparison lists."
    ),
}

def render_value(value: str) -> str:
    return EMOJI_MAP.get(value.lower(), "❓")

def slugify(text: str) -> str:
    """Convert a category name to a GitHub markdown anchor."""
    return text.lower().replace(" ", "-").replace("&", "").replace("--", "-").strip("-")

def humanize(key: str) -> str:
    """Convert snake_case to Title Case."""
    return key.replace("_", " ").title()

def build_category_table_grouped(platforms: list, features: list) -> list:
    """
    Build SEPARATE tables for each feature group.
    This avoids horizontal scrolling issues with one massive table.
    Returns a list of lines.
    """
    lines = []
    
    # Build feature lookup by key for getting labels
    feature_lookup = {f["key"]: f["label"] for f in features}
    
    # Create one table per feature group
    for group_name, feature_keys in FEATURE_GROUPS.items():
        # Group header
        lines.append(f"### {group_name}")
        lines.append("")
        
        # Table header
        feature_labels = [feature_lookup.get(fkey, humanize(fkey)) for fkey in feature_keys]
        header = ["**Platform**"] + [f"**{lbl}**" for lbl in feature_labels]
        separator = ["---"] * len(header)
        
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(separator) + " |")
        
        # Data rows
        for p in platforms:
            row = [f"[{p['name']}]({p['url']})"]
            
            for fkey in feature_keys:
                raw = p["features"].get(fkey, "unknown")
                emoji = render_value(raw)
                note = p.get("feature_notes", {}).get(fkey, "")
                if note:
                    emoji += " †"
                row.append(emoji)
            
            lines.append("| " + " | ".join(row) + " |")
        
        lines.append("")  # Blank line between tables
    
    return lines

def build_notes_for_category(platforms: list) -> list:
    """Build the notes block for a single category's platforms.
    Includes Description and Architecture for every platform,
    plus any feature_notes entries marked with †.
    Uses collapsible <details> sections for clean presentation.
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
            label = humanize(fkey)
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
        "> **Auto-generated from `platforms.json`** — do not edit this file directly.",
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

        # The table with GROUPED HEADERS
        lines += build_category_table_grouped(cat_platforms, features)
        lines.append("")

        # Notes for this category (collapsible sections)
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
    
    # Build feature count from groups
    feature_count = sum(len(features) for features in FEATURE_GROUPS.values())
    
    print(
        f"✅ Generated {OUTPUT_FILE} — "
        f"{len(platforms)} platforms across {len(categories)} categories "
        f"with {feature_count} grouped features."
    )

if __name__ == "__main__":
    main()

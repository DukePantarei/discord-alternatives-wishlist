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
        "ai_features_or_training",
        "ai_generated_codebase",
    ],
    "Pricing": [
        "free_to_use",
        "no_premium_tier",
        "self_hosting_license",
        "freemium_limitations",
        "enterprise_tier",
        "hardware_required_for_use",
    ],
    "Platform Support": [
        "web_app",
        "windows_app",
        "macos_app",
        "linux_app",
        "android_app",
        "ios_app",
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
    "Moderation & Safety": [
        "large_community_moderation",
        "automod",
        "audit_logs",
        "user_timeout_mute",
        "raid_protection",
        "message_reporting",
        "age_verification",
        "id_verification",
    ],
    "Server & Admin": [
        "role_management",
        "server_organization",
        "admin_gui",
        "invite_links_guest_access",
        "migration_assistant",
        "bridges",
        "discord_api_compatible",
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
        "community_discovery",
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
    # GitHub converts "Legacy & Niche" to "legacy--niche" (& becomes --, spaces become -)
    # So we need to match that behavior
    return text.lower().replace(" & ", "--").replace(" ", "-").strip("-")

def humanize(key: str) -> str:
    """Convert snake_case to Title Case."""
    return key.replace("_", " ").title()

def build_category_table_grouped(platforms: list, features: list) -> list:
    """
    Build SEPARATE tables for each feature group.
    This avoids horizontal scrolling issues with one massive table.
    Each table is wrapped in a collapsible <details> section.
    Feature notes relevant to each group appear immediately after the table.
    Returns a list of lines.
    """
    lines = []
    
    # Build feature lookup by key for getting labels
    feature_lookup = {f["key"]: f["label"] for f in features}
    
    # Create one table per feature group
    for group_name, feature_keys in FEATURE_GROUPS.items():
        # Wrap each table in collapsible details (collapsed by default)
        lines.append("<details>")
        lines.append(f"<summary><strong>{group_name}</strong></summary>")
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
        
        lines.append("")
        
        # Add feature notes relevant to THIS group only (collapsible)
        group_notes = build_notes_for_feature_group(platforms, feature_keys)
        if group_notes:
            lines += group_notes
        
        lines.append("</details>")
        lines.append("")  # Blank line between tables
    
    return lines

def build_notes_for_feature_group(platforms: list, feature_keys: list) -> list:
    """Build notes for features in a specific feature group.
    Only includes notes for features that are in this group.
    Now wrapped in a collapsible section.
    """
    lines = []
    note_content = []
    
    for p in platforms:
        feature_notes = p.get("feature_notes", {})
        
        # Filter to only notes relevant to this feature group
        relevant_notes = {fkey: note for fkey, note in feature_notes.items() if fkey in feature_keys}
        
        if relevant_notes:
            note_content.append(f"**{p['name']}:**")
            for fkey, note_text in relevant_notes.items():
                label = humanize(fkey)
                note_content.append(f"- *{label}:* {note_text}")
            note_content.append("")
    
    # If we have notes, wrap them in collapsible section
    if note_content:
        lines.append("<details>")
        lines.append("<summary><strong>† Feature Notes</strong></summary>")
        lines.append("")
        lines += note_content
        lines.append("</details>")
        lines.append("")
    
    return lines


def build_toc(categories: list, grouped: dict) -> list:
    """Build a table of contents linking to each category section with platform lists."""
    lines = ["## Contents", ""]
    for category in categories:
        if not grouped.get(category):
            continue
        anchor = slugify(category)
        count  = len(grouped[category])
        platform_names = [p['name'] for p in grouped[category]]
        
        # Format platform list
        if count <= 5:
            # For small categories, list all platforms inline
            platform_list = ', '.join(platform_names)
            lines.append(f"- **[{category}](#{anchor})** ({count}) — {platform_list}")
        else:
            # For large categories, show first 3 + "and X more"
            shown = ', '.join(platform_names[:3])
            remaining = count - 3
            lines.append(f"- **[{category}](#{anchor})** ({count}) — {shown}, and {remaining} more")
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
        # (platform descriptions appear in first table, feature notes appear under each table)
        lines += build_category_table_grouped(cat_platforms, features)
        lines.append("")
        
        # Add back to top link for easier navigation
        lines += [
            "---",
            "",
            "[↑ Back to top](#platform-comparison)",
            "",
        ]

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

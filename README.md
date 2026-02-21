# Discord Alternatives Comparison
### A community-driven comparison of privacy-respecting, open-source chat platforms

> **Are you a Discord refugee?** In February 2026, Discord announced mandatory age verification (face scans or government ID) just 5 months after a breach exposed 70,000 IDs. This project helps you find privacy-respecting alternatives.

---

## 📖 Navigation

- **[BACKGROUND.md](BACKGROUND.md)** — Full Discord exodus story, why this matters
- **[COMPARISON.md](COMPARISON.md)** — Feature comparison table (67 platforms, 61 features)
- **[FEATURES.md](FEATURES.md)** — What features mean and how to prioritize
- **[SECURITY.md](SECURITY.md)** — ⚠️ Vibe-coded platforms, active security incidents
- **[MODERATION.md](MODERATION.md)** — Privacy-respecting vs invasive moderation

---

## 🚀 Quick Start

### If you want...

| Goal | Try | Why |
|------|-----|-----|
| **Easiest Discord transition** | Stoat or Fluxer | Most Discord-like UI, open source |
| **True decentralization** | Matrix (Commet/Element) | Federated — no single company controls it |
| **Best for large communities** | Zulip or Discourse | Topic-based threading, strong moderation |
| **Maximum privacy** | Matrix or SimpleX | E2EE by default, federated/decentralized |
| **Discord bot compatibility** | Spacebar | Discord API compatible, bots work as-is |
| **Gaming communities** | Steam Chat or TeamSpeak | Low-latency voice, huge user base (Steam) |
| **Self-host without hassle** | Zulip or Rocket.Chat | Docker support, good documentation |

**→ See [COMPARISON.md](COMPARISON.md) for full feature comparison**

---

## ⚠️ Critical Warnings

**Before choosing a platform, check these:**

### 🔒 Active Security Incidents
- **Matrix** — Cryptographic vulnerability (Feb 17, 2026) → Monitor for patches
- **Kloak** — Critical breach (Feb 20, 2026) → **DO NOT USE**
- **Paracord** — 20+ vulnerabilities → **DO NOT USE**

**→ See [SECURITY.md](SECURITY.md) for full details**

### 🤖 AI-Generated "Vibe-Coded" Platforms
- **Paracord, Blite Chat, Voltage** — AI-generated, unverified security
- **Discourse, Virola, Osmium, Rocket.Chat, Root** — Community flagged concerns
- **Stoat, Fluxer, Oldcord, Spacebar, Zulip** — Responsible AI use (transparent, reviewed)

**→ See [SECURITY.md](SECURITY.md#what-is-vibe-coding) for explanation**

### 🔐 Privacy-Invasive Platforms
- **Discord (March 2026)** — Will require face scans or government ID
- **All centralized commercial platforms** — Will face same pressure eventually

**→ See [MODERATION.md](MODERATION.md#the-centralization-problem) for why this matters**

---

## What Is This?

This repository is a **structured, community-maintained comparison** of Discord alternatives:

- **67 platforms** tracked across **8 categories**
- **61 features** organized into **8 logical groups**
- **Auto-generated comparison tables** from single source of truth (`platforms.json`)

### Categories

**Matrix Clients** (5) — Element, Cinny, Commet, FluffyChat, SchildiChat  
**Privacy-Focused Centralized** (9) — Stoat, Valour, Nerimity, Kloak, Echoed, Voltage, Apoka, etc.  
**Self-Hosted Platforms** (18) — Spacebar, Fluxer, Zulip, Rocket.Chat, Discourse, Mattermost, etc.  
**Commercial Alternatives** (6) — Discord, Telegram, GameVox, Steam Chat, Osmium, Root  
**Legacy & Niche** (14) — TeamSpeak, Mumble, Signal, Ventrilo, IRC, XMPP, Carrion (Adult RP), etc.  
**Business Productivity** (6) — Slack, Microsoft Teams, Amazon Chime, Pumble, Chanty, Virola  
**Protocols & Frameworks** (1) — Polyproto (for developers, not end users)  
**Discontinued** (8) — Guilded, Xfire, RaidCall, Curse Voice, etc.

**→ See [COMPARISON.md](COMPARISON.md) for detailed breakdown**

---

## Most Discord-Like Platforms

Based on 16 core features (including moderation):

| Rank | Platform | Similarity | Category | Notes |
|------|----------|-----------|----------|-------|
| 1 | Commet | 100% (16/16) | Matrix | Most Discord-like Matrix client |
| 2 | Element | 100% (16/16) | Matrix | Federated, E2EE by default |
| 3 | SchildiChat | 100% (16/16) | Matrix | Element fork, simplified UI |
| 4 | Mattermost | 88% (14/16) | Self-Hosted | DevOps favorite, E2EE beta |
| 5 | Microsoft Teams | 88% (14/16) | Business | Office integration, federated |
| 6 | Rocket.Chat | 88% (14/16) | Self-Hosted | Enterprise-grade tools |
| 7 | Slack | 88% (14/16) | Business | Workplace standard |
| 8 | Telegram | 88% (14/16) | Commercial | Huge scale, missing persistent voice |
| 9 | Discourse | 75% (12/16) | Self-Hosted | Forum-style, excellent moderation |
| 10 | Echoed | 69% (11/16) | Privacy-Focused | Missing moderation tools |

**Key insights:**
- Matrix clients lead (100%) but need moderation bots
- Business platforms (Slack, Teams) score high due to strong moderation
- Gaming alternatives (Stoat, Fluxer) feel Discord-like but lack advanced moderation

**→ See full ranking in [README.md - Discord Similarity section](#most-discord-like-platforms) (you're here!)**

---

## Why People Are Leaving Discord

### The Timeline:
- **Sept 2025:** Discord breach exposes 70,000 government IDs
- **Feb 2026:** Discord announces mandatory global age verification
- **March 2026:** Phased rollout begins

### The Requirements:
- Face scanning via video selfie, OR
- Government ID upload (driver's license, passport)
- "Age inference" AI surveillance in background

### The Response:
- Major creators refuse (Eret: 1M+ followers, Tubbo: 5.2M)
- Reddit exodus, Nitro cancellations
- EFF condemns: "Beyond what any law requires"
- Search spike for "Discord alternatives"

### The Deeper Problem:
- **UK Online Safety Act** requires platforms to implement age verification
- **EU DSA, Australia, US states** — similar laws spreading
- **Any centralized platform** will face same pressure
- **Vendor concerns:** Discord tested Persona (security issues, tracks extensive metrics for advertisers), switched to k-ID, could switch again
- **Business model shift:** Discord increasingly advertiser-friendly, in-app game microtransactions, potential IPO
- **Only solution:** Decentralization and self-hosting

**→ Read full story: [BACKGROUND.md](BACKGROUND.md)**  
**→ Understand the pattern: [MODERATION.md](MODERATION.md#the-centralization-problem)**

---

## Feature Groups

All 61 features organized into 8 groups:

1. **Privacy & Licensing** (11) — Open source, E2EE, no tracking, AI usage
2. **Pricing** (6) — Free tier, hardware costs, premium limitations
3. **Platform Support** (8) — Web, Windows, macOS, Linux, Android, iOS, Docker
4. **Communication** (10) — Voice, video, screen sharing, text, files
5. **Moderation & Safety** (8) — AutoMod, audit logs, raid protection, age/ID verification
6. **Server & Admin** (7) — Roles, organization, migration, bridges
7. **Channels & Content** (5) — Docs, events, galleries, announcements
8. **Community Tools** (6) — Bots, webhooks, raid planners, tournaments

**→ See [FEATURES.md](FEATURES.md) for detailed explanations and trade-offs**

---

## How to Choose

### Step 1: Define Your Must-Haves
- What features can't you live without?
- What's your privacy tolerance?
- What's your technical skill level?
- What's your budget?

### Step 2: Check Security
- Read [SECURITY.md](SECURITY.md) for active incidents
- Avoid vibe-coded platforms for privacy-critical use
- Prefer established, audited platforms

### Step 3: Consider Moderation Needs
- Small community (<500)? Basic tools sufficient
- Large community (1000+)? Need AutoMod, audit logs
- Privacy-focused? Avoid invasive verification

### Step 4: Review Comparison
- Browse [COMPARISON.md](COMPARISON.md)
- Check platform notes (marked with †)
- Compare options side-by-side

### Step 5: Test Before Committing
- Try platform before migrating
- Test with small group
- Verify critical features work

**→ See [FEATURES.md](FEATURES.md) for prioritization guidance**

---

## Contributing

We welcome contributions! Here's how to help:

### Report Inaccuracies
- Open an [Issue](../../issues) with label `correction`
- Or submit PR updating `platforms.json`

### Add New Platform
1. Check it's not already listed
2. Ensure platform is real (not vaporware)
3. Follow template in `platforms.json`
4. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

### Vote on Features
- Visit [Discussions](../../discussions)
- Upvote features you want tracked
- Suggest new features (use template)

### Share Your Experience
- Migrated a community? Tell us what worked
- Found inaccuracies? Let us know
- Security concerns? Please report

**→ See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines**

---

## Data Sources

**Primary source:** `platforms.json` — single source of truth

**Community research:**
- [Discord Replacers by Jay Gatsby](https://docs.google.com/spreadsheets/d/14vicw-V9Z5m7ckuburP5wxyDIIb_fFJFEjnxxHk8qRw/edit?gid=0#gid=0)
- Official platform documentation
- Security audits and vulnerability reports
- Community testing and feedback

**Feature values:**
- ✅ `yes` — Fully supported
- ⚠️ `partial` — Limited support
- 🗓️ `planned` — On roadmap
- ❌ `no` — Not supported
- ❓ `unknown` — Unverified

---

## Related Resources

### Community Evaluations
- [Discord Alternatives: My Personal Deep Dive by mvh](https://rant.mvh.dev/discord-alternatives-my-personal-deep-dive-into-matrix-zulip-discourse-and-stoat) — In-depth comparison of Matrix, Zulip, Discourse, and Stoat
- [In Search of a Discord Replacement by James Liu](https://no-bull.sh/blog/2026/02/16/in-search-of-a-discord-replacement/)
- [Discord Alternatives, Ranked by Michael Taggart](https://taggart-tech.com/discord-alternatives/)
- [Original r/matrixdotorg discussion](https://www.reddit.com/r/matrixdotorg/comments/1r50sqi/)

### Platform Documentation
- [Matrix.org](https://matrix.org) — Federated protocol
- [Stoat](https://stoat.chat) — Open source alternative
- [Zulip](https://zulip.com) — Topic-based threading
- [Rocket.Chat](https://rocket.chat) — Self-hosted collaboration

### Other Comparisons
- [Discord Alternatives by Hemeka](https://github.com/Hemeka/Discord-Alternatives)
- [Self-hosted alternatives by Vigno04](https://github.com/Vigno04/discord-selfhosted-alternatives)

---

## License

[Creative Commons Zero v1.0 Universal (CC0)](LICENSE) — freely usable by anyone.

---

**Built by the community, for the community.**  
*If this helped you, consider starring ⭐ the repo so others can find it.*

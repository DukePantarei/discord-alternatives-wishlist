# Discord Alternatives Comparison
### A community-driven comparison of privacy-respecting, open-source chat platforms

> **Are you a Discord refugee?** In February 2026, Discord announced mandatory age verification (face scans or government ID) just 5 months after a breach exposed 70,000 IDs. This project helps you find privacy-respecting alternatives.

---

## 📖 Navigation

- **[BACKGROUND.md](BACKGROUND.md)** — Full Discord exodus story, why this matters
- **[COMPARISON.md](COMPARISON.md)** — Feature comparison table (79 platforms, 61 features)
- **[FEATURES.md](FEATURES.md)** — What features mean and how to prioritize
- **[SECURITY.md](SECURITY.md)** — Vibe-coded platforms, active security incidents
- **[MODERATION.md](MODERATION.md)** — Privacy-respecting vs invasive moderation
- **[BEYOND_DISCORD.md](BEYOND_DISCORD.md)** — Dream features: What could be better than Discord?

---

## Quick Start

### If you want...

| Goal | Try | Why |
|------|-----|-----|
| **Easiest Discord transition** | Fluxer or Matrix (Commet) | Fluxer: Discord-like, self-hostable. Commet: Discord UI on proven Matrix protocol |
| **True decentralization** | Matrix (Element/Commet/Cinny) | Federated — no single company controls it, proven at scale |
| **Best for small communities (<100)** | Fluxer, Spacebar, or Matrix | Discord-like features, self-hostable, privacy-focused |
| **Best for large communities (100+)** | Matrix, Zulip, or Discourse | Proven at scale, topic-based threading, strong moderation |
| **Maximum privacy** | Matrix or RetroShare | Matrix: E2EE + federated. RetroShare: P2P + anonymous |
| **Discord bot compatibility** | Spacebar | Discord API compatible, existing bots work as-is |
| **Gaming communities** | Matrix (Element Call) or TeamSpeak | Matrix: Modern + E2EE. TeamSpeak: Legacy but reliable |
| **Self-host without hassle** | Zulip, Rocket.Chat, or Conduit | Good docs, Docker support. Conduit: lightweight Matrix server |

**Avoid Stoat (formerly Revolt):** Serious child safety concerns (mishandled CSAM reports), censorship of criticism, deceptive user count claims (advertises "1M+ users" but 200-400 actually online), moving away from open source. Voice features recently added (Feb 18-20, 2026) but very new and stability unproven. See platform notes in COMPARISON.md for details.

**→ See [COMPARISON.md](COMPARISON.md) for full feature comparison**

---

## Critical Warnings

**Before choosing a platform, check these:**

### Matrix Cryptographic Vulnerability (Feb 17, 2026)

Monitor for patches before using for sensitive communications:
- Matrix Rust library (vodozemac) has cryptographic issues
- Affects: Element, Commet, FluffyChat, all Matrix clients using vodozemac
- See [SECURITY.md](SECURITY.md) for latest status

### Early Stage / Unverified Platforms

**16 platforms are marked "Early Stage / Unverified"** - included for transparency but NOT recommended for production use.

**Platforms with active security issues:**
- **Kloak** - Security breach (Feb 20, 2026): Attacker accessed user list and private messages
- **Paracord** - 20+ documented vulnerabilities including remote code execution and plaintext secrets

See [SECURITY.md](SECURITY.md) for complete vulnerability details.

**Other platforms in this category:**
Ripcord (new), sadlounge, Apoka, Pulse Chat, Sharkord, Roomy, Colanode, Raven, Commz, Voltage, Osmium, Concord, Nexus Chat, Nexus (Magnimont)

These range from vaporware (waitlist only) to very early projects with minimal documentation. Check their notes in [COMPARISON.md](COMPARISON.md) for specific details on each platform's status and concerns.

### AI-Generated "Vibe-Coded" Platforms
- **Paracord, Blite Chat, Voltage** — AI-generated, unverified security
- **Discourse, Virola, Osmium, Rocket.Chat, Root** — Community flagged concerns
- **Stoat, Fluxer, Oldcord, Spacebar, Zulip** — Responsible AI use (transparent, reviewed)

**→ See [SECURITY.md](SECURITY.md#what-is-vibe-coding) for explanation**

### Privacy-Invasive Platforms
- **Discord (March 2026)** — Will require face scans or government ID
- **All centralized commercial platforms** — Will face same pressure eventually

**→ See [MODERATION.md](MODERATION.md#the-centralization-problem) for why this matters**

---

## What Is This?

This repository is a **structured, community-maintained comparison** of Discord alternatives:

- **73 platforms** tracked across **8 categories**
- **61 features** organized into **8 logical groups**
- **Auto-generated comparison tables** from single source of truth (`platforms.json`)

### Categories

**Matrix Clients** (5) — Element, Cinny, Commet, FluffyChat, SchildiChat  
**Privacy-Focused Centralized** (12) — Stoat, Valour, Nerimity, Kloak, Echoed, Voltage, Apoka, Session, RetroShare, 0xchat, etc.  
**Self-Hosted Platforms** (21) — Spacebar, Fluxer, Zulip, Rocket.Chat, Discourse, Mattermost, Strafe, Common Ground, Conduit, etc.  
**Commercial Alternatives** (6) — Discord, Telegram, GameVox, Steam Chat, Osmium, Root  
**Legacy & Niche** (14) — TeamSpeak, Mumble, Signal, Ventrilo, IRC, XMPP, Carrion (Adult RP), etc.  
**Business Productivity** (6) — Slack, Microsoft Teams, Amazon Chime, Pumble, Chanty, Virola  
**Protocols & Frameworks** (1) — Polyproto (for developers, not end users)  
**Discontinued** (8) — Guilded, Xfire, RaidCall, Curse Voice, etc.

**→ See [COMPARISON.md](COMPARISON.md) for detailed breakdown**

---

## Most Discord-Like Platforms

Based on feature coverage, real-world testing (mvh, discordless.com), and UI/UX similarity:

| Rank | Platform | Why Discord-Like | Category | Reality Check |
|------|----------|------------------|----------|---------------|
| 1 | **Fluxer** | Nearly complete feature parity, Discord-style UI, bot API | Self-Hosted | Public beta, self-hostable |
| 2 | **Commet** | Discord-like UI on Matrix protocol, full features | Matrix | Single maintainer, federated |
| 3 | **Element** | Full Matrix features, most mature client | Matrix | Different UI, proven at scale |
| 4 | **SchildiChat** | Element fork with Discord-inspired tweaks | Matrix | Element features + better UX |
| 5 | **Spacebar** | Discord API compatible, bot compatibility | Self-Hosted | Alpha stage, voice in development |
| 6 | **Stoat** | Closest Discord clone in look/feel | Privacy-Focused | ⚠️ Alpha: voice broken, slow updates, expect issues |
| 7 | **Rocket.Chat** | Enterprise features, voice/video, roles | Self-Hosted | 50 user limit (free), business-focused |
| 8 | **Mattermost** | Team chat, moderation, integrations | Self-Hosted | DevOps/business focused |
| 9 | **Telegram** | Massive scale, channels, bots | Commercial | Missing persistent voice channels |
| 10 | **Zulip** | Topic-based threading, full features | Self-Hosted | Different paradigm (topics required) |
| 11 | **Slack** | Workplace standard, strong features | Business | Business-focused, expensive |

**⚠️ Alpha/Early Stage Platforms:**
- **Stoat** — Voice support just added (Feb 18-20, 2026), working on main instance but very new. Browser-based voice functional, desktop app still in development. Updates slow, alpha-quality stability. Beautiful Discord-like UI but production readiness questionable. Serious moderation concerns (see platform notes). Revisit in ~1 year.
- **Spacebar** — Discord bot compatibility promising but voice/video still in development. Making new guilds/adding friends may not work consistently.

**❌ DO NOT USE (Security Issues):**
- **Kloak** — Critical security breach (Feb 2026), user data compromised
- **Paracord** — 20+ vulnerabilities, vibe-coded, unverified security

**Key insights:**
- **Fluxer** leads for open-source Discord-like experience (discordless: "only open-source app with almost all Discord features")
- **Matrix clients** offer proven federation + E2EE, but need moderation bots (Draupnir essential)
- **Stoat** looks most like Discord but core features broken — beautiful UI, frustrating experience
- **Avoid platforms with security incidents** (Kloak, Paracord) entirely

**→ See [COMPARISON.md](COMPARISON.md) for detailed feature breakdown**

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

### Platform Directories
- **[discordless.com](https://discordless.com/)** — Curated alternatives with privacy focus, decentralization emphasis, and detailed pros/cons
- [AlternativeTo: Discord Alternatives](https://alternativeto.net/software/discord-app/) — 100+ alternatives with user ratings and comments
- [Discord Alternatives by Hemeka](https://github.com/Hemeka/Discord-Alternatives)
- [Self-hosted alternatives by Vigno04](https://github.com/Vigno04/discord-selfhosted-alternatives)

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

# Discord Alternatives Comparison
### A community-driven comparison of privacy-respecting, open-source chat platforms

> **Are you a Discord refugee?** You're not alone. This project was born from the growing wave of users looking for privacy-respecting, open-source alternatives to Discord. Basically, platforms that don't scan your face, sell your data, or push advertisements into your chats.

---

## What Is This?

This repository is a **structured, community-maintained comparison** of Discord alternatives across **61 platforms** and **55 features**. It's designed to help you make an informed decision about where to move your community.

## Current State

- **61 platforms** tracked across **7 categories**
- **55 features** organized into **8 logical groups**
- **Auto-generated comparison tables** from a single source of truth (`platforms.json`)

### Categories

- **Matrix Clients** (5) — Decentralized, federated, open protocol (Element, Cinny, Commet, FluffyChat, SchildiChat)
- **Privacy-Focused Centralized** (6) — Open source but centrally hosted (Stoat, Valour, Nerimity, Kloak, Blite Chat, Echoed)
- **Self-Hosted Platforms** (18) — Run your own instance (Spacebar, Fluxer, Zulip, Rocket.Chat, Discourse, Mattermost, Sharkord, Loqa, DCTS, Mezon, Nextcloud Talk, Snikket, Databag, Pulse, Roomy, Colanode, Raven)
- **Commercial Alternatives** (6) — Polished products with varying privacy tradeoffs (Discord, Root, Telegram, GameVox, Steam Chat, Osmium)
- **Legacy & Niche** (12) — Historical context and specific use cases (TeamSpeak, Mumble, Signal, Ventrilo, Skype, SimpleX Chat, Quiet, Campfire, Oldcord, Jami, Gajim, Swift IM, Movim)
- **Business Productivity** (6) — Team collaboration tools (Slack, Microsoft Teams, Amazon Chime, Pumble, Chanty, Virola)
- **Discontinued** (8) — Platforms no longer active, included for historical reference (Guilded, Roger Wilco, Xfire, RaidCall, Dolby Axon, Razer Comms, Curse Voice, TeaSpeak)

**If you're a user:** Browse [COMPARISON.md](COMPARISON.md) to see detailed feature matrices for every platform. Vote on features you want via GitHub Discussions.

**If you're a developer:** Use the [wishlist discussions](../../discussions) to understand what users actually need. The comparison tables show gaps where no platform excels yet.

---

## Quick Comparison

Not sure where to start? Here are some common paths:

| If you want... | Try... | Why |
|---|---|---|
| **Easiest Discord transition** | Stoat (formerly Revolt) or Fluxer | Most Discord-like UI and features, open source |
| **True decentralization** | Matrix (via Commet or Element) | Federated protocol — no single company can shut it down |
| **Best for large communities (1000+ users)** | Zulip | Topic-based threading scales well, strong moderation tools |
| **Self-host without technical hassle** | Zulip or Rocket.Chat | Mature platforms with good docs and Docker support |
| **Maximum privacy** | Matrix or SimpleX Chat | Matrix has E2EE by default; SimpleX has no user identifiers |
| **Discord bot compatibility** | Spacebar | Only platform where existing Discord bots work without modification |
| **Gaming communities** | Steam Chat or TeamSpeak | Steam Chat has 350M+ gamers; TeamSpeak has low-latency voice |

**See the full comparison:** [COMPARISON.md](COMPARISON.md)

---

## Most Discord-like Platforms

Looking for the closest thing to Discord? Here are platforms ranked by how many core Discord features they support:

| Platform | Discord Similarity | Category | Key Differences |
|----------|-------------------|----------|-----------------|
| **Element** | 100% (11/11) | Matrix Client | Federated, E2EE by default, steeper learning curve |
| **Commet** | 100% (11/11) | Matrix Client | Most Discord-like Matrix client, excellent mobile support |
| **SchildiChat** | 100% (11/11) | Matrix Client | Element fork with simplified UI |
| **Sharkord** | 100% (11/11) | Self-Hosted | Self-hostable, open source, smaller community |
| **Root** | 100% (11/11) | Commercial | Privacy-focused commercial alternative |
| **Kloak** | 100% (11/11) | Privacy-Focused | Centralized but open source, active development |
| **Fluxer** | 91% (10/11) | Self-Hosted | Missing bots, but very Discord-like UI and features |
| **DCTS** | 91% (10/11) | Self-Hosted | Lightweight, self-hostable, good for small communities |
| **Stoat** | 64% (7/11) | Privacy-Focused | No voice/video yet, but most Discord-like UI |
| **Spacebar** | 64% (7/11) | Self-Hosted | Discord API compatible (bots work!), no voice/video yet |

**Scoring based on:** Voice/video chat, screen sharing, text channels, persistent voice, bots, roles, server organization, GIFs, file sharing, invite links

**Notes:** 
- **Matrix clients** (Element, Commet, SchildiChat) score perfectly but use a different architecture (federated) requiring a homeserver
- **Stoat** and **Spacebar** have the most Discord-like *interfaces* but are still building out voice/video features
- **Fluxer** is probably the best drop-in replacement if you want something that feels exactly like Discord

---

## Moderation & Safety: The Privacy Tradeoff

**Why this matters:** Discord's planned age verification system (requiring government ID or face scans) is a major privacy concern and a key reason people are seeking alternatives. This repository tracks both traditional moderation tools AND privacy-invasive verification systems.

### CRITICAL: The Centralization Problem

**Discord isn't unique — this is a systemic issue with centralized platforms:**

Any centralized, commercial platform (Discord, Slack, Teams, etc.) will eventually face the same government pressure to implement invasive age verification and content monitoring. The UK's Online Safety Act is just the beginning — similar legislation is spreading:
- **UK:** Age verification via ID/face scan (active enforcement 2025)
- **EU:** Digital Services Act requiring content moderation at scale
- **Australia:** Online Safety Act with similar requirements
- **US:** Multiple state laws requiring age verification for "harmful content"

**The pattern:**
1. Government passes "safety" legislation
2. Centralized platforms must comply or face massive fines
3. Platform implements invasive verification (ID upload, biometrics, AI monitoring)
4. User privacy is permanently compromised

**Discord is just the first to announce it publicly.** Other commercial platforms will follow as enforcement ramps up. If you're fleeing Discord for another centralized commercial platform (Root, Osmium, etc.), you're only buying time before they face the same requirements.

### The Only Long-Term Solution: Decentralization & Self-Hosting

**Platforms that can resist this pressure:**
- **Self-hosted** (Rocket.Chat, Mattermost, Discourse) — You control the server, you set the rules
- **Federated** (Matrix, XMPP) — No central authority to compel, enforcement is impractical
- **Open source** — Can be forked and run outside jurisdictions with invasive laws

**Why these work:**
- No central company to fine or prosecute
- Can be hosted in privacy-friendly jurisdictions
- Community can fork if project compromises
- Enforcement is technically and legally impractical

### Privacy-Invasive Verification (Avoid These)

**Discord** — Planned invasive verification:
- **Age Verification (Planned)**: Teen accounts with restricted features
- **ID Verification (Planned)**: Face scanning OR government ID upload required for age-gating
- **UK Pilot (2025)**: Testing biometric age verification
- **Privacy Impact**: Government ID and biometric data stored by third-party vendor (Yoti)
- **Why this is problematic**: Creates honeypot of sensitive data, face recognition normalizes surveillance, disproportionate for chat platform

**Other Centralized Platforms** — Not yet, but coming:
- All major centralized platforms (Slack, Teams, Root, Osmium, etc.) will face the same legislative pressure
- Compliance is a question of when, not if
- Moving from Discord to another centralized platform is a temporary solution

### Privacy-Respecting Moderation

These platforms offer strong moderation WITHOUT invasive identity verification:

**Discourse** — Trust-based moderation:
- AutoMod with automatic post hiding
- Trust levels (new users → regulars → leaders)
- Flag system for community reporting
- Audit logs and user silencing
- **Privacy**: Email-based, no ID verification, GDPR compliant

**Matrix (Element/Commet/SchildiChat)** — Decentralized moderation:
- Draupnir/Mjolnir bots for advanced moderation
- Shared ban lists across federated servers
- Audit logs and user timeouts
- **Privacy**: E2EE by default, federated (you choose your homeserver), no central authority

**Rocket.Chat & Mattermost** — Enterprise-grade:
- Message reporting and review queues
- Audit logs for compliance
- Role-based permissions
- **Privacy**: Self-hosted option means full data control, GDPR compliant

**Discord (Current Features)** — Strong moderation, pre-verification era:
- AutoMod (keyword filters, spam detection, mention limits)
- Raid protection and verification levels
- Audit logs and timeout features
- Message reporting dashboard
- **Note**: Current Discord is fine; concern is planned 2025+ verification requirements

### Basic Moderation

Most alternatives offer basic moderation tools:
- Kick/ban users
- Role-based permissions
- Message deletion
- Channel controls

**Sufficient for**: Small to medium communities (<500 active members)  
**May struggle with**: Large public communities with active raids/spam

### Check the Full Comparison

See the [Moderation & Safety table](COMPARISON.md) for detailed feature-by-feature comparison including:
- AutoMod capabilities
- Audit logs
- Raid protection
- Message reporting
- Age/ID verification status (who's privacy-respecting vs invasive)

### Bottom Line

**For large communities with moderation needs**:
1. **Privacy-focused + good moderation**: Discourse (forums) or Matrix with Draupnir (chat)
2. **Best moderation, some privacy concerns**: Current Discord (before verification rollout)
3. **Avoid**: Discord after age/ID verification rollout (2025+)

**For small/medium communities**:
- Most alternatives have sufficient moderation tools
- Prioritize privacy, self-hosting, and federation over advanced moderation

---

## Key Features Tracked

All features are organized into **8 logical groups** for easier comparison:

### Privacy & Licensing (9 features)
- Open source, self-hostable, federated
- End-to-end encryption, no ads, no tracking, GDPR compliance
- Biometric age verification, message TTL / auto-expiry

### Pricing (5 features)
- Free to use, no premium tier required
- Self-hosting license (freely self-hostable vs commercial license)
- Freemium limitations, enterprise tier availability

### Platform Support (5 features)
- Web app, desktop app, mobile app
- Docker install, mobile device hosting

### Communication (10 features)
- Voice, video, screen sharing (with system audio)
- Text channels, file sharing, GIF/embed support
- Threads & forums, persistent voice channels
- Per-user audio output control

### Moderation & Safety (8 features)
- Large community moderation tools
- AutoMod (automated content filtering)
- Audit logs, user timeout/mute, raid protection
- Message reporting
- **Age verification** (Discord's planned teen accounts)
- **ID verification** (Discord's planned face scanning & ID checks)

### Server & Admin (7 features)
- Role management, server organization, admin GUI
- Invite links & guest access, migration assistant
- Bridges to other platforms, Discord API compatibility

### Channels & Content (5 features)
- Docs/wiki channels, list/task channels, media galleries
- Scheduled announcements, event scheduling

### Community Tools (6 features)
- Bots & automation, webhooks
- Raid planner / group activity tools
- Tournament brackets, rich calendar tools
- Community discovery

---

## How to Participate

### Vote on feature priorities
Go to the [**Discussions tab**](../../discussions) and upvote features you want.

### Submit a new feature idea
1. Check [existing discussions](../../discussions) to avoid duplicates
2. Click **New Discussion** and select the **💡 Feature Ideas & Improvements** category
3. Use the provided template (see [feature_request.md](feature_request.md))

### Report an inaccuracy
If something in the comparison table is wrong or outdated, open an [Issue](../../issues) with the label `correction`, or submit a Pull Request updating `platforms.json`.

### Add a new platform
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome additions as long as they meet basic criteria (real users, public availability, not vaporware).

---

## Understanding the Data

All platform data lives in **`platforms.json`** — a single source of truth that generates the comparison tables automatically via GitHub Actions.

**Data sources:** This repository integrates information from community research, official documentation, and the excellent [Discord Replacers spreadsheet by Jay Gatsby](https://docs.google.com/spreadsheets/d/14vicw-V9Z5m7ckuburP5wxyDIIb_fFJFEjnxxHk8qRw/edit?gid=0#gid=0), with additional verification and expansion.

**Feature values:**
- ✅ `yes` — Fully supported
- ⚠️ `partial` — Limited support or workarounds needed
- 🗓️ `planned` — Officially on the roadmap
- ❌ `no` — Not supported
- ❓ `unknown` — Unverified

**Notes:** Many features have `†` markers linking to detailed notes below each table explaining limitations, workarounds, or context.

---

## Related Resources

### Community Evaluations
- [Original Reddit discussion (r/matrixdotorg)](https://www.reddit.com/r/matrixdotorg/comments/1r50sqi/)
- [In Search of a Discord Replacement by James Liu](https://no-bull.sh/blog/2026/02/16/in-search-of-a-discord-replacement/)
- [Discord Alternatives, Ranked by Michael Taggart](https://taggart-tech.com/discord-alternatives/)
- [Discord Replacers by Jay Gatsby (Google Sheet)](https://docs.google.com/spreadsheets/d/14vicw-V9Z5m7ckuburP5wxyDIIb_fFJFEjnxxHk8qRw/edit?gid=0#gid=0) — Community-maintained spreadsheet comparison

### Platform Documentation
- [Matrix.org](https://matrix.org) — Federated protocol
- [matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy) — Easy Matrix self-hosting
- [Stoat](https://stoat.chat) — Open source Discord alternative
- [Zulip](https://zulip.com) — Topic-based threading for communities
- [Rocket.Chat](https://rocket.chat) — Self-hosted team collaboration

### Other Comparisons
- [Discord Alternatives by Hemeka](https://github.com/Hemeka/Discord-Alternatives)
- [Self-hosted alternatives by Vigno04](https://github.com/Vigno04/discord-selfhosted-alternatives)
- [So you need a Discord alternative by u/firebreathingbunny](https://www.reddit.com/r/TechQA/comments/1r2frya/so_you_need_a_discord_alternative_alternate/)
- [A list of discord alternatives by u/Locustinalab](https://www.reddit.com/r/pcgaming/comments/1r27qjf/a_list_of_some_discord_alternatives_and_their/)
- [Discord Alternatives by u/Bologna0128](https://www.reddit.com/r/degoogle/comments/1r5catk/discord_alternatives/)

---

## Contributing

1. **Update platform data** — Submit PRs to `platforms.json` when features change
2. **Add missing platforms** — Follow the template in `platforms.json` (see [CONTRIBUTING.md](CONTRIBUTING.md))
3. **Improve documentation** — Clarify notes, fix typos, add context
4. **Vote and discuss** — Use GitHub Discussions to prioritize features
5. **Share your experience** — If you've migrated a community, tell us what worked and what didn't

---

## License

All content in this repository is licensed under [Creative Commons Zero v1.0 Universal (CC0)](LICENSE) — meaning it is freely usable by anyone, including developers who want to implement these features.

---

*Built by the community, for the community. If this helped you, consider starring ⭐ the repo so others can find it.*

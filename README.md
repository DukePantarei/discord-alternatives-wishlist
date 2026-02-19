# Discord Alternatives Comparison
### A community-driven comparison of privacy-respecting, open-source chat platforms

> **Are you a Discord refugee?** You're not alone. This project was born from the growing wave of users looking for privacy-respecting, open-source alternatives to Discord. Basically, platforms that don't scan your face, sell your data, or push advertisements into your chats.

---

## What Is This?

This repository is a **structured, community-maintained comparison** of Discord alternatives across **55 platforms** and **48 features**. It's designed to help you make an informed decision about where to move your community.

## Current State

- **55 platforms** tracked across **7 categories**
- **48 features** organized into **7 logical groups**
- **Auto-generated comparison tables** from a single source of truth (`platforms.json`)

### Categories

- **Matrix Clients** (5) — Decentralized, federated, open protocol (Element, Cinny, Commet, FluffyChat, SchildiChat)
- **Privacy-Focused Centralized** (6) — Open source but centrally hosted (Stoat, Valour, Nerimity, Kloak, Blite Chat, Echoed)
- **Self-Hosted Platforms** (16) — Run your own instance (Spacebar, Fluxer, Zulip, Rocket.Chat, Sharkord, Loqa, DCTS, Mattermost, Discourse, Mezon, Nextcloud Talk, Snikket, Databag, Pulse, Roomy, Colanode, Raven)
- **Commercial Alternatives** (6) — Polished products with varying privacy tradeoffs (Discord, Root, Telegram, GameVox, Steam Chat, Osmium)
- **Legacy & Niche** (11) — Historical context and specific use cases (TeamSpeak, Mumble, Signal, Ventrilo, Skype, SimpleX Chat, Quiet, Campfire, Oldcord, Jami, Gajim, Swift IM, Movim)
- **Business Productivity** (3) — Team collaboration tools (Pumble, Chanty, Virola)
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

## Key Features Tracked

All features are organized into **7 logical groups** for easier comparison:

### Privacy & Licensing (9 features)
- Open source, self-hostable, federated
- End-to-end encryption, no ads, no tracking, GDPR compliance
- Biometric age verification, message TTL / auto-expiry

### Pricing & Licensing (5 features)
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

### Server & Admin (9 features)
- Role management, server organization, admin GUI
- Large community moderation tools
- Invite links & guest access, migration assistant
- Bridges to other platforms, Discord API compatibility
- Community discovery

### Channels & Content (5 features)
- Docs/wiki channels, list/task channels, media galleries
- Scheduled announcements, event scheduling

### Community Tools (5 features)
- Bots & automation, webhooks
- Raid planner / group activity tools
- Tournament brackets, rich calendar tools

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

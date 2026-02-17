# Discord Alternatives Comparison
### A community-driven comparison of privacy-respecting, open-source chat platforms

> **Are you a Discord refugee?** You're not alone. This project was born from the growing wave of users looking for privacy-respecting, open-source alternatives to Discord. Basically, platforms that don't scan your face, sell your data, or push advertisements into your chats.

---

## What Is This?

This repository is a **structured, community-maintained comparison** of Discord alternatives across 22 platforms and 44 features so far. It's designed to help you make an informed decision about where to move your community.

I've compare platforms across five categories:
- **Matrix Clients** — Decentralized, federated, open protocol
- **Privacy-Focused Centralized** — Open source but centrally hosted (Stoat, Valour, Nerimity)
- **Self-Hosted Platforms** — Run your own instance (Zulip, Rocket.Chat, Spacebar, etc.)
- **Commercial Alternatives** — Polished products with varying privacy tradeoffs (Discord baseline, Root, Telegram)
- **Legacy & Niche** — Historical context and specific use cases (Guilded, TeamSpeak, Mumble, Signal)

**If you're a user:** Browse [COMPARISON.md](COMPARISON.md) to see detailed feature matrices for every platform. Vote on features you want via GitHub Discussions.

**If you're a developer:** Use the [wishlist discussions](../../discussions) to understand what users actually need. The comparison tables show gaps where no platform excels yet.

---

## Quick Comparison

Not sure where to start? Here are some common paths:

| If you want... | Try... | Why |
|---|---|---|
| **Easiest Discord transition** | Stoat (formerly Revolt) | Most Discord-like UI and features, EU-based, open source |
| **True decentralization** | Matrix (via Commet or Element) | Federated protocol — no single company can shut it down |
| **Best for large communities (1000+ users)** | Zulip + Jitsi | Topic-based threading scales well, strong moderation tools |
| **Self-host without technical hassle** | Zulip or Rocket.Chat | Mature platforms with good docs and Docker support |
| **Maximum privacy** | Matrix or Mumble | Matrix has E2EE by default; Mumble has true E2EE voice |
| **Discord bot compatibility** | Spacebar | Only platform where existing Discord bots work without modification |

**See the full comparison:** [COMPARISON.md](COMPARISON.md)

---

## Key Features Tracked

**Privacy & Licensing**
- Open source, self-hostable, federated
- End-to-end encryption, no ads, no tracking, GDPR compliance
- Message TTL / auto-expiry

**Communication**
- Voice, video, screen sharing (with system audio)
- Persistent voice channels (hop-in/out anytime vs call-based)
- Text channels, file sharing, GIF/embed support
- Per-user audio volume control

**Features**
- Bots & automation, webhooks, role management
- Event scheduling, raid planners, rich calendar tools
- Docs/wiki channels, task lists, media galleries
- Large community moderation tools (automod, mass ban, audit logs)
- Migration assistants, bridges to other platforms

**Platform Support**
- Web app, desktop app, mobile app
- Docker install, mobile device hosting

**Pricing**
- Free to use, no premium tier required

---

## How to Participate

### Vote on feature priorities
Go to the [**Discussions tab**](../../discussions) and upvote features you want.

### Submit a new feature idea
1. Check [existing discussions](../../discussions) to avoid duplicates
2. Click **New Discussion** and select the **💡 Feature Ideas & Improvements** category
3. Use the provided template (see [FEATURE_REQUEST_TEMPLATE.md](.github/DISCUSSION_TEMPLATE/feature_request.md))

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
- 📣 [Original Reddit discussion (r/matrixdotorg)](https://www.reddit.com/r/matrixdotorg/comments/1r50sqi/)
- 📝 [In Search of a Discord Replacement](https://no-bull.sh/blog/2026/02/16/in-search-of-a-discord-replacement/)

### Platform Documentation
- 🌐 [Matrix.org](https://matrix.org) 
- 📦 [matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy)
- 🐘 [Stoat](https://stoat.chat) 
- 📊 [Zulip](https://zulip.com) 
- 🚀 [Rocket.Chat](https://rocket.chat) 

### Other Comparisons
- 📊 [Discord Alternatives by Hemeka](https://github.com/Hemeka/Discord-Alternatives)
- 📊 [Self-hosted alternatives by Vigno04](https://github.com/Vigno04/discord-selfhosted-alternatives)

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

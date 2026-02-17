# Matrix Client Wishlist
### A community-driven feature wishlist for the ideal privacy-first Discord alternative

> **Are you a Discord refugee?** You're not alone. This project was born from the growing wave of users looking for a privacy-respecting, open-source alternative to Discord. Ideally, one that doesn't scan your face, sell your data to the surveillance state, or push advertisements into your chats.

---

## What Is This?

This repository is a **structured, community-maintained wishlist** of features we want to see in a Matrix-based Discord alternative. Think of it as a public product roadmap, built by users, for developers.

Matrix is a powerful, decentralized, and federated open protocol for real-time communication. It already supports a lot of what Discord users love. However, the experience across clients is fragmented, and some key features are missing or hard to discover. This project aims to change that.

**If you're a user:** Browse the wishlist, vote on features you want, and submit new ideas.  
**If you're a developer:** Use this as a structured backlog to understand what the community actually needs.

---

## Why Matrix?

Unlike Discord, Matrix is:

- **Decentralized** — No single company controls the network. Anyone can run a homeserver.
- **Federated** — Servers talk to each other, just like email providers do.
- **Open source** — The protocol and most clients are fully open source.
- **Privacy-first** — End-to-end encryption available. No ads. No face scans.
- **Self-hostable** — You control your own data entirely.

> Think of Matrix like email. Homeservers are the providers (Gmail, Outlook, etc.), and clients are the apps you use to read your mail (Outlook app, Apple Mail, Thunderbird). You can pick any combination, and they all talk to each other.

### What Already Exists

Many Discord-like features already exist across the Matrix ecosystem — they're just not always in one place or easy to find:

| Feature | Status | Where to find it |
|---|---|---|
| Bots & automation | ✅ Exists | Matrix API, maubot |
| Large hosting / scaling | ✅ Exists | Synapse, Conduit, Dendrite |
| Web/video/GIF embeds | ✅ Exists | Commet, Element |
| Web interface | ✅ Exists | All major clients |
| Event schedule/calendar | ✅ Exists | Commet |
| Screen sharing | ✅ Exists (needs system audio) | Element, Commet |
| Voice & video chat | ✅ Exists | MatrixRTC + LiveKit |
| Role management | ✅ Partial | Client-dependent |
| Profile/nickname/avatar | ✅ Exists | Most clients |
| Docker installation | ✅ Exists | ESS, matrix-docker-ansible-deploy |
| Admin GUI | ✅ Partial | Element Admin, Synapse-Admin, Draupnir |

### What's Still Missing or Needs Improvement

- ❌ Migration assistant (from Discord — roles, channels, message history)
- ❌ Seamless invite URLs / anonymous/guest access with minimal friction
- ❌ Raid planner / event RSVP tools
- ❌ A single polished client that matches Discord's ease of use for non-technical users
- ❌ Better onboarding and education around the Server → Space → Room model
- ⚠️ Screen sharing with system audio
- ⚠️ Consistent UX across clients

---

## Client Landscape

Not sure which Matrix client to use? Here's a quick overview:

| Client | Best For | Notes |
|---|---|---|
| [Element](https://element.io) | Enterprise / power users | Reference client, most features, work-focused |
| [Cinny](https://cinny.in) | Discord-like UI | Clean, simple, actively developed |
| [Commet](https://commet.chat) | Feature-rich casual use | GIFs, stickers, events, voice channels |
| [FluffyChat](https://fluffychat.im) | Mobile / simple UX | Very beginner friendly |
| [SchildiChat](https://schildi.chat) | Discord-like feel | Based on Element with extra features |

> **Note:** Element is the reference client but it is **enterprise-focused**, not designed for average users. If you're coming from Discord, try **Cinny** or **Commet** first.

---

## How to Participate

### Vote on existing ideas
Go to the [**Discussions tab**](../../discussions) and use 👍 reactions to upvote features you want. The most-voted ideas help developers prioritize.

### Submit a new feature idea
1. Check [existing discussions](../../discussions) to avoid duplicates
2. Click **New Discussion** and select the **💡 Feature Ideas** category
3. Use the provided template to structure your idea (Epic → User Stories → Acceptance Criteria)
4. Tag it appropriately so developers can filter by area

### Report an inaccuracy
If something in this README is wrong or out of date, open an [Issue](../../issues) with the label `correction`.

### Contribute to the comparison list
See [contributing.md](contributing.md) for how to add new platforms or update feature status.

---

## Feature Categories

Features in this wishlist are organized into the following areas:

- 🔐 **Privacy & Security** — Encryption, data handling, verification
- 🎙️ **Voice & Video** — Audio quality, screen sharing, system audio
- 🤖 **Bots & Automation** — Bot frameworks, webhooks, integrations
- 🗂️ **Server Organization** — Spaces, rooms, channels, categories
- 🎨 **UI/UX** — Interface design, onboarding, discoverability
- 🔀 **Migration** — Tools to move from Discord, Slack, or other platforms
- 👤 **Identity & Access** — Profiles, guest access, invite links, roles
- 📅 **Events & Scheduling** — Calendars, RSVPs, raid planning
- 📱 **Platform Support** — Mobile, desktop, web apps

---

## Related Resources

- [Original Reddit discussion (r/matrixdotorg)](https://www.reddit.com/r/matrixdotorg/comments/1r50sqi/)
- [Matrix.org](https://matrix.org) — Official Matrix protocol home
- [matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy) — Easy self-hosting
- [ESS (Element Server Suite)](https://element.io/server-suite) — Managed hosting option
- [Discord Alternatives list by Hemeka](https://github.com/Hemeka/Discord-Alternatives)
- [Self-hosted alternatives comparison by Vigno04](https://github.com/Vigno04/discord-selfhosted-alternatives)

---

## License

All content in this repository is licensed under [Creative Commons Zero v1.0 Universal (CC0)](LICENSE) meaning it is freely usable by anyone, including developers who want to implement these features.

---

*Built by the community, for the community. If this helped you, consider starring ⭐ the repo so others can find it.*

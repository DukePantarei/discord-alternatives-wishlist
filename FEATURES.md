# Feature Guide

> **Quick reference:** What do all these features actually mean, and which ones matter for your community?

---

## Feature Groups Overview

All 58 features are organized into **8 logical groups** for easier comparison. Here's what each group covers and why it matters:

---

## 1. Privacy & Licensing (11 features)

### What This Group Covers:
- Open source, self-hostable, federated
- End-to-end encryption, no ads, no tracking, GDPR compliance
- Biometric age verification, message TTL / auto-expiry
- AI features / training on user data
- **AI-generated codebase ("vibe-coded")** - Security/quality concerns

### Why It Matters:
- **Trust & Transparency**: Open source = can audit code, verify privacy claims
- **Data Control**: Self-hosting = you own your data, not a corporation
- **Security**: E2EE = even platform operators can't read your messages
- **Longevity**: Federation = platform can't be shut down by single company

### Key Features Explained:

**Open Source**
- Source code publicly available and auditable
- Community can verify privacy/security claims
- Can be forked if project goes wrong direction

**Self-Hostable**
- You can run your own instance
- Full control over data, rules, and features
- Immune to platform policy changes

**Federated**
- Multiple instances can communicate with each other
- No single point of failure
- Choose your server/community

**End-to-End Encryption (E2EE)**
- Messages encrypted on your device, decrypted on recipient's device
- Server operators cannot read messages
- Gold standard for privacy

**AI-Generated Codebase**
- Platform primarily built using AI code generation
- **Security concern**: See [SECURITY.md](SECURITY.md) for why this matters
- Not automatically bad, but requires expert review

### How to Prioritize:

**High privacy needs:**
- Require: E2EE, open source, self-hostable or federated
- Consider: GDPR compliance, no tracking

**Moderate privacy needs:**
- Require: Open source, no ads
- Consider: Self-hostable option

**Low privacy needs:**
- May accept: Commercial platforms with good policies
- Still avoid: Platforms with active breaches or invasive verification

---

## 2. Pricing (6 features)

### What This Group Covers:
- Free to use, no premium tier required
- Self-hosting license (freely self-hostable vs commercial license)
- Freemium limitations, enterprise tier availability
- Hardware required for use (do you need to buy/rent a server?)

### Why It Matters:
- **Total cost of ownership**: "Free" platform that requires $50/month VPS isn't free
- **Feature access**: Can you use full platform without paying?
- **Sustainability**: How does platform make money?

### Key Features Explained:

**Free to Use**
- Can use platform without paying
- May have premium features, but core functionality is free

**No Premium Tier**
- All features available to everyone
- No "pro" or "plus" subscription needed
- Sustainable via donations, self-hosting, or other model

**Hardware Required for Use**
- Must you provide your own server (physical or VPS)?
- Self-hosted = yes, cloud-hosted = no
- Impacts total cost significantly

### How to Calculate True Cost:

**Cloud-hosted (free tier):**
```
Cost = $0/month (unless you hit limits)
Examples: Discord, Slack, Teams (free tier)
```

**Cloud-hosted (paid):**
```
Cost = Subscription fees
Examples: Slack ($8/user/mo), Teams ($4/user/mo)
```

**Self-hosted:**
```
Cost = Server rental + electricity + maintenance time
Examples: 
- Small: $5-10/month (basic VPS)
- Medium: $20-50/month (better performance)
- Large: $100+/month (high traffic)
```

### How to Prioritize:

**Budget-conscious:**
- Prefer: Free cloud tier or cheap self-hosting
- Avoid: Per-user pricing at scale

**Privacy-focused:**
- Accept: Self-hosting costs for data control
- Consider: Shared community server to split costs

---

## 3. Platform Support (5 features)

### What This Group Covers:
- Web app, desktop app, mobile app
- Docker install, mobile device hosting

### Why It Matters:
- **Accessibility**: Can your community access from their devices?
- **Deployment**: How easy is it to set up?
- **User experience**: Native apps vs web apps

### Key Features Explained:

**Web App**
- Access via browser, no installation needed
- Works on any device with browser
- May have fewer features than native apps

**Desktop App**
- Native Windows/Mac/Linux application
- Often better performance and features
- Offline support

**Mobile App**
- Native iOS/Android application
- Push notifications
- Mobile-optimized UI

**Docker Install**
- Self-hosting made easier
- One-command deployment
- Easy updates and maintenance

### How to Prioritize:

**Mixed device community:**
- Require: Web app + mobile apps
- Prefer: Desktop app for power users

**Mobile-first community:**
- Require: Excellent mobile apps
- Web app can be secondary

**Self-hosting:**
- Strongly prefer: Docker install support
- Makes deployment 10x easier

---

## 4. Communication (10 features)

### What This Group Covers:
- Voice, video, screen sharing (with system audio)
- Text channels, file sharing, GIF/embed support
- Threads & forums, persistent voice channels
- Per-user audio output control

### Why It Matters:
- **Core functionality**: This is what people actually use
- **Collaboration**: Voice/video/screen sharing for teams
- **Expression**: GIFs, files, rich media

### Key Features Explained:

**Persistent Voice Channels**
- Voice channels that exist permanently (like Discord)
- vs temporary call rooms
- Users can drop in/out freely

**Screen Sharing with System Audio**
- Share your screen AND the sound from your computer
- Critical for watching videos together, gaming
- Many platforms share screen but not audio

**Threads & Forums**
- Organize conversations by topic
- Prevent channel clutter
- Keep discussions focused

### How to Prioritize:

**Gaming communities:**
- Require: Voice, persistent voice channels, screen sharing with audio
- Prefer: Low-latency voice

**Work/collaboration:**
- Require: Video, screen sharing, file sharing
- Prefer: Threads for organization

**Text-focused communities:**
- Require: Text channels, GIFs, file sharing
- Voice/video optional

---

## 5. Moderation & Safety (8 features)

### What This Group Covers:
- Large community moderation tools
- AutoMod (automated content filtering)
- Audit logs, user timeout/mute, raid protection
- Message reporting
- **Age verification** (Discord's planned teen accounts)
- **ID verification** (Discord's planned face scanning & ID checks)

### Why It Matters:
- **Community health**: Tools to prevent spam, harassment, raids
- **Privacy concerns**: Invasive verification vs privacy-respecting moderation
- **Scale**: Small communities need basic tools, large communities need advanced

### Key Features Explained:

**AutoMod**
- Automated content filtering
- Keyword blocking, spam detection
- Reduces moderator workload

**Audit Logs**
- Track all moderation actions
- Accountability for moderators
- Investigate issues after the fact

**Raid Protection**
- Prevent mass join spam
- Verification levels for new users
- Rate limiting

**Age/ID Verification** ⚠️
- **Red flag**: Invasive privacy violation
- Face scanning or government ID upload
- See [MODERATION.md](MODERATION.md) for why this matters

### How to Prioritize:

**Large communities (1000+ members):**
- Require: AutoMod, audit logs, raid protection
- Avoid: Platforms with invasive ID verification

**Small communities (<100 members):**
- Sufficient: Basic kick/ban/roles
- Advanced moderation nice to have

**Privacy-focused:**
- **Absolutely avoid**: Any platform with biometric or ID verification
- Prefer: Self-hosted with full control

**See [MODERATION.md](MODERATION.md) for detailed recommendations**

---

## 6. Server & Admin (7 features)

### What This Group Covers:
- Role management, server organization, admin GUI
- Invite links & guest access, migration assistant
- Bridges to other platforms, Discord API compatibility

### Why It Matters:
- **Management**: How easy is it to run your server?
- **Migration**: Can you import data from Discord?
- **Integration**: Connect to other platforms

### Key Features Explained:

**Role Management**
- Assign permissions via roles
- Fine-grained access control
- Essential for organized communities

**Migration Assistant**
- Import data from Discord or other platforms
- Makes switching easier
- Preserves history and structure

**Discord API Compatibility**
- Existing Discord bots work without modification
- Huge ecosystem of existing tools
- Easiest transition from Discord

### How to Prioritize:

**Migrating from Discord:**
- Prefer: Migration assistant, Discord bot compatibility
- Makes transition smoother

**New community:**
- Require: Good role management
- Migration tools not needed

---

## 7. Channels & Content (5 features)

### What This Group Covers:
- Docs/wiki channels, list/task channels, media galleries
- Scheduled announcements, event scheduling

### Why It Matters:
- **Organization**: Structure content beyond just chat
- **Collaboration**: Built-in tools vs external integrations
- **Community engagement**: Events, announcements

### How to Prioritize:

**Documentation-heavy:**
- Prefer: Docs/wiki channels
- Alternative: Use external wiki

**Event-focused:**
- Prefer: Event scheduling built-in
- Alternative: External calendar

**Most communities:**
- These are nice-to-have
- Core chat features matter more

---

## 8. Community Tools (6 features)

### What This Group Covers:
- Bots & automation, webhooks
- Raid planner / group activity tools
- Tournament brackets, rich calendar tools
- Community discovery

### Why It Matters:
- **Automation**: Bots handle repetitive tasks
- **Gaming**: Raid planning, tournaments
- **Growth**: Discovery features help find members

### Key Features Explained:

**Bots & Automation**
- Extend functionality via bots
- Custom commands, automated responses
- Critical for large communities

**Webhooks**
- Connect external services (GitHub, Twitter, etc.)
- Automated notifications
- Integration with other tools

### How to Prioritize:

**Gaming communities:**
- Prefer: Raid planners, event tools
- Bots for game-specific features

**General communities:**
- Require: Bots & webhooks
- Other tools nice to have

---

## Trade-offs to Understand

### Privacy vs Convenience
- **Self-hosted** = Maximum privacy, requires technical skill
- **Cloud-hosted** = Easy to use, trust platform operator

### Features vs Security
- **New platforms** = Latest features, unproven security
- **Mature platforms** = Fewer bleeding-edge features, battle-tested

### Free vs Paid
- **Free tier** = Limited features or users
- **Paid tier** = Full features, ongoing cost
- **Self-hosted** = Full features, server cost

### Centralized vs Federated
- **Centralized** = Easier to use, single point of failure
- **Federated** = More resilient, more complex

---

## Feature Prioritization by Use Case

### For Gaming Communities:
1. Voice quality (low latency)
2. Persistent voice channels
3. Screen sharing with system audio
4. Bots & automation
5. Event/raid planning

### For Privacy-Focused Groups:
1. E2EE
2. Open source
3. Self-hostable or federated
4. No tracking/ads
5. GDPR compliance

### For Large Communities (1000+ users):
1. AutoMod
2. Audit logs
3. Raid protection
4. Role management
5. Scaling capabilities

### For Small Friend Groups:
1. Voice/video quality
2. Mobile apps
3. Easy to use
4. Free tier
5. Everything else is bonus

---

## How to Use the Comparison Table

1. **Start with your must-haves**: What features can't you live without?
2. **Check [COMPARISON.md](COMPARISON.md)**: Filter by required features
3. **Consider trade-offs**: Perfect platform doesn't exist
4. **Read platform notes**: Details matter (marked with †)
5. **Check warnings**: See [SECURITY.md](SECURITY.md) before choosing

---

## Related Pages

- **[COMPARISON.md](COMPARISON.md)** — Full feature comparison table
- **[README.md](README.md)** — Quick start guide
- **[SECURITY.md](SECURITY.md)** — Security warnings
- **[MODERATION.md](MODERATION.md)** — Moderation deep dive

---

*Last updated: February 21, 2026*  
*58 features tracked across 8 groups*

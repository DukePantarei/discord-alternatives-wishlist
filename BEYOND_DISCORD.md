# Beyond Discord: What We Actually Deserve

I've spent weeks researching Discord alternatives for our community of about 100 people. What started as "we need to escape age verification" turned into something bigger: why are we settling for just another Discord clone? If we're going to move anyway, shouldn't we aim for something genuinely better?

Discord revolutionized how gaming communities communicate, but it has fundamental flaws we've all learned to accept as normal. The age verification announcement is just the latest symptom of a deeper problem: when you build your community on someone else's platform, you're always at their mercy. Terms of service changes, feature additions you didn't ask for, surveillance expansion - you accept it all or leave.

But here's what really frustrates me: most Discord "alternatives" just replicate the same problems. They're building Discord clones when they should be building something better. This document outlines what a platform built for communities like ours should actually look like.

---

## What Matters Most

### Self-Hosting: Actually Owning Your Community

The single most important feature isn't a feature at all - it's who controls the infrastructure. When Discord announced mandatory face scans just five months after a breach exposed 70,000 government IDs, we had two choices: comply or leave. That's not ownership.

Self-hosting means running the platform on your own hardware or VPS. Discord raises prices? Doesn't affect you. They add AI training on your messages? Not on your server. They shut down entirely? Your community keeps running. You own the infrastructure, the data, and the rules.

This used to require serious technical expertise, but platforms like Fluxer and Matrix are making it accessible. With relatively minimal hardware (old laptops lying around, business desktops and slim pcs sold on facebook marketplace) a server can host a community of a fairly decent size. Platforms like Conduit make running a Matrix server so lightweight it works on a Raspberry Pi.

The key is easy deployment - Docker containers, simple configuration, good documentation. If it takes more than an afternoon to get running, most people won't bother. The best platforms understand this.

### Searchable, Permanent Knowledge

Many a community has years of troubleshooting knowledge, tutorials, and guides trapped in Discord. When someone Google searches a problem we've already solved, they'll never find our solution because Discord isn't indexed. Discord's "forum channels" made this worse, not better - they're still locked behind Discord's walls. You'll then have to join the discord community, if it is still available, requset the correct permissions, and then sift through tons of documentaiton to find the information you're looking for.

Compare that to traditional forums where solutions live forever and help people who don't even know your community exists. When our Discord server eventually dies - and all servers eventually die - that knowledge disappears with it.

A proper platform should have public-by-default forums that search engines can index, with granular privacy controls for sensitive discussions. Your community's knowledge should outlive the platform. Discourse gets this right, but it's not real-time chat. Matrix can make rooms publicly viewable, but most people don't. A real-time chat platform should focus on exactly that, real-time chat. However, there can be tools provided for easily exporting/creating documentation that is meant to last, and then allowing it to be posted on an indexed forum. I believe the mental model for discord was off base for this, it created insular information sharing rather than community building.

### Gaming Features That Actually Work

Discord started for gamers, then forgot about us. Remember Guilded? It had integrated calendars for raid scheduling, tournament brackets, LFG tools, game server integration. Then Roblox acquired it in 2021 and slowly killed it off. Now we're stuck using a dozen bots to accomplish what Guilded did natively.

**Event scheduling:** I shouldn't need a bot to schedule raid night. I need role-based signups (two tanks, three healers, five DPS), automatic reminders, timezone conversion, and waitlist management. This is basic functionality for gaming communities.

**Tournament support:** We run tournaments. Setting up brackets, tracking scores, notifying players when matches are ready - we do all of this through bots and external sites. A gaming platform should have native tournament tools.

**LFG that works:** Currently, looking for group means typing "LFG Destiny 2 raid, need 1 warlock" and hoping someone sees it. There should be a persistent LFG board with role selection and skill matching. Games have matchmaking - why doesn't our platform?

**Game integration:** When I'm on our Minecraft server, everyone should see the server status without asking. "Is the server up?" "How many people are on?" "What's the IP?" These questions are constant because there's no native game server integration.

The opportunity here is massive. No platform has filled Guilded's void. If someone built a self-hostable platform with Discord's UX and Guilded's gaming features, gaming communities would flood to it.

### Privacy Without Surveillance

Discord scans every message. For "safety," they say, but also for engagement metrics and who knows what else. There's no end-to-end encryption option. Your private conversations aren't private - Discord can read everything.

For most casual chat, this is fine. But communities should have the option for truly private conversations - E2EE for sensitive discussions about health, politics, personal issues. Matrix offers this. Signal has it for DMs. It should be standard, not exceptional.

More importantly: no surveillance capitalism. No AI training on your messages without permission. No behavioral tracking for ads. No "engagement" algorithms. A platform that respects privacy isn't just about encryption - it's about not treating users as products.

### Interoperability: Meeting People Where They Are

Not everyone will move to the same platform. Some people stay on Discord, others prefer Matrix, some use Telegram. Rather than force everyone onto one platform, why not bridge them?

Matrix excels at this - you can bridge Matrix to Discord, Telegram, Slack, IRC. Your Matrix users can talk to Discord users seamlessly. During a migration, you can run both platforms simultaneously, bridging them together until everyone's ready to move.

This also future-proofs your community. If a better platform comes along, you can migrate without losing contact with people who aren't ready to move yet.

### Customization and Accessibility

Discord's one-size-fits-all interface doesn't work for everyone. Some people need dyslexia-friendly fonts. Others want compact mode. Power users want vim keybindings. Communities want custom themes that reflect their identity.

Fluxer allows custom CSS. Matrix has multiple clients with different UIs. The platform should adapt to users, not force users to adapt to it. This is especially important for accessibility - people with disabilities shouldn't be locked out because the platform doesn't support their needs.

### Sustainable Funding Without Venture Capital

Discord's path was predictable: free → VC funding → pressure to monetize → Nitro → not enough revenue → NFTs → crypto → AI features → surveillance expansion. This is the pattern with every VC-backed "free" platform.

Better options exist: community funding (like Patreon for your server), freemium with optional hosted service (free to self-host, paid for managed hosting), or straightforward subscriptions. Fluxer does this well - free and open source to self-host, optional Plutonium subscription on their hosted instance for premium features, and they accept donations from people who self-host.

The key is transparency about costs and alignment of incentives. If the business model requires surveillance or ads, the platform will eventually enshittify. If it's funded by users who want the platform to exist, incentives align.

---

## What Actually Matters for Our Community

After all this research, here's what I think we need, in order of priority:

**Essential:**
1. Self-hostable - We should own our infrastructure
2. Good voice quality - We're gamers, voice matters
3. Discord-like UX - Migration should be easy
4. Active development - The platform should have a future
5. Open source - We should be able to audit and modify it

**Important for gaming:**
6. Event scheduling - Native calendar with role-based signups
7. Tournament tools - Brackets and score tracking
8. LFG functionality - Persistent group finder
9. Game server integration - Status and quick-join

**Important for knowledge:**
10. Searchable public forums - Knowledge that outlasts the platform
11. Complete data export - We should own our history

**Nice to have:**
12. E2EE for sensitive conversations
13. Bridge support for interoperability
14. Custom themes and accessibility
15. Federation (Matrix-style)

Not everything matters equally. We're a gaming community first, so Discord-like UX and gaming features matter more than federation. A study group might prioritize differently. Your community's priorities should drive your choice.

---

## Where We Go From Here

No single platform checks all these boxes yet. Here's the honest assessment:

**Fluxer** comes closest for gaming communities - self-hostable, Discord-like UX, good development momentum, open source. Missing: gaming features (could be added), public forums, federation (planned). Best for communities that want Discord's UX with self-hosting.

**Matrix** wins for privacy and federation - E2EE, truly decentralized, bridges to everything, can make rooms public. Missing: Discord-like UX (though Commet client helps), easy self-hosting (Conduit is getting better), gaming features. Best for communities that prioritize privacy and federation.

**Spacebar** has Discord bot compatibility, which is neat. But it's alpha-stage with voice still in development. Worth watching, not ready yet.

**Discourse** for forums, Matrix/Fluxer for real-time chat might be the hybrid approach. Use each for what it does best.

For our community specifically, I'm leaning toward Fluxer. The self-hosting story is getting simpler, the UX is familiar, and it's the most Discord-like of the self-hostable options. We'd need to use bots for gaming features initially, but the platform is open source - those features could be contributed if there's demand.

But this decision should be democratic. I've built this repository to help us - and communities like ours - make informed decisions. Read the comparison tables, check out the platforms that interest you, and let's decide together what matters most.

The dream platform - self-hostable, gaming-focused, with public forums and Discord's UX - doesn't exist yet. But by documenting what we actually need, maybe we'll inspire someone to build it. Or maybe we'll contribute to making Fluxer or Spacebar or Matrix into that platform.

We're not just escaping Discord's age verification. We're building something better than Discord ever was.

---

**Want to contribute your thoughts?** Open an issue on the repository with features you think should be prioritized, or use this doc to start conversations with your own community about what actually matters to you.

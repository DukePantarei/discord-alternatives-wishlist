# Moderation & Safety Guide

> **Key insight:** The only long-term solution to avoid invasive surveillance is decentralization and self-hosting.

---

## The Privacy vs Safety Tradeoff

**Why this matters:** Discord's planned age verification system (requiring government ID or face scans) is a major privacy concern and a key reason people are seeking alternatives. This repository tracks both traditional moderation tools AND privacy-invasive verification systems.

---

## ⚠️ CRITICAL: The Centralization Problem

**Discord isn't unique — this is a systemic issue with centralized platforms.**

Any centralized, commercial platform (Discord, Slack, Teams, etc.) will eventually face the same government pressure to implement invasive age verification and content monitoring. The UK's Online Safety Act is just the beginning — similar legislation is spreading:

- **UK:** Age verification via ID/face scan (active enforcement 2025)
- **EU:** Digital Services Act requiring content moderation at scale
- **Australia:** Online Safety Act with similar requirements
- **US:** Multiple state laws requiring age verification for "harmful content"

### The Pattern:

1. Government passes "safety" legislation
2. Centralized platforms must comply or face massive fines
3. Platform implements invasive verification (ID upload, biometrics, AI monitoring)
4. User privacy is permanently compromised

**Discord is just the first to announce it publicly.** Other commercial platforms will follow as enforcement ramps up. If you're fleeing Discord for another centralized commercial platform (Root, Osmium, etc.), you're only buying time before they face the same requirements.

---

## The Only Long-Term Solution: Decentralization & Self-Hosting

### Platforms That Can Resist This Pressure:

**Self-hosted** (Rocket.Chat, Mattermost, Discourse, Zulip)
- You control the server, you set the rules
- Not subject to corporate policies
- Can be hosted in privacy-friendly jurisdictions

**Federated** (Matrix, XMPP)
- No central authority to compel
- Enforcement is impractical across independent servers
- Community can fork if project compromises

**Open source**
- Can be forked and run outside jurisdictions with invasive laws
- Community-maintained alternatives always possible
- Code can be audited for backdoors

### Why These Work:

- ✅ No central company to fine or prosecute
- ✅ Can be hosted in privacy-friendly jurisdictions
- ✅ Community can fork if project compromises
- ✅ Enforcement is technically and legally impractical

---

## Privacy-Invasive Verification (Avoid These)

### Discord — Planned Invasive Verification:

**What they're implementing:**
- **Age Verification**: Teen accounts with restricted features by default
- **ID Verification**: Face scanning OR government ID upload required for age-gating
- **UK Pilot (2025)**: Testing biometric age verification
- **Global Rollout (March 2026)**: "Age inference" surveillance in background

**Privacy Impact:**
- Government ID and biometric data stored by third-party vendors (k-ID, Persona)
- Creates honeypot of sensitive data
- Face recognition normalizes surveillance
- Background profiling of all users
- Disproportionate for a chat platform

**Why this is problematic:**
- Platform that leaked 70,000 IDs now demanding more IDs
- Third-party vendors have security issues (Persona frontend exposed, tracks extensive metrics)
- Discord tested Persona, switched to k-ID (after backlash), could switch vendors again
- Peter Thiel (Palantir founder) investment connections to Persona
- Constant surveillance via "age inference model"
- **Business motivations**: Advertiser-friendly data collection, in-app microtransactions, potential IPO
- Vendors like Persona track metrics far beyond age verification — valuable for ad targeting

**The "trusted partners" deception:**
Discord calls age verification vendors **"trusted partners."** But users never chose these partners — **Discord did, based on business interests, not user privacy.**

Users are forced to trust:
- Persona (data breach risks, extensive tracking)
- k-ID (Discord's current choice, no user input)
- Yoti (UK pilot vendor)
- Any future vendor Discord selects

**The problem:** When these "trusted partners" breach user data or misuse it, users suffer the consequences — not Discord, not the vendors. This is a fundamental flaw of for-profit platforms: **vendor selection serves profit maximization, not user protection.** Users have no voice in who handles their most sensitive data.

**See [BACKGROUND.md](BACKGROUND.md) for full story**

---

### Other Centralized Platforms — Not Yet, But Coming:

All major centralized platforms (Slack, Teams, Root, Osmium, etc.) will face the same legislative pressure:
- Compliance is a question of **when, not if**
- Moving from Discord to another centralized platform is a **temporary solution**
- Self-hosting or federation is the only long-term answer

---

## Privacy-Respecting Moderation

These platforms offer strong moderation WITHOUT invasive identity verification:

### Discourse — Trust-Based Moderation

**Features:**
- AutoMod with automatic post hiding
- Trust levels (new users → regulars → leaders)
- Flag system for community reporting
- Audit logs and user silencing
- Spam detection and rate limiting

**Privacy:**
- ✅ Email-based registration (no ID required)
- ✅ No biometric verification
- ✅ GDPR compliant
- ✅ Self-hosted option for full control
- ✅ Open source (can audit)

**Best for:** Forum-style communities, support communities, Q&A

---

### Matrix (Element/Commet/SchildiChat) — Decentralized Moderation

**Features:**
- Draupnir/Mjolnir bots for advanced moderation
- Shared ban lists across federated servers
- Audit logs and user timeouts
- Room moderation and kicks/bans
- Encryption doesn't compromise moderation

**Privacy:**
- ✅ E2EE by default
- ✅ Federated (you choose your homeserver)
- ✅ No central authority
- ✅ Open protocol (can't be shut down)
- ✅ Self-hostable

**Best for:** Privacy-focused communities, activist groups, international communities

**Note:** Check [SECURITY.md](SECURITY.md) for vodozemac vulnerability status before deploying.

---

### Rocket.Chat & Mattermost — Enterprise-Grade

**Features:**
- Message reporting and review queues
- Audit logs for compliance
- Role-based permissions
- Advanced admin controls
- Compliance certifications (HIPAA, SOC2, etc.)

**Privacy:**
- ✅ Self-hosted option means full data control
- ✅ GDPR compliant
- ✅ No biometric verification
- ✅ Open source
- ✅ Enterprise security audits

**Best for:** Businesses, healthcare, regulated industries, large organizations

---

### Discord (Current Features) — Pre-Verification Era

**Features:**
- AutoMod (keyword filters, spam detection, mention limits)
- Raid protection and verification levels
- Audit logs and timeout features
- Message reporting dashboard
- Sophisticated moderation tools

**Privacy:**
- ⚠️ Current Discord is fine
- ❌ Concern is planned 2025+ verification requirements
- ❌ Will require face scans or government ID

**Recommendation:** Current Discord has excellent moderation, but **plan your exit** before age verification rollout forces a rushed migration.

---

## Moderation Feature Levels

### ⚙️ Basic Moderation

**What it includes:**
- Kick/ban users
- Role-based permissions
- Message deletion
- Channel controls
- Basic user blocking

**Sufficient for:**
- Small to medium communities (<500 active members)
- Friend groups
- Private communities

**May struggle with:**
- Large public communities
- Active raids/spam
- Coordinated harassment
- Bot attacks

**Platforms with basic moderation:**
- Most self-hosted alternatives
- Smaller open source projects
- Gaming-focused platforms

---

### 🛡️ Advanced Moderation

**What it includes:**
- AutoMod (automated content filtering)
- Raid protection
- Audit logs
- User timeouts/mutes
- Message reporting systems
- Trust levels or reputation systems

**Sufficient for:**
- Large communities (500-10,000+ members)
- Public communities
- Communities with moderation teams

**Platforms with advanced moderation:**
- Discord (current)
- Discourse
- Matrix (with Draupnir/Mjolnir bots)
- Rocket.Chat
- Mattermost
- Slack/Teams

---

## The "Cars Analogy"

**The privacy vs safety argument, explained:**

> "Criminals also use cars, but should we require face ID scanning and GPS tracking while operating any vehicle?"

**The point:**
- Yes, cars can be used for crime
- Yes, we need some safety measures (licenses, speed limits)
- **No,** we don't require biometric scanning of every driver
- **No,** we don't mandate GPS tracking on every car
- The privacy invasion would be **disproportionate to the risk**

**Same applies to chat platforms:**
- Yes, children need protection online
- Yes, we need moderation tools
- **No,** we don't need biometric face scans of every user
- **No,** we don't need government ID uploads to chat
- The privacy invasion is **disproportionate to the risk**

**Better solutions exist:**
- Trust-based moderation (Discourse)
- Community moderation (Matrix)
- Parental controls (actual parents, not corporations)
- Education about online safety
- Strong moderation tools WITHOUT identity verification

---

## The "Protecting Children" Narrative: Co-opted for Surveillance

**CRITICAL CONTEXT:** As [penguinz0](https://youtu.be/jkhMx9hEsK0) and [SomeOrdinaryGamers](https://youtu.be/MTK-R4mrwLA) have analyzed, the "protecting children" narrative is being **weaponized by corporations and governments** to justify mass surveillance and data collection.

### The Real Purpose

**What they say:**
- "We need to verify ages to protect children"
- "This is about keeping kids safe online"
- "Anyone against this doesn't care about children"

**What's actually happening:**
- **Corporations:** Building surveillance infrastructure to collect behavioral data for advertisers
- **Governments:** Establishing precedent for requiring ID/biometrics to access online spaces
- **Both:** Using "child safety" as unassailable justification that shuts down debate

**The proof:**
- Discord went **beyond legal requirements** (EFF noted this)
- Chose vendors that **track far more than age** (Persona's extensive metrics)
- Implemented **surveillance of all users** (not just children via "age inference")
- Pattern repeating across platforms: Meta, Roblox, Reddit, Snap, Instagram

**The actual goal:** Create a surveillance state where:
1. All online activity requires identity verification
2. Anonymous speech becomes impossible
3. Dissent can be tracked and quelled
4. Corporations monetize verified identity + behavioral data
5. "Protecting children" provides political cover

### Where Is Parental Accountability?

**The uncomfortable truth:** Parents are being let off the hook while everyone else loses privacy.

**The reality:**
- Parents provide children smartphones and tablets
- Parents allow **unfettered internet access**
- Parents use devices as **distraction/babysitting tools**
- Parents don't monitor, limit, or educate about online use
- When problems arise, **corporations are blamed instead of parents**

**The solution being pushed:**
- Don't hold parents accountable
- Don't expect parental supervision
- Instead: **Surveill everyone** (adults and children)
- Result: Privacy lost, children still unsupervised

**What actually works:**
- Parental monitoring and involvement
- Limited, supervised internet access for children
- Education about online risks
- Age-appropriate content controls **set by parents**
- Actual engagement with what children do online

**Personal perspective:** As someone who had unfettered internet access in both my own and the internet's formative years, I wouldn't allow children the same. The internet has become far more polarizing and dangerous. If children need access, it should be:
- Properly explained
- Actively monitored  
- Appropriately limited
- Supervised by parents, not corporations

### The Detrimental Effects (Being Ignored)

**Device addiction and unfettered access cause:**
- Decreased attention spans
- Disrupted dopamine production
- Lack of interest in non-screen activities
- Increased anxiety and depression
- Social development issues
- Sleep disruption
- Reduced physical activity

**But instead of addressing these:**
- We're implementing mass surveillance
- We're normalizing biometric data collection
- We're teaching children privacy doesn't matter
- We're making the internet require ID verification
- **We're solving the wrong problem**

### The Systemic Economic Context

**Why parents struggle:** This isn't just individual failure - it's systemic.

**Under capitalism, we've created the "cost of living crisis":**

**Wage stagnation:**
- Real wages haven't kept pace with costs
- Single income can't support most families
- Both parents must work to survive

**Childcare crisis:**
- Daycare costs have skyrocketed ($15,000-$30,000/year)
- Reinforces need for both parents to work
- Catches families in impossible bind
- Can't afford childcare, can't afford not to work

**The impossible situation:**
```
Can't afford childcare → Both parents work
Both parents work → No time for supervision
No supervision → Children get devices
Devices = free "babysitting" → Unfettered access
Unfettered access → "Think of the children!"
→ Mass surveillance instead of addressing root causes
```

**The dream is dead:**
- Single income supporting family: **Out of reach** for most
- Stay-at-home parent: **Economic impossibility**
- Constant caregiver presence: **Unaffordable luxury**
- Family time: **Squeezed by work demands**

**The broader impacts:**

**Declining birth rates:**
- Couples choose not to have children
- Can't afford expenses with little support
- Especially professionals who moved for work (away from family help)
- Economic calculation: Children = financial ruin

**Loneliness epidemic:**
- Both genders more exhausted than ever
- Little time to socialize
- No energy for meaningful partnerships
- Work consumes life, relationships suffer

### The Solution Being Ignored

**What should happen:**
1. **Economic reform:** Living wages, affordable childcare, parental leave
2. **Parental accountability:** Actual supervision, not device babysitting
3. **Education:** Teach parents and children about online safety
4. **Privacy-respecting moderation:** Tools that don't surveill everyone
5. **Community support:** Extended family, community childcare, social infrastructure

**What's happening instead:**
1. **Mass surveillance:** Everyone loses privacy
2. **Corporate profit:** Data collection disguised as child safety
3. **Government control:** Establishing precedent for ID verification online
4. **Systemic issues:** Completely ignored
5. **Parents:** Still not accountable, still giving kids devices

### The Bottom Line

**The "protecting children" narrative is being weaponized to:**
- Build surveillance infrastructure
- Normalize identity verification for online access
- Collect data for corporate profit
- Track and quell dissent
- Establish government control over online speech

**While the real problems go unaddressed:**
- Economic systems forcing both parents to work
- Lack of affordable childcare
- Parental accountability
- Device addiction and mental health impacts
- Systemic inequality and cost of living

**We shouldn't have to sacrifice everyone's privacy because:**
- Parents are economically forced to work constant hours
- Devices are cheaper than childcare
- Corporations want surveillance infrastructure
- Governments want to track citizens

**The reality:** "Protecting children" is the excuse. **Surveillance and data collection is the goal.** Parental accountability and systemic economic reform are the ignored solutions.

**As SomeOrdinaryGamers points out:** This is about control, data, and profit - not child safety. If it were about child safety, we'd be addressing parental supervision and economic systems, not building a surveillance state.

---

## Platform Recommendations

### For Large Communities Needing Strong Moderation

**Best options:**
1. **Discourse** — Forum-style, exceptional moderation, no ID required
2. **Matrix + Draupnir** — Chat-style, federated, strong moderation with privacy
3. **Rocket.Chat/Mattermost** — Enterprise-grade tools, self-hosted option

**Avoid:**
- Discord (after age verification rollout)
- Commercial platforms that will face same pressure

---

### For Privacy-First Communities

**Best options:**
1. **Matrix** (Element, Commet) — E2EE, federated, no central authority
2. **SimpleX Chat** — No user identifiers, maximum privacy
3. **Self-hosted platforms** — Full control over data

**Accept tradeoff:**
- May need to implement moderation via bots (Matrix)
- Smaller user base initially
- More technical setup

---

### For Gaming Communities

**Best options:**
1. **Steam Chat** — 350M+ gamers, built-in moderation
2. **TeamSpeak** — Low-latency voice, self-hosted option
3. **Mumble** — Open source, self-hosted, excellent voice quality

**Consider:**
- Gaming communities may prioritize voice quality over text moderation
- Can use multiple platforms (Steam for voice, Matrix for text)

---

## Bottom Line

### For Large Communities with Moderation Needs:

**Privacy-focused + good moderation:**
- Discourse (forums)
- Matrix with Draupnir (chat)

**Best moderation, some privacy concerns:**
- Current Discord (before verification rollout)
- Slack/Teams (if comfortable with commercial)

**Avoid:**
- Discord after age/ID verification rollout (2025+)
- Any platform that implements face scanning or ID upload

---

### For Small/Medium Communities:

- Most alternatives have sufficient moderation tools
- **Prioritize privacy, self-hosting, and federation over advanced moderation**
- Basic moderation (kick/ban/roles) is usually enough

---

### The Recommendation Hierarchy:

1. **Best:** Self-hosted + open source + strong moderation (Discourse, Zulip)
2. **Good:** Federated + privacy-focused + decent moderation (Matrix)
3. **Acceptable:** Current Discord (plan exit before verification)
4. **Avoid:** Discord post-verification, any platform with ID/face scanning

---

## Related Pages

- **[BACKGROUND.md](BACKGROUND.md)** — Full Discord exodus story and why this matters
- **[SECURITY.md](SECURITY.md)** — Vibe-coded platforms and security incidents
- **[README.md](README.md)** — Quick start guide
- **[COMPARISON.md](COMPARISON.md)** — Full moderation feature comparison

---

*Last updated: February 21, 2026*  
*Moderation features updated to include privacy-invasive verification tracking*

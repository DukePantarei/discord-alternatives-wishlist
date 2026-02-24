# Security Guide

> **Critical:** Three platforms currently have active security incidents. Check warnings below before choosing a platform.

---

## ⚠️ ACTIVE SECURITY INCIDENTS

### Matrix Ecosystem - CRYPTOGRAPHIC VULNERABILITY (Feb 17, 2026)

⚠️ **Cryptographic issues discovered in Matrix's Rust library (vodozemac)**

**Affected platforms:**
- Element
- Commet
- FluffyChat
- All Matrix clients using vodozemac library

**Details:**
- Discovered by cryptography researcher
- Impacts end-to-end encryption reliability
- **Source**: [Soatok's cryptographic analysis](https://soatok.blog/2026/02/17/cryptographic-issues-in-matrixs-rust-library-vodozemac/)

**Recommendation:** Monitor for patches from Matrix.org before using for sensitive communications. This is a recent discovery; users should check for updates before deploying.

---

### Kloak - CRITICAL BREACH (Feb 20, 2026)

❌ **DO NOT USE** - Active security compromise

**What happened:**
- Attacker demonstrated ability to access full user list and private messages
- Users received unsolicited mass messages from compromised account
- Account creation disabled for hours following incident
- Breach pattern similar to Paracord (suggests possible vibe-coded origin)

**Current status:**
- No security audit or incident response available
- No transparency from developers
- Platform security fundamentally compromised

**Recommendation:** Delete account immediately if you have one. Do not use until comprehensive security audit is published.

---

### Paracord - Known Vulnerabilities (Feb 2025)

❌ **DO NOT USE** - 20+ critical security flaws documented

**Community security audit found:**
- Unauthenticated LiveKit proxy (anyone can join voice calls silently)
- Remote code execution via admin endpoint
- JWT secrets stored in plaintext
- Rate limiting trivially bypassed
- CORS allows any origin
- UPnP auto-opens router ports (exposes server to internet)

**The irony:** Marketed as "privacy-focused Discord alternative" but has worse security than Discord.

**Developer's admission:** Built "in a few evenings" using AI. [Community response](https://github.com/Scdouglas1999/Paracord): "This got absolutely rekt on arrival."

**Status:** Confirmed AI-generated with no security review. DO NOT USE under any circumstances.

---

## 🤖 What is "Vibe-Coding"?

**Definition:** Creating software primarily using AI code generation tools (ChatGPT, Claude, Copilot) rather than traditional software development.

**Why it matters for security:**
- AI can accelerate development BUT security-critical applications require expert review
- AI tools don't understand threat models or security implications
- Subtle vulnerabilities are invisible to AI
- Security requires expertise, not just working code

**When AI-generated code is problematic:**
- Authentication systems
- Encryption implementations
- Network protocols
- Access control
- Data validation
- Security-critical applications (like chat platforms handling private data)

**When AI can be helpful:**
- UI components
- Boilerplate code
- Standard CRUD operations
- Non-security-critical features
- **With proper human review and testing**

---

## Platforms to Scrutinize

### ❌ Confirmed AI-Generated (Proceed with Extreme Caution)

**Paracord** — DO NOT USE
- 20+ critical vulnerabilities documented
- Built "in a few evenings" using AI
- No security review
- Community security audit exposed fundamental flaws

**Blite Chat** — Caution
- Explicitly AI-generated
- Security status unknown
- No known audit

**Voltage/VoltChat** — Untested
- Very new (Feb 2026)
- Strong vibe-coding indicators
- No security audit
- Use at your own risk

**Discourse** — Community Assessment
- Community marked as "NOT vibe-safe"
- Has AI plugin, marked "Bad" security in Google Sheet
- However: Mature platform with years of use
- Enterprise adoption suggests some vetting

**Virola, Osmium, Rocket.Chat, Root** — Community Assessment
- All marked "NOT vibe-safe" by Google Sheet community (Feb 2026)
- Rocket.Chat: "Advertises AI features heavily"
- Root: ALSO SUSPICIOUS - NFT-VC backed, no revenue model, features don't exist
- Proceed with caution

---

### ✅ Responsible AI Use (Transparent, Reviewed, Tested)

These platforms use AI responsibly - as a development tool, not a replacement for expertise:

**Stoat (formerly Revolt)**
- Previously had AI commits, removed after community backlash
- Developer statement: "Stoat's foundation predates vibe-coding"
- Anti-AI stance since cleanup

**Fluxer**
- Developer uses AI as "rubber duck" debugging tool
- All code written personally
- AI used for discussion/brainstorming, not code generation
- Blog: [How I Built Fluxer](https://blog.fluxer.app/how-i-built-fluxer-a-discord-like-chat-app/)

**Echoed**
- Backend coded from scratch
- Frontend has "bits and pieces" of AI assistance
- Developer transparent about AI use

**Oldcord**
- Explicitly bans AI-generated code: "We don't use AI to generate any of our code"
- Does not accept AI-generated contributions
- Uses AI only for style checking

**Spacebar/Fermi**
- Explicitly bans AI code: "AI code due to not being GPLv3 compatible is not allowed"
- Technical license restrictions prevent AI usage

**Zulip** — Exemplary Policy
- Permits AI assistance BUT strictly disallows AI commits with zero oversight
- All AI code must be reviewed and verified
- Policy: [CONTRIBUTING.md](https://github.com/zulip/zulip/blob/main/CONTRIBUTING.md)
- This is the gold standard for responsible AI use

**Freenet**
- Transparent: "Some codebase written with extensive AI assistance"
- All code reviewed, tested, refined by humans
- Extensive testing: unit tests, integration tests, network simulations
- Small team using AI for productivity, all code validated

**Critterchat**
- Explicitly states: "Not built with, enabled by or integrated with any generative AI"
- Clear anti-AI stance
- 482 commits, active development

---

## 🔍 How to Identify Vibe-Coded Platforms

### Suspicious Indicators:
- ⚠️ Single large commit (developed privately, dumped publicly)
- ⚠️ Rapid development timeline ("built in a weekend")
- ⚠️ Minimal documentation
- ⚠️ No development history visible
- ⚠️ "Privacy-focused" claims without security audit
- ⚠️ Developer can't explain security architecture when asked
- ⚠️ Very new platform with full feature set

### Safe Indicators:
- ✅ Active development history (not single commit)
- ✅ Security audits by reputable firms
- ✅ Used by established organizations
- ✅ Years of production use
- ✅ Active security vulnerability disclosure process
- ✅ Community code review
- ✅ Transparent about AI usage (if any)

---

## Security Best Practices

### Before Choosing a Platform

1. **Check this page** for active incidents
2. **Review development history** on GitHub
3. **Look for security audits** by reputable firms
4. **Check who's using it** - Established orgs or just new users?
5. **Read the code** if you're technical
6. **Search for vulnerability reports** - Responsible disclosure?

### Red Flags to Watch For

- ❌ New platform without track record
- ❌ "Built quickly" as selling point
- ❌ No security audit
- ❌ Developer can't explain security architecture
- ❌ Single developer with no security background
- ❌ Recent security incident with no response
- ❌ Promises of "military-grade encryption" without details

### What to Do If Breached

1. Change passwords immediately
2. Enable 2FA if available
3. Review who has access to your data
4. Consider migrating to more secure platform
5. Report incident to platform
6. Warn your community

---

## Recommendations by Use Case

### For Privacy-Critical Use Cases:

**Prefer established, audited platforms:**
1. **Matrix** (Element, Commet, SchildiChat) — Years of hardening, but monitor vodozemac fix
2. **Signal** — Gold standard for encrypted messaging
3. **Rocket.Chat** — Enterprise-grade, widely deployed
4. **Zulip** — Strong security practices, bug bounty program

**Avoid:**
- Brand new platforms without security review
- Platforms marketed on development speed
- Solo projects claiming "privacy-focused" without audits
- Any platform with active security incidents (Kloak, Paracord)

### For Gaming Communities:

**Lower risk tolerance OK:**
- Discord (pre-age-verification) — Battle-tested, good security
- Steam Chat — Backed by Valve
- TeamSpeak — Decades of production use

**Medium risk:**
- Stoat, Fluxer — Open source, community-reviewed
- Spacebar — Discord-compatible, active development

**Avoid:**
- Anything with active incidents
- Untested new platforms

### For Large Organizations:

**Enterprise-grade only:**
- Mattermost — E2EE, compliance certifications
- Rocket.Chat — HIPAA compliant, extensive auditing
- Zulip — Bug bounty, rapid security response
- Slack/Teams — If comfortable with commercial platforms

---

## The Repository Tracks AI-Generated Codebases

This repository includes an `ai_generated_codebase` feature specifically to help you make informed decisions. Being transparent about development methodology is crucial for security-critical applications like chat platforms.

**Our philosophy:**
- AI use is NOT automatically bad
- Transparency is essential
- Security review is mandatory
- Users deserve to know

---

## Related Pages

- **[BACKGROUND.md](BACKGROUND.md)** — Why Discord's security matters
- **[MODERATION.md](MODERATION.md)** — Privacy-respecting vs invasive verification
- **[README.md](README.md)** — Quick start guide
- **[COMPARISON.md](COMPARISON.md)** — Full security feature comparison

---

*Last updated: February 21, 2026*  
*Active incidents checked: Matrix (Feb 17), Kloak (Feb 20), Paracord (ongoing)*

# Architecture Types Explained

Understanding the difference between "centralized," "self-hostable," and "federated" is crucial when choosing a Discord alternative.

---

## Core Definitions

These terms are often confused because they describe **different aspects** of a platform:

### Open Source vs Closed Source (Code Availability)

**Open Source:**
- Source code is publicly available
- Anyone can inspect, modify, and contribute
- Usually free to use and self-host
- Examples: Stoat, Matrix, Spacebar, Linux

**Closed Source (Proprietary):**
- Source code is secret
- Only the company can see/modify it
- Often requires payment or has restrictions
- Examples: Discord, Slack, Microsoft Teams

**Key Point:** Open source tells you about **code transparency**, NOT about how servers work.

---

### Centralized vs Decentralized (Server Control)

**Centralized:**
- One entity controls the server(s)
- All users connect to the same network
- Single point of control
- Examples: Discord (closed source, centralized), Stoat (open source, centralized)

**Decentralized:**
- Multiple independent servers/entities
- Can be federated (servers talk to each other) OR isolated (they don't)
- No single point of control
- Examples: Matrix (federated), Stoat when self-hosted (isolated instances)

**Key Point:** Centralized tells you about **control structure**, NOT about code availability.

---

### Federated vs Non-Federated (Server Communication)

**Federated:**
- Multiple servers that communicate with each other
- Users on any server can interact with users on any other server
- Portable identity across servers
- Examples: Matrix, XMPP, Mastodon, email

**Non-Federated (Isolated):**
- Servers exist but don't communicate
- Each server is its own separate network
- Requires different account per server
- Examples: Stoat instances, Spacebar instances, Discord (only one official server anyway)

**Key Point:** Federation tells you about **server interoperability**, NOT about centralization.

---

## Yes, Stoat is BOTH Open Source AND Centralized!

This confuses people, but it's completely valid:

### Stoat's Architecture:

**Open Source:** ✅ YES
- Source code on GitHub: https://github.com/stoatchat
- Anyone can read, modify, fork the code
- Can self-host using their code

**Centralized:** ✅ YES
- Official instance at stoat.chat run by Stoat team
- Most users use this single central instance
- One company/team controls the main network

**Federated:** ❌ NO
- Self-hosted instances can't talk to each other
- Can't talk to stoat.chat from your own instance
- Each instance is completely isolated

### Why This Works:

**Analogy:** 
Think of it like restaurant recipes:
- **Open Source:** Recipe is published, anyone can use it
- **Centralized:** Most people eat at the main restaurant
- **Non-Federated:** Each restaurant using the recipe is separate - no shared menu or customers

**Stoat is like:**
- Open recipe (open source) ✅
- Main restaurant most people use (centralized) ✅
- Each restaurant is independent, no shared system (non-federated) ✅

---

## Common Combinations

| Platform | Open/Closed | Centralized/Decentralized | Federated | Example |
|----------|-------------|---------------------------|-----------|---------|
| **Discord** | Closed | Centralized | No | One company, secret code, one network |
| **Stoat** | Open | Centralized* | No | Main instance + isolated self-hosted copies |
| **Matrix** | Open | Decentralized | Yes | Many servers, all interconnected |
| **Telegram** | Closed | Centralized | No | One company, secret code, one network |
| **Spacebar** | Open | Centralized* | No | Similar to Stoat - main instance + isolated copies |

*Centralized in practice (main instance), but technically allows decentralized self-hosting (isolated instances)

---

## Why "Open Source + Centralized" Matters

### What You Gain:
- ✅ **Trust:** Can verify code doesn't have backdoors
- ✅ **Transparency:** See exactly how it works
- ✅ **Option to Self-Host:** Can run your own if you want
- ✅ **Community Contributions:** Others can improve it

### What You Don't Gain (without federation):
- ❌ **Network Effects:** Self-hosting means starting over, not joining larger network
- ❌ **Portable Identity:** Need new account per instance
- ❌ **Cross-Instance Communication:** Can't talk to users on other instances

### Real-World Impact:

**Scenario:** Stoat.chat changes their age verification policy

**If you use stoat.chat:**
- ❌ You're subject to their policy (like Discord)
- ✅ But you CAN self-host to escape (unlike Discord)

**If you self-host:**
- ✅ Your rules, your server
- ❌ But you lose access to all users on stoat.chat
- ❌ And can't talk to other self-hosted instances

**Compare to Matrix:**
- If matrix.org changes policy, switch to another server
- ✅ Keep all your contacts and rooms
- ✅ Still talk to everyone on matrix.org
- ✅ Portable identity

---

## The Spectrum

### 1. Centralized (Not Self-Hostable)
**Example:** Discord, Telegram, Slack

**How it works:**
- One company runs all the servers
- You must use their servers
- They control everything

**Pros:**
- Easy to use
- No technical knowledge needed
- Always up-to-date

**Cons:**
- Company has full control
- Can change policies anytime (age verification, data collection)
- Can shut down or change pricing
- Single point of failure

---

### 2. Self-Hostable but NOT Federated (Isolated Instances)
**Examples:** Stoat/Revolt, Spacebar, Rocket.Chat (free tier)

**How it works:**
- You CAN run your own server
- BUT each server is completely isolated
- Users on Server A cannot talk to users on Server B
- Like running your own private Discord

**Analogy:** 
Think of it like email if every company had its own email system and Gmail users couldn't email Outlook users. Each instance is its own island.

**Pros:**
- You control your own server
- No corporate surveillance on YOUR instance
- Can customize and modify
- Your data stays with you

**Cons:**
- Each instance requires separate account
- Cannot communicate across instances
- Hosting your own = starting from scratch
- Fragmenting your community if some self-host

**When this works well:**
- Single community/organization (company, gaming clan, friend group)
- Want privacy/control but don't need to talk to other instances
- Willing to manage your own server

**When this doesn't work:**
- Want to be part of a larger network
- Users scattered across multiple communities
- Want portable identity across servers

---

### 3. Federated (Interconnected Instances)
**Examples:** Matrix (Element, Cinny, Commet), XMPP, Mastodon

**How it works:**
- Anyone can run a server
- All servers talk to each other
- Users on ANY server can talk to users on ANY other server
- One account works everywhere

**Analogy:**
Like email - Gmail users can email Outlook users. You pick your server, but can talk to everyone.

**Pros:**
- Best of both worlds: control + connectivity
- One account, access everywhere
- No single point of control
- Can switch servers without losing contacts
- Portable identity

**Cons:**
- More complex to understand
- Server choice matters (moderation, privacy, speed)
- Some servers may defederate (block each other)

---

### 4. Peer-to-Peer (No Servers)
**Examples:** RetroShare, Tox, Jami

**How it works:**
- No central servers at all
- Devices connect directly to each other
- Fully decentralized

**Pros:**
- Maximum privacy
- Censorship-resistant
- No hosting costs

**Cons:**
- Both parties must be online simultaneously
- Complex to set up
- Limited features compared to server-based

---

## Common Confusion: Stoat/Revolt

### Question 1: "Stoat is open source, so isn't it decentralized?"

**Answer:** No. **Open source ≠ decentralized.**

- **Open Source** = Code is public (transparency)
- **Decentralized** = Multiple independent servers (control structure)
- **You can have one without the other!**

**Stoat is:**
- ✅ Open source (code on GitHub)
- ✅ Centralized in practice (stoat.chat is the main instance)
- ❌ Not federated (instances can't talk to each other)

### Question 2: "Stoat is self-hostable, so isn't it decentralized?"

**Answer:** Technically yes, but practically no. Here's why:

**Stoat's Reality:**
- **Official instance (stoat.chat):** Centralized, most users are here
- **Self-hosted instances:** Technically decentralized (you run your own), but isolated
- **Network effect:** 99% of users on stoat.chat = effectively centralized

**What this means in practice:**

- **Self-hostable:** ✅ Yes, you can run your own Stoat server
- **Federated:** ❌ No, your Stoat server CANNOT talk to other Stoat servers
- **Decentralized:** ❌ No, it's just self-hosted centralization

**What this means in practice:**

Imagine you run `stoat.yourguild.com` for your gaming clan.

**What you CAN do:**
- Full control over your instance
- Your data on your server
- Customize it however you want

**What you CANNOT do:**
- Users on `stoat.yourguild.com` talk to users on `stoat.anotherguild.com`
- They need separate accounts on each instance
- No shared channels or servers across instances

**Compare to Matrix:**

If you run `matrix.yourguild.com` (a Matrix homeserver):
- Users on your server CAN talk to users on `matrix.org` or any other Matrix server
- One account, access to the entire Matrix network
- Can join rooms hosted on other servers

---

## Which Architecture Is Best?

### Choose Centralized if:
- You want the easiest experience
- Don't care about corporate control
- Trust the company running it

### Choose Self-Hostable (Isolated) if:
- Single community that doesn't need to talk to others
- Want control and privacy
- Comfortable managing a server
- Don't mind starting your own network

### Choose Federated if:
- Want both control AND connectivity
- Need portable identity
- Community spans multiple servers
- Want to be part of larger network

### Choose P2P if:
- Maximum privacy is paramount
- Small group communication
- Comfortable with technical complexity

---

## Summary Table

| Type | Examples | Control | Privacy | Connectivity | Complexity |
|------|----------|---------|---------|--------------|------------|
| **Centralized** | Discord, Telegram | ❌ Company | ❌ Low | ✅ High | ✅ Easy |
| **Self-Hosted (Isolated)** | Stoat, Spacebar | ✅ You | ✅ High | ❌ None | ⚠️ Medium |
| **Federated** | Matrix, XMPP | ✅ You | ✅ High | ✅ High | ⚠️ Medium |
| **P2P** | RetroShare, Tox | ✅ You | ✅✅ Maximum | ⚠️ Limited | ❌ Hard |

---

## Key Takeaway

**"Self-hostable" does NOT automatically mean "federated" or "decentralized."**

- Stoat is self-hostable but creates isolated islands
- Matrix is self-hostable AND federated (interconnected)
- Discord is neither (centralized only)

When choosing a platform, consider:
1. Do you need to talk to users on other servers?
2. Do you want a portable identity?
3. Are you okay with isolated instances?

If yes to #1 and #2, you need **federated**, not just **self-hostable**.

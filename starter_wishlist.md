# Starter Wishlist

This document captures the initial feature ideas sourced from the [original Reddit post](https://www.reddit.com/r/matrixdotorg/comments/1r50sqi/) and community discussion. Each item here should eventually become its own Discussion thread where the community can vote and comment.

Items are marked with their current status across the Matrix ecosystem.

---

## Legend

| Symbol | Meaning |
|---|---|
| ✅ | Already exists somewhere in the Matrix ecosystem |
| ⚠️ | Partially exists but needs improvement |
| ❌ | Does not yet exist — genuine gap |

---

## Migration

### ❌ Discord Migration Assistant
A tool that imports a Discord server's structure into a Matrix Space — including channels, categories, roles, and optionally backfilling message history.

**Why it matters:** The single biggest barrier to migration. Rebuilding a large community from scratch is impractical and discourages switching.

**Related:** DiscordChatExporter can export messages, but there's no tool to import them into Matrix natively.

---

### ⚠️ Server Template Export/Import
The ability to save a Space/Room structure as a reusable template, similar to Discord's server templates feature.

---

## Identity & Access

### ❌ Frictionless Invite Links with Guest/Anonymous Access
A shareable invite URL that lets new users join a room without creating an account first — similar to how Discord invite links work, which was a key reason Discord overtook TeamSpeak, Mumble, and Ventrilo.

**Why it matters:** Removing friction is the single most important factor in getting non-technical users to switch. If joining requires account creation, many casual users won't bother.

**Note:** Matrix has some guest access support but it is inconsistent across clients and rarely surfaced in UI.

---

### ✅ Profile / Nickname / Avatar Switching
The ability to set different display names and avatars per Space or community.

**Status:** Exists in the Matrix protocol. Client support varies — check your client's settings.

---

### ⚠️ Role Management
Fine-grained roles with specific permissions assignable to users, similar to Discord's role system.

**Status:** Matrix has power levels which serve a similar function, but the UX is less intuitive than Discord's role system. This is primarily a client-side improvement.

---

## Voice & Video

### ✅ Native Voice and Video Chat
Real-time voice and video calls within rooms and channels.

**Status:** Exists via MatrixRTC + LiveKit. Works well and scales. Supported in Element, Commet, and others.

---

### ⚠️ Screen Sharing with System Audio
Share your screen including system audio (not just microphone), useful for watching videos together or streaming games.

**Status:** Screen sharing exists. System audio capture is the missing piece, particularly on Linux.

---

## Bots & Automation

### ✅ Bot Creation & Automation
The ability to create and run automated bots that respond to commands, moderate rooms, post scheduled messages, etc.

**Status:** Fully supported via the Matrix API. maubot is a popular framework. Appservices allow deeper integrations.

---

### Webhook Support (Discord-style)
Simple incoming webhooks that allow external services to post messages to a room without a full bot setup.

**Status:** Some bridges exist but a simple, standardized webhook URL system like Discord's does not yet exist natively.

---

## Server Organization

### ⚠️ Space / Room Onboarding and Education
Clear, intuitive onboarding that explains the Matrix concept of Homeservers → Spaces → Rooms to users coming from Discord's Server → Category → Channel model.

**Why it matters:** The conceptual mismatch is one of the most common points of confusion for new Matrix users. This is primarily a UI/UX and documentation problem, not a protocol problem.

---

### ⚠️ Admin GUI
A polished, comprehensive graphical interface for server/space administrators to manage users, rooms, permissions, and moderation.

**Status:** Element Admin and Synapse-Admin exist. Draupnir helps with moderation. More polish and consolidation needed.

---

## Events & Scheduling

### ✅ Event Schedule / Calendar
The ability to create and display scheduled events within a community, with RSVP functionality.

**Status:** Exists in Commet. Not universally available across all clients.

---

### ❌ Raid Planner / Group Activity Coordination
Structured tools for organizing group activities — raid sign-ups, role assignments, attendance tracking — as popularized by Guilded before its acquisition by Roblox.

**Why it matters:** Gaming communities specifically need this. It was one of Guilded's strongest differentiators.

---

## UI/UX & Onboarding

### ❌ Polished Consumer-Facing Client
A single, well-maintained Matrix client that prioritizes ease of use for non-technical users coming from Discord — with a familiar layout, intuitive onboarding, and consistent feature set.

**Why it matters:** Element is the reference client but is explicitly enterprise-focused. Cinny and Commet are promising but still maturing. This may be the most impactful single gap in the ecosystem.

---

### ⚠️ Web Interface for Easy Community Joining
A web-based interface that allows new users to browse and join communities without installing an app first.

**Status:** Most clients have a web version. The friction is more in account creation and server discovery than the interface itself.

---

## Installation & Self-Hosting

### ✅ Easy Docker-Based Deployment
A stable, well-documented Docker Compose stack for self-hosting a Matrix homeserver.

**Status:** Fully exists. matrix-docker-ansible-deploy and ESS (Element Server Suite) are the two main options. Good documentation available.

---

## Platform Support

### ⚠️ Consistent Cross-Platform Apps
Stable, feature-consistent clients across Web, Windows, macOS, Linux, Android, and iOS.

**Status:** Most major clients cover these platforms but feature parity between platforms varies. Mobile clients in particular tend to lag behind desktop.

---

*This starter list is a snapshot. The real wishlist lives in [Discussions](../../discussions) where you can vote, comment, and add new ideas.*

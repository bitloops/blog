---
title: "Obsidian, Markdown Files, and Duct Tape: How Developers Are Hacking Memory Into AI Agents"
subtitle: "The fact that developers are building second brains for their AI tells you everything about what's missing from the toolchain."
description: "Developers are using Obsidian vaults, CLAUDE.md files, and markdown hacks to give AI coding agents persistent memory. Here's why these workarounds exist — and what actually needs to change."
author: Sergio
date: 06-April-2026
image: https://storage.googleapis.com/bitloops-github-assets/Blog%20Images/obsidian-markdown-files-and-duct-tape/scattered-stick.png
tags:
  [
    "AI Coding",
    "Context Engineering",
    "Developer Productivity",
    "Software Architecture",
    "Bitloops"
  ]
---

A developer on Reddit recently described their workflow: they'd wired up an Obsidian vault as a "persistent brain" for Claude. Every session, they'd manually update a context file with what the AI learned last time — architecture decisions, rejected approaches, naming conventions. Before each new session, they'd feed this file back in so the agent didn't start from zero.

The post blew up. Hundreds of upvotes. Dozens of comments from developers sharing their own versions of the same hack. Some were using CLAUDE.md files. Others had built elaborate folder structures with templates and daily notes. One person described maintaining a separate "decisions log" they'd paste into every new conversation.

Every single one of these developers had independently arrived at the same conclusion: **AI coding agents are brilliant reasoners with total amnesia**, and the only way to compensate is to become the agent's external memory system.

That's not a productivity hack. That's a missing layer in the toolchain.

## The 165:1 ratio that explains everything

Someone recently tracked their Claude Code token usage across a month of real work. The numbers were striking: 100 million tokens consumed. Of those, 99.4% were input tokens — reading. Only 0.6% were output — writing. A 165:1 read-to-write ratio.

Every single request, the agent re-reads the codebase from scratch. It has no way to carry forward what it learned in the previous turn, let alone the previous session. Close the terminal, and everything evaporates. Open a new session Wednesday morning, and Monday's forty-five-minute architecture discussion might as well have never happened.

The cost isn't just tokens. It's the compounding waste: the same files parsed again and again, the same relationships re-discovered, the same constraints re-explained. A human developer who joins your team spends a week ramping up, then carries that understanding for years. An AI agent ramps up fresh every single request.

This is the structural issue that sends developers scrambling for workarounds.

## The Obsidian approach (and why it's everywhere)

The Obsidian-as-AI-memory pattern has exploded across dev communities in 2025-2026. The core idea is simple: use a local markdown vault as the single source of truth that bridges sessions.

A typical setup looks like this:

```
my-project/
├── CLAUDE.md            # Loaded automatically each session
├── context/
│   ├── decisions.md     # Architecture decisions log
│   ├── rejected.md      # Approaches tried and abandoned
│   └── conventions.md   # Naming, patterns, style rules
├── daily-notes/         # Session summaries
└── src/
    └── ...              # Actual codebase
```

The workflow: after each AI session, either manually or by prompting the agent, you update the relevant context files. Before the next session, the agent reads CLAUDE.md and whatever context files are referenced. The idea is that the vault accumulates intelligence over time — each session adding to a growing body of project knowledge.

It's genuinely clever. And it highlights three things Obsidian gets right that most AI memory approaches don't:

1. **Local ownership.** No vendor lock-in. No cloud dependency. Files on your disk, in a format you control.
2. **Human-readable state.** Unlike opaque embedding databases, you can open any file and see exactly what the AI "remembers." You can edit, delete, or reorganize it.
3. **Structure as retrieval.** Folder hierarchies and backlinks create navigable knowledge graphs without needing vector search or semantic embeddings.

But once you move past solo side-projects, the cracks show fast.

## Where manual memory breaks down

The Obsidian workflow has a fundamental bottleneck: **you are the memory manager.**

You decide what to save. You decide how to organize it. You write the summaries. You maintain the folder structure. You update the context files before each session. You notice when information is stale and clean it up.

That's a full-time curation job layered on top of actual development work. And it breaks in predictable ways:

**Staleness.** Context files drift from reality. You refactored `PaymentService` last week but forgot to update `conventions.md`. The agent reads outdated guidance and generates code against a structure that no longer exists.

**Incompleteness.** You capture the decisions you remember to capture. The subtle constraint you discussed halfway through a debugging session — "don't call the Stripe API directly, always go through the gateway" — gets lost because you didn't think to log it.

**Single-player only.** Your Obsidian vault is your vault. Your teammate has their own CLAUDE.md with their own conventions, potentially contradicting yours. There is no shared ground truth. Three developers, three different agents, three incompatible versions of "how this codebase works."

**Doesn't scale with complexity.** For a personal project with a few hundred files, manual curation works fine. For a codebase with 200+ modules, dozens of service boundaries, and years of accumulated architecture decisions, no human can maintain a complete context document by hand.

One developer in the Reddit thread captured it perfectly: they said the process felt like maintaining a second codebase — except this one had no tests, no linting, and no way to tell when it was wrong.

## CLAUDE.md: the same problem, officially endorsed

Claude Code reads a file called `CLAUDE.md` at the root of any project directory and loads it automatically every session. It's the officially supported version of the Obsidian pattern — and it inherits all the same problems.

In practice, most CLAUDE.md files follow a predictable lifecycle:

1. **Day 1:** Developer writes a thoughtful context file. Project structure, key decisions, conventions.
2. **Week 2:** File has grown to 200 lines. Some sections are outdated. Developer adds new context at the bottom without cleaning up the top.
3. **Month 2:** File is 500+ lines. Half the information contradicts the current codebase. The agent reads all of it and has no way to distinguish current truth from historical artifact.
4. **Month 3:** Developer starts a new CLAUDE.md from scratch. The cycle repeats.

The problem isn't CLAUDE.md itself. It's that manually curated, static context can't keep pace with a living codebase. Stale context isn't just useless — research has shown it can actually *decrease* agent performance while raising costs. It's a snapshot pretending to be a live feed.

## What persistent context infrastructure actually looks like

The developers building Obsidian workarounds have correctly identified what's missing. They just can't build it with markdown files and willpower alone. What they're reaching for has a name: **persistent context infrastructure** — a live, structural memory layer over the codebase that no one has to maintain by hand.

The context layer has four non-negotiable properties:

**If it's not captured automatically, it doesn't exist.** If a developer has to manually log every decision, most decisions won't get logged. Memory needs to be a side effect of working — not a separate task you do after the real work is done.

**Text recall isn't structural awareness.** Knowing that "PaymentService depends on OrderRepository" isn't a snippet to paste — it's a graph relationship to traverse. Flat files can't represent dependency trees, call chains, or module boundaries in a way agents can query. The memory layer needs to understand code *as code*, not as prose about code.

**Memory that can go stale is worse than no memory.** Stale context doesn't just fail to help — it actively misleads. When `PaymentService` gets refactored, the memory layer needs to know automatically, not because a human noticed and updated a file. Outdated guidance that the agent trusts is more dangerous than a blank slate.

**One codebase, one truth — regardless of the agent or the developer.** The context layer can't live in one person's vault. When your teammate makes an architecture decision using Cursor on Tuesday, and you pick up the same module Wednesday in Claude Code, both agents need to be working from the same ground truth. At team scale, this isn't a convenience issue — it's a coordination failure. Three developers maintaining three incompatible maps of the same territory will produce three incompatible versions of the same system.

## Obsidian vaults are the shell scripts of AI development

There's a recurring pattern in software tooling. A new capability arrives. Early adopters build ad-hoc solutions with whatever's available. Those solutions are creative, often brilliant — and they work right up until the complexity of the actual problem outgrows them.

Developers deployed with FTP and shell scripts before CI/CD pipelines existed. The scripts worked. They were inventive. And the breakthrough wasn't a better shell script — it was a purpose-built layer that automated what humans had been doing manually and made it reliable at scale.

Obsidian vaults and CLAUDE.md files are the shell scripts of AI-native development. They're the right instinct expressed through the wrong medium. The developers writing them have identified exactly what the toolchain needs — persistent, structured, queryable context — and are building it by hand because the infrastructure doesn't exist yet.

## What this means for how you work today

If you're currently managing context for your AI agents through markdown files and manual curation, you're not doing anything wrong. You've identified a real problem and built a real solution with the tools available.

But pay attention to where the friction is. When you find yourself re-explaining the same constraint for the third time. When your teammate's agent generates code that contradicts an architecture decision you made last week. When your context file is 400 lines long and you're not sure which half is still accurate.

Those friction points are the signal. They're telling you that the problem has outgrown the workaround — and that the context layer isn't a nice-to-have. It's the missing infrastructure between AI agents and production-grade software development.

Not documentation. Not embeddings. Not a bigger context window. A live, structural memory layer that understands your codebase the way a senior engineer does — and retains that understanding across sessions, across agents, across your entire team.

The question isn't whether this layer will exist. It's how much longer teams will keep building it by hand.

The agents are smart enough. They just can't remember. Not yet.

**Related reading:**
- [Claude Code's Memory System Is the Most Ambitious in Production. Here's Where It Hits the Ceiling.](claude-codes-memory-system-is-the-most-ambitious-in-production-here-is-why-it-fails)
- [We Built Bitloops Because AI Agents Keep Forgetting](we-built-bitloops-because-ai-agents-keep-forgetting)
- [The Future of Software Development: Context-Aware AI Engineering](future-of-software-development-context-aware-ai-engineering)

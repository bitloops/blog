---
title: "Your CLAUDE.md Is Probably Making Claude Dumber"
description: "New research shows AI-generated CLAUDE.md files reduce success rates by 3% and increase cost by 20%. Here's what actually works — and what doesn't."
author: Sergio
date: 04-April-2026
image: https://storage.googleapis.com/bitloops-github-assets/Blog%20Images/your_claude.md_is_probably_making_your_claude_dumb/your-claude-md-is-probably-making-cla_e549a375-15ed-4197-ad21-a76587a9ac5a_2.png
tags:
  [
    "AI Coding",
    "Context Engineering",
    "Claude Code",
    "Developer Productivity",
    "Bitloops"
  ]
---

The instinct is obvious: [Claude Code](https://bitloops.com/claude-code) reads a CLAUDE.md file at the start of every session, so the more you put in it, the better Claude should perform. Architecture docs, naming conventions, style guides, past decisions, folder structure, API patterns — dump it all in.

Two research papers published this year tested that instinct. Both found the same thing: it's wrong.

## The Research

An [ETH Zurich study](https://arxiv.org/abs/2506.08211) tested `agent.md` files across hundreds of real GitHub issues. The results:

- **AI-generated CLAUDE.md files** reduced success rates by 3% and increased cost by 20%
- **Developer-written files** improved performance by only 4% — and inconsistently. Claude Code paired with Sonnet 4.5 actually showed a 2% *drop* with developer-written context

The main finding: unnecessary context makes tasks harder. More isn't better. More is actively worse.

A second study, [SkillsBench](https://arxiv.org/abs/2506.06775), ran 7,000+ test cases with 105 researchers. Same pattern:

- **Carefully curated skills** (focused, 2–3 modules) improved performance by 16.2 percentage points
- **Self-generated skills** — the AI writing its own context — produced zero benefit

The difference isn't whether you provide context. It's whether that context is focused, relevant, and minimal enough to actually land. This is the core challenge of [context engineering](https://bitloops.com/guides/context-engineering) — and it applies far beyond a single file.

## Why Bloated Context Gets Ignored

Here's something most Claude Code users don't know. When Claude Code sends your CLAUDE.md to the API, it wraps it with a disclaimer:

> *"This context may or may not be relevant to your task. You should not respond to this context unless it is highly relevant."*

This was discovered by [Human Layer](https://humanlayer.dev), who put a proxy between Claude Code and the Anthropic API to see the actual system prompt. Your carefully written 300-line CLAUDE.md arrives at the model pre-labelled as potentially irrelevant. Generic or bloated files aren't just wasteful — they're explicitly told to be deprioritized.

The context you spent an hour writing? Claude may be ignoring most of it by design.

## The Compliance Decay Curve

Even context that *does* land doesn't stick for long. Research on instruction compliance across conversation length shows a predictable decay:

- **Messages 1–2:** ~95% compliance with instructions
- **Messages 3–5:** 60–80% compliance
- **Messages 6–10:** 20–60% compliance
- **Beyond 10 messages:** degrades rapidly

This explains a pattern every [Claude Code](https://bitloops.com/claude-code) user has experienced: the agent follows your rules for the first few exchanges, then starts drifting. By mid-session it's making "stupid mistakes" — not because the model degraded, but because your instructions are losing weight with every additional message in the context window. (We wrote about [why this happens at the model level](/blog/why-coding-agents-fail-not-the-model-its-the-memory) previously.)

A 500-line CLAUDE.md doesn't just start at a disadvantage. It decays faster, because the model has more low-relevance content competing with your actual instructions. (For a look at how these files balloon in practice, see our earlier piece on [why your CLAUDE.md is 500 lines long](/blog/why-your-claude-md-is-500-lines-long).)

## What Actually Works

[Boris Cherny](https://x.com/AskBorisCherny), creator of Claude Code, shared his own setup. It's the opposite of what most developers do:

**One CLAUDE.md, checked into git.** Around 60–80 lines. The whole team contributes. It evolves through failure — when Claude does something wrong, someone adds a rule.

**Verification commands are the most important lines.** Type check, test, lint — commands Claude can run to check its own work. Boris says these 2–3x the quality of Claude's output. The reason is simple: they give Claude a feedback loop. Without them, it's operating open-loop — generating code with no way to validate whether it works.

**Personal CLAUDE.md is two lines.** It just points to the team version. No personal tweaks, no 200-line addendum.

**Auto-updates via GitHub Actions.** When a PR merges, the CLAUDE.md gets refreshed. It stays current without anyone manually maintaining it.

The pattern is clear: the CLAUDE.md that works is short, specific, team-maintained, and focused on giving Claude the ability to verify its own output.

## The Progressive Disclosure Model

The deeper insight from this research is that not all context should be treated equally. There are three tiers:

**Always loaded (every message):** CLAUDE.md, system prompt, memory files. This is the most expensive tier — it's injected into every API call. It should be minimal: verification commands, critical constraints, project identity. Nothing more.

**On-demand (when relevant):** Rule files, skills, subdirectory-level CLAUDE.md files. Loaded only when Claude is working in a specific area. This is where architectural patterns, module-specific conventions, and domain rules belong.

**Reference only (zero cost until accessed):** Documentation, READMEs, source code. Claude reads these when it needs them. They cost nothing until that moment.

The insight: **CLAUDE.md should be an index, not a document.** Point to where information lives. Don't cram it all into the always-loaded tier.

Most developers do the opposite. They treat CLAUDE.md as a single flat file and stuff everything into Tier 1. Every session pays the cost of loading context that's relevant to maybe 10% of the tasks Claude will actually perform.

## The Real Fix

The research points to an uncomfortable conclusion: hand-maintaining a context file is a losing strategy at scale. The ETH Zurich data shows that even developer-written files barely move the needle. The compliance decay curve means that whatever benefit you get evaporates mid-session. And the progressive disclosure model requires a level of context management that no one wants to do manually.

What actually moves performance is **focused, relevant context delivered at the right moment** — not a monolithic file loaded every time.

This is the problem [Bitloops](https://bitloops.com) is built around. Instead of asking developers to hand-curate what the agent should know, Bitloops captures context from what actually happens — commits, architectural decisions, session reasoning, team patterns — and surfaces the relevant slice when the agent needs it. The always-loaded tier stays minimal. The on-demand tier is [managed automatically](https://bitloops.com/how-it-works). Context that would otherwise bloat your CLAUDE.md gets structured, stored, and delivered only when it's relevant.

Not a replacement for CLAUDE.md. [A replacement for the 450 lines that shouldn't be in it.](https://bitloops.com/guides/claude-md-vs-bitloops)

## What to Do Right Now

If you're maintaining a CLAUDE.md today, here's the practical takeaway from the research:

- **Cut it to under 80 lines.** If it's longer, most of it is being deprioritized or ignored
- **Lead with verification commands.** Type check, test, lint — whatever gives Claude a feedback loop. This is the highest-ROI content you can put in the file
- **Move domain-specific rules to subdirectory CLAUDE.md files.** They only load when Claude is working in that directory
- **Remove anything Claude can derive from reading the code.** File structure, import patterns, naming conventions that are already consistent — Claude can see these. You don't need to spell them out
- **Treat it as an index.** Point to where detailed information lives, don't duplicate it

Your CLAUDE.md should be a signpost, not an encyclopedia. The research is clear: the less you put in, the more of it actually lands.

---

**Further reading:**
- [Why Coding Agents Fail: Not the Model, It's the Memory](/blog/why-coding-agents-fail-not-the-model-its-the-memory)
- [Why Your CLAUDE.md Is 500 Lines Long](/blog/why-your-claude-md-is-500-lines-long)
- [CLAUDE.md vs Bitloops — What Goes Where](https://bitloops.com/guides/claude-md-vs-bitloops)
- [Context Engineering Guide](https://bitloops.com/guides/context-engineering)
- [Bitloops — Open Source](https://bitloops.com/open-source)

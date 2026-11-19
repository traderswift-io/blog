---
title: Since Lockbox – A Week of Building Signer and TraderSwift
description: What we built between 11 and 18 November 2026, what broke, and what we changed.
kind: update
order: 2
---

On 11 November we halted our first chain, Lockbox, and archived it.

Seven days later, we had:

- a new signing chain with live orders behind it;
- a chain at the centre of TraderSwift, called the hub;
- a wallet design;
- our own sign-in;
- a storage chain that passed its first launch test;
- a build line where most of the code is written by Codex.

This update walks through that week: what we built, what broke, and what we changed because of it.

Each part carries one of three labels: **Live** (running for real), **Built, not live** (the code exists and passed its checks), or **Planned** (a design or an aim).

## What did the week look like?

![Milestones, 11 to 18 November](../assets/since-lockbox/milestones.svg)

![Commits per day, all repositories](../assets/since-lockbox/commits_daily.svg)

Across all our repositories there are 729 commit records between 11 and 18 November. The busiest day was 15 November, with 138.

These are commit records, not features: one fix can take several commits.

The last day is also partial.

We share the counts so you can judge the pace of the work for yourself, not take our word for it.

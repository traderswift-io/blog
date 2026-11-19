---
title: How did Codex become our main builder?
description: How a job moves from spec to merge, and what the review panel found.
order: 4
---

On 14 November we made a simple rule: send as much well-specified coding as possible to Codex.

Each project's owner then reviews and merges what Codex writes.

By the end of the week, Codex jobs covered almost every part of the system.

![Codex jobs per day](../assets/since-lockbox/jobs_daily.svg)

![Codex jobs by area](../assets/since-lockbox/jobs_by_area.svg)

There are 321 job entries in the week, counting reviews and revisions as their own jobs. Signals and the desk had the most, at 64, then execution and research at 52, and Signer at 35.

Why this matters to you: it shows where the work went, and that review is counted as work, not skipped.

## How does a job move?

1. **Spec.** An agent writes it: what to build, where, and the check that proves it works.
2. **Run.** A runner starts Codex. It runs the checks outside Codex's sandbox, retries on failure, and writes a summary.
3. **Review.** The owner reads the change. A second, independent pass reviews anything public or anything on the money path, meaning code that can place an order or move funds.

On 15 November a second Codex came online, so coding and reviewing could run side by side. The dispatcher became event-driven: a finished job starts the next one, with no one waiting.

## What did the review panel find?

On 17 November we ran our first full internal review of the cryptography. Its findings feed the next releases.

It also showed that the public Signer code and the code running live had already drifted apart.

Two of its findings were already fixed in the running branch.

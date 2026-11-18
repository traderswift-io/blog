---
title: How did Codex become our main builder?
description: How a job moves from spec to merge, and what the review panel found.
order: 4
---

On 14 November we made a simple rule: send as much well-specified coding as possible to Codex, and let each project's owner review and merge.

By the end of the week, Codex jobs covered almost every part of the system.

![Codex jobs per day](../assets/since-lockbox/jobs_daily.svg)

![Codex jobs by area](../assets/since-lockbox/jobs_by_area.svg)

There are 321 job folders in the week, counting reviews and revisions as their own jobs.

Signals and the desk had the most, at 64, then execution and research at 52, and Signer at 35.

How a job moves:
1. **Spec.** An agent writes it: the words, the repository, the files, and the check that proves it works.
2. **Run.** A runner starts Codex. It runs the checks outside Codex's sandbox, retries on failure, and writes a summary.
3. **Review.** The owner reads the change, and a second independent pass reviews anything public or anything on the money path.

On 15 November a second Codex came online, so coding and reviewing could run side by side.

The dispatcher became event-driven: a finished job starts the next one, with no one waiting.

On 17 November we ran our first full crypto review panel across 10 repositories. Its findings feed the next releases.

It also showed us that the public Signer code and the code running live had already drifted apart, and two of its findings were already fixed in the running branch.

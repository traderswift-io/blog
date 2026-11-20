---
title: What went wrong, and what did we change?
description: The faults we found this week, and the rules we changed.
order: 13
---

A lot, and that is the useful part of the week.

## Why were agents waiting on each other?

An audit of our fault log found 59 entries:

- work with no owner;
- replies that never reached the asker;
- wake-ups that failed;
- health checks that measured activity instead of progress.

We fixed the wake path and the readers. We also changed the rules: agents now resume work that is already authorized instead of waiting for a fresh go.

## Why did some checks pass when they shouldn't have?

An audit of 29 jobs found two checks that reported a pass while hiding a failure. The runner now records the raw exit status of one check command.

## How could an answer attach to the wrong question?

An approval could attach to the wrong question, or survive a retry it should not have. Answers are now bound to exactly what was offered, and answered questions are frozen.

## What leaked into a job's checkout?

Broad staging let excluded files reach a job's working copy. Jobs are now staged file by file, from the permitted copy only.

## Why did we say a thing landed before checking?

Twice, a result was reported before anyone read what the code actually did. The rule now: read the implemented requirement before saying it landed.

## What did review find in Signer's next release?

Review of the next Signer changes found more defects. We keep a clear line between the release that is running and the next one under review.

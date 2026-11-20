---
title: What went wrong?
description: Decision records that waited in an outbox.
order: 6
---

Every signer writes a record of each decision, signed or refused, to the chain.

After the first step, none from the new machines arrived.

The cause was simple: the new signers had no accounts on the chain, so they had nothing to send from. They had not lost anything.

Each kept its records in a local outbox and waited. Once the accounts were created, the backlog went on chain together, at height 353,836.

That is the lesson for the next rotation, target Sat 21 Nov 2026: its checklist will check for a decision record on chain from each new signer before the old set is removed.

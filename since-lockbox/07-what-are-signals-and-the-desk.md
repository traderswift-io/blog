---
title: What are Signals and the desk?
description: From a published idea to an executed trade, through Signer.
order: 7
---

Signals is how a published trade idea becomes an executed trade. The publisher dictates or types a signal, it is shaped into a clear trade, and it goes into a private store. If an idea is missing its invalidation, its confidence or its expiry, Signals asks for it instead of guessing.

Signals stays private. Early in the week, one route made it public by mistake; we reverted it and disabled the publisher, and the rule now is that every read is access-controlled.

The desk executes signals through Signer. We built it from two open-source trading desks, each forked into the same three branches:
- **Upstream.** Unchanged.
- **Signer.** The default branch, where the desk signs through Signer instead of holding a venue key.
- **TraderSwift.** The desk also checks the publisher and the signal on the hub before it acts.

Signals Desk went public on 15 November and Pathiel on 16 November. On 17 November the desk ran Signer's rotation gate on a small live account with real money: one refusal, one entry and one close.

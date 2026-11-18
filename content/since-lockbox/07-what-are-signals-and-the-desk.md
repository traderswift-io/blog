---
title: What are Signals and the desk?
description: From a published idea to an executed trade, through Signer.
order: 7
---

Signals is how a published trade idea becomes an executed trade.

The publisher dictates or types a signal, it is shaped into a clear trade, and it goes into a private store. If an idea is missing its invalidation, its confidence or its expiry, Signals asks for it instead of guessing.

Signals stays private. Early in the week, one route made it public by mistake; we reverted it and disabled the publisher, and the rule now is that every read is access-controlled.

The desk executes signals through Signer. The desk is not our own software. It runs on two open-source trading desks that we forked, each into the same three branches:
- **Upstream.** Unchanged.
- **Signer.** The default branch, where the desk signs through Signer instead of holding a venue key.
- **TraderSwift.** The desk also checks the publisher and the signal on the hub before it acts.

Signals Desk is our fork of [galleonlabs/hypergrok-trading-desk](https://github.com/galleonlabs/hypergrok-trading-desk), the HyperGrok Trading Desk. Pathiel is our fork of [Julian-dev28/pathiel](https://github.com/Julian-dev28/pathiel).

Both are under the MIT licence. What we added are the Signer and TraderSwift branches. We made our fork of Signals Desk public on 15 November, and our fork of Pathiel on 16 November.

On 17 November the desk ran Signer's rotation gate on a small live account with real money: one refusal, one entry and one close.

---
title: What are Signals and the desk?
description: From a published idea to an executed trade, through Signer.
order: 7
---

Signals is how a published trade idea becomes an executed trade.

The publisher dictates or types a signal, it is shaped into a clear trade, and it goes into a private store. If an idea is missing its invalidation, its confidence or its expiry, Signals asks for it instead of guessing.

## Who can read a signal?

Signals stay private: only wallets the publisher has authorised can read a signal's content.

Each signal also gets a fingerprint and a timestamp, so a provider can build a track record. The fingerprint does not reveal who a subscriber is.

Fingerprinting is **Built, not live**, and kept off the chain for now. No real signal has been published yet.

Early in the week, one route was briefly public when it should not have been. It never held a signal.

We closed it and disabled the publisher. Every read now needs an authorised token.

## What is the desk?

The desk executes signals through Signer.

The desk is not our own software. It runs on two open-source trading desks that we forked, each into the same three branches:

- **Upstream.** Unchanged.
- **Signer.** The default branch, where the desk signs through Signer instead of holding a venue key.
- **TraderSwift.** **Planned:** the desk will also check the publisher and the signal on the hub before it acts.

Signals Desk is our fork of [galleonlabs/hypergrok-trading-desk](https://github.com/galleonlabs/hypergrok-trading-desk), the HyperGrok Trading Desk. Pathiel is our fork of [Julian-dev28/pathiel](https://github.com/Julian-dev28/pathiel).

Both are under the MIT licence. What we added are the Signer and TraderSwift branches.

We made our fork of Signals Desk public on Sun 15 Nov 2026 (**Live**), and our fork of Pathiel on Mon 16 Nov 2026 (**Built, not live**).

On Tue 17 Nov 2026 Signals Desk ran Signer's rotation gate on a small live account with real money: one refusal, one entry and one close.

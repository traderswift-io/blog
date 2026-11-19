---
title: What is signer-1, and what did it do this week?
description: The live launch with real money, and the move to new machines.
order: 2
---

`signer-1` is the chain that runs Signer, and it is **Live**.

Signer keeps a trading key as shares on separate machines, called signers, and signs an order only if it fits the owner's written limits. [How does Signer hold a key?](../what-is-traderswift/08-how-does-signer-hold-a-key.html) explains it in full.

![How a Signer request flows](../assets/since-lockbox/signer-request-flow.svg)

![The public Signer repository, on a phone](../assets/since-lockbox/signer-repo-390-light.png "Signer is open source: github.com/traderswift-io/signer.")

`signer-1` started on 12 November.

![signer-1 heights recorded this week](../assets/since-lockbox/signer_heights.svg)

## What happened at the live launch on 14 November?

The chain admin, the wallet that can change who signs, moved to the owner's own wallet at height 160,839.

Then we traded, on a small live account with real money, BTC only:

- **Fills.** An immediate-or-cancel buy filled, and a close-only sell closed it.
- **Over-cap refusal.** A buy at twice the order cap was refused before it reached the exchange.
- **Revoke.** We cancelled the owner's limits on the chain at height 161,327. The next order was refused at 161,330.
- **Transfers and withdrawals.** Every one of these requests was refused, and the refusal logged.

That account is our own test account, and it is public by choice.

For your own account, the trading account address and the contents of your orders never appear on `signer-1` in readable form. [What can other people see on the chain?](../what-is-traderswift/11-what-can-other-people-see-on-the-chain.html) explains what the chain shows instead.

The launch key had existed whole before we split it. It was a key the owner had already approved on the exchange to trade for the account.

Keys made jointly by the signers, which never exist whole, were proven on the same set with a throwaway key.

## What happened in the rotation on 17 November?

A rotation moves Signer to a new set of machines with a new key.

On 17 November we did our first one, and signing moved from the old key to the new one with no stop.

The new set passed the same live gate: a refusal, an entry and a close.

When the old set was removed, four validators were left, and any three of them can sign. [Update 03](../trading-key-rotation/index.html) tells the rotation step by step.

## What did the rotation find?

The new signers had no chain accounts: the identities a machine needs before it can write to the chain.

So their decision records piled up in a local outbox, a queue on each machine. They were safe, but off the chain.

Once the accounts existed, 22 records went on chain at height 353,836.

The checklist for the next rotation, on Fri 20 Nov 2026, checks for a decision record from each new signer before the old set is removed.

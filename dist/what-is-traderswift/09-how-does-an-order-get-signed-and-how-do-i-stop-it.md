---
title: How does an order get signed, and how do I stop it?
description: The limits you write, how each order is checked and signed, and the one message that stops your agent.
order: 9
part: Security, which is more than the key
---

You decide what your agent may trade, and Signer holds it to that.

This chapter goes one step at a time: the limits, the signing, and the stop.

## Who writes the limits?

You do. You write down what the agent may trade:

- **Markets** – which ones it may trade.
- **Order size** – how big one order may be.
- **Daily size** – how much it may trade in a day.
- **Expiry** – the date the limits stop working.

You sign these limits with your own wallet, so nobody else can change them. This set of limits is called a policy.

## Where is the policy kept?

It is kept on `signer-1`, the blockchain Signer runs on. Nobody can change a past entry on it alone.

That matters because the signers read your policy from there. Nobody can hand them a different one.

## How does an order get signed?

The agent sends an order request. It signs the request with its own small key, which cannot sign anything at the exchange, so it is worth little to a thief.

Each signer reads the request and checks it against your policy on its own.

If the order fits, the signer builds the exchange message itself and signs its part. It never signs a message someone else hands it.

When three signers have signed their parts, the signature is complete. It goes to the exchange, and the order is placed.

If the order does not fit, it is refused, and the refusal is recorded. [Chapter 10](10-how-would-i-know-if-someone-tried-to-break-in.html) explains why that record helps you.

## What can the agent never do?

The agent can send trading requests only: orders, cancels, and a timed cancel-all that closes every order after a set time.

Signer never signs a transfer or a withdrawal. Moving funds stays with your own wallet.

## How do I stop the agent?

You sign one message that revokes the policy. The chain adds new entries in batches, called blocks.

A revoke takes effect in the block it lands in. From then on the policy allows nothing new: no new orders, and no size increases.

For 600 seconds after the revoke, the agent can still cancel orders and arm a timed cancel-all, so it can tidy up; after that, everything is refused.

At launch, the next order after the revoke was refused, and the refusal was on chain three blocks later. **Live** since 14 Nov 2026.

## What limits are coming next?

A second set of limits is in review, with a target of Fri 20 Nov 2026. The chain part is **Built, not live**, and the signer part is still being built.

- **A price band** – orders too far from the market price are refused.
- **An order-rate cap** – a limit on how many orders the agent may send in a given time.
- **Post-only** – orders may only rest on the book and wait, never take an existing price.
- **Value caps** – a limit on the total value of an order, not just its size.

Each one narrows what a taken-over agent could do.

## Where do I learn more?

The Signer how-tos show each step in detail:

- [How do I write a trading policy?](../signer-guides/04-how-do-i-write-a-trading-policy.html)
- [How do I stop an agent fast?](../signer-guides/05-how-do-i-stop-an-agent-fast.html)

To review the cryptography itself, start with [how to understand and review cryptographic systems](../cryptography/index.html).

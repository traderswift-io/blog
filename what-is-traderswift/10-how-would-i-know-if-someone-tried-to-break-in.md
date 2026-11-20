---
title: How would I know if someone tried to break in?
description: Every order request is recorded, signed or refused. A refused order tells you someone tried something outside your limits.
order: 10
part: Security, which is more than the key
---

Normally, whoever had your key would either drain you, or you'd never know they'd been in.

With Signer, you would see them try.

## What is recorded?

Every order request your agent sends is recorded on the Signer chain, `signer-1`, whether it was signed or refused.

Each record shows:

- **When** – the block the request was decided in.
- **Which signer** – the one that made the decision.
- **The decision** – signed or refused.
- **The reason** – why, if it was refused.
- **A fingerprint of the order** – not the order itself.

A fingerprint here is a short code worked out from the order. The same order always gives the same code, but the code does not show what the order was.

The signers check the fingerprint, and only they can open the details.

## Why is a refused order useful?

A refused order is your alarm.

It means someone with your agent's access tried something outside your limits. Perhaps a market you never allowed, or an order far bigger than your cap.

The attempt failed, and you can see that it happened.

With a key held the usual way, there is no refusal to see. The order simply goes through, and the exchange shows it as one of yours.

## What can I do when I see one?

You can revoke the policy, the set of limits you gave the agent, by signing one message.

A revoke takes effect in the block it lands in. From then on the policy allows nothing new: no new orders, and no size increases.

For 600 seconds after the revoke, the agent can still cancel orders and arm a timed cancel-all, so it can tidy up. After that, everything is refused.

[Chapter 09](09-how-does-an-order-get-signed-and-how-do-i-stop-it.html) shows where the revoke fits in signing an order.

## How do I read the record?

You run a node, a program that keeps its own copy of the Signer chain, and look up the decisions.

The how-to [How do I read Signer's record?](../signer-guides/06-how-do-i-read-signers-record.html) walks you through it.

## Is this running?

**Live.** Every decision since launch on Sat 14 Nov 2026 is on the Signer chain.

[The next chapter](11-what-can-other-people-see-on-the-chain.html) explains what other people can see on that chain, and what they cannot.

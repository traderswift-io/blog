---
title: How does the network fit together?
description: One shared chain at the centre, a separate chain for each job, and the people who run them.
order: 24
part: The network, and where it stands
---

TraderSwift is not one blockchain.

It is several, each with one job, joined at a shared centre.

This chapter explains the words used for each piece, once, so the rest of the update can use them.

## What is a blockchain here?

A blockchain is a shared record kept by several machines.

Those machines are called validators. A change goes in only when enough of them agree, so no single one can rewrite the past.

## What is the hub?

The hub is the chain at the centre. Its name is `traderswift-1`.

It holds:

- the identities used across TraderSwift;
- the list of the hub's own validators;
- each subnet's charter;
- each subnet's anchors.

The hub holds no token and no balances, and it charges no fees. So there is nothing to buy before you can use it.

**Live** since Sat 14 Nov 2026.

## What is a subnet?

A subnet is a chain with one job, run by its own validators. It has its own vote, and its vote binds.

Each subnet runs on its own. If the hub stops, the subnet keeps working.

The table below lists each subnet and its current status.

| Subnet | Its job | Status |
| :--- | :--- | :--- |
| `signer-1` | Holds trading limits, and signs orders inside them | **Live** on Hyperliquid since Sat 14 Nov 2026 |
| `storage-1` | Checks that storage providers still hold your scrambled files | **Built, not live** |
| `ledger-1` | Where your tasks are kept, and who may read them | **Live** since Thu 19 Nov 2026; nothing writes to it yet |
| `vault-1` | Where your notes and files are kept, and who may read them | **Live** since Thu 19 Nov 2026; nothing writes to it yet |
| Market data | Daily fingerprints of market candles | **Built, not live** |
| Signals | A private record of signal fingerprints | **Planned** |

## What is a charter?

A charter is a subnet's entry on the hub. It is how the hub knows a subnet exists and is part of TraderSwift.

Only the hub's admin can add one.

## What is an anchor?

An anchor is a short fingerprint of a subnet's record, posted to the hub.

Once it is there, anyone can check that subnet's past against it. [Chapter 14](14-how-can-i-check-market-data.html) explains fingerprints.

## Who controls the hub?

The hub has an admin: the account that adds charters.

On 18 Nov 2026, the admin was handed to a multisig. A multisig is an account that acts only when several of its keys agree.

So no single key can add a subnet, or change one.

## When do the first charters go on?

There is no date yet. They wait on one security review, and then on final approval.

## Who are network participants?

Network participants are people who run part of the network, such as a validator or a data node, and people who pay to use what others run.

Ways to take part:

- **Run a Signer validator.** [How do I run a Signer validator?](../signer-guides/07-how-do-i-run-a-signer-validator.html) shows how.
- **Run a charts data node,** and compare its fingerprints with ours. [Chapter 14](14-how-can-i-check-market-data.html) shows how.
- **Pay to use what others run,** such as data or front ends. [Chapter 20](20-what-is-the-marketplace-and-how-do-builders-get-paid.html) explains payment.

A launcher that starts a node from one link is **Planned**. [How do I launch a node with one link?](../signer-guides/08-how-do-i-launch-a-node-with-one-link.html) describes it.

If you want to build a whole new subnet, read [chapter 25](25-can-i-build-a-subnet-of-my-own.html).

---
title: What is Signer, and who is it for?
description: Signer lets an agent trade from a key that no one holds whole, under a policy the owner writes on a chain.
order: 1
---

After this page you will know what Signer does, whether it fits your trading, and why you might wait before using it.

## What is Signer?

Signer is threshold signing for agents that trade. A venue key is held in shares by a group of signer machines.

A quorum of them must agree before an order is signed.

Each signer checks the order against a policy before it signs.

The policy is written by the owner on a small chain called `signer-1`.

Every decision, signed or refused, is recorded on that chain.

Signer is open source under the Apache License 2.0 at github.com/traderswift-io/signer. It is one part of TraderSwift, which we describe as a blockchain infra layer for agentic and hybrid trading.

## How does a key that nobody holds work?

The key is split into shares, and each share sits on a different signer machine.

Since 17 November 2026 there are four signers, and any three can sign together. Two cannot.

At launch the setup was two of three.

When the signers generate a key together, it never exists whole on any machine. That is not true of our live key.

It existed whole once, because it was an exchange agent the owner had already approved. We then split it into shares.

## Why would I use Signer?

A trading bot usually holds a full key. If the bot leaks it, whoever has it can do everything the key allows.

Signer changes what the bot holds.

- **No key in the bot.** The agent sends an order request and never holds the venue key.
- **Limits at the key.** The policy bounds which markets, how big and for how long, before anything reaches the venue.
- **A hard stop.** The owner can revoke the policy on chain, and later orders are refused.
- **A public record.** Every decision is on the chain, so you can read what was signed and what was refused.

Each signer also builds the venue message itself from the order request. It never signs a hash someone hands it.

Transfers and withdrawals are always refused, whatever the policy says.

## Who is Signer for?

Signer is for someone who runs an agent or a bot with real money behind it. It suits an owner who wants to say, in writing and on chain, what that agent may do.

It is also for people who build trading software and want a signing layer that is open to read.

You can run it as your own chain with your own signers, or follow the guide to run a validator.

## Why shouldn't I use Signer?

Be honest with yourself on this one. Signer is in development, and these limits are real today.

- **In development.** The chain started on 12 November 2026 and the first live orders were on 14 November. That is a short record.
- **No key for your own account yet.** Outsiders cannot get a key for their own account until the next rotation. Another rotation comes before signers we do not run can join.
- **One venue live.** Hyperliquid is the only venue live today. The code also has Aster and Base, but neither is live.
- **Fewer rules than you may want.** The policy bounds sizes per market. It has no price band yet. Policy v2 plans one, and we explain it in the policy article.
- **Interactive signing.** Signing is interactive today, so each order needs several signers online.

If you need a key for your own account this week, Signer is not ready for you. If you want to read the code and the record, it is.

## What has Signer done so far?

The launch was on a small live account with real money, on Hyperliquid mainnet.

The record is public in the `signer-1-launch` release of the repository.

- **Fills.** A buy filled and a close-only sell closed it.
- **Refusal.** A buy at twice the order cap was refused before it reached the venue.
- **Revoke.** We revoked the policy at height 161,327. The next order was refused at height 161,330.
- **Transfers.** Every transfer and withdrawal request was refused, and the refusal was logged.

On 17 November we moved Signer to a new set of machines and a new key.

The new set passed the same live gate: a refusal, an entry and a close.

## Where do I go from here?

Read the next articles in this order. They are short.

1. **How does an order get signed?** The path from your agent's request to the venue.
2. **How do I write a trading policy?** The fields you set, and what stays with you.
3. **How do I stop an agent fast?** The on-chain revoke.

## Final thoughts

Signer takes the venue key out of the agent's hands and puts a written policy in front of it. It is early, it is open, and we say plainly where it stops.

Start with the article on how an order gets signed. If you run a validator or read the chain, you can check our claims yourself.

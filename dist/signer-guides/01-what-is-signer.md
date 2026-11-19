---
title: What is Signer, and who is it for?
description: Signer lets a trading agent place orders without holding the key to the account, inside limits the owner sets.
order: 1
---

After this page you will know what Signer does, whether it fits your trading, and why you might wait before using it.

## What is Signer?

Signer lets a trading agent place orders without holding the key to the account.

A key is what signs an order at an exchange, which we call a venue. Whoever holds the key can trade the account.

With Signer, the key is cut into pieces, called shares. Each share sits on a different machine, called a signer.

Enough of the signers must agree before an order is signed. This is called threshold signing.

To see the mathematics behind it with small numbers, read [Shamir: which threshold really applies?](../cryptography/08-shamir-which-threshold-really-applies.html) in our cryptography guide.

Each signer first checks the order against limits the owner writes down, called a policy.

The policy is kept on a small public blockchain called `signer-1`. Every decision, signed or refused, is recorded there too.

Signer is open source under the Apache License 2.0 at github.com/traderswift-io/signer.

It is one part of TraderSwift, the infrastructure layer for agentic trading.

## How does a split key work?

The key is split into shares, and each share sits on a different signer machine.

Since 17 November 2026 there are four signers, and any three can sign together. Two cannot.

At launch the setup was two of three, and that first key was split into shares from a key the owner had already approved at the venue.

Since the rotation on 17 November 2026, our live key was made by the signers together. It has never existed whole on any machine, at any point.

## Why would I use Signer?

A trading bot usually holds a full key. If the bot leaks it, whoever has it can do everything the key allows.

Signer changes what the bot holds.

- **No key in the bot.** The agent sends an order request and never holds the venue key.
- **Limits at the key.** The policy bounds which markets, how big and for how long, before anything reaches the venue.
- **A hard stop.** The owner can revoke the policy on the chain, and later orders are refused.
- **A public record.** Every decision is on the chain, so you can see what was signed and what was refused. A refused order tells you someone tried something your policy does not allow.

Each signer also builds the venue message itself from the order request. It never signs a hash, a short fingerprint of a message, that someone hands it.

Transfers and withdrawals are always refused, whatever the policy says.

## Who is Signer for?

Signer is for someone who runs an agent or a bot with real money behind it.

It suits an owner who wants to say, in writing, what that agent may do, and have every machine that signs check it.

It is also for people who build trading software and want a signing layer that is open to read.

You can run it as your own chain with your own signers, or help run ours as a validator.

## Why shouldn't I use Signer?

Be honest with yourself on this one. Signer is in development, and these limits are real today.

- **In development.** The chain started on 12 November 2026 and the first live orders were on 14 November. That is a short record.
- **Your own account is not open yet.** Our target is Saturday 21 November 2026. The [Signer index](index.html) says what it waits on.
- **One venue live.** Hyperliquid is the only venue live today. Aster has a target of Friday 20 November 2026, and Base (Avantis) has no date yet.
- **No price limit yet.** Today the policy bounds sizes per market, not prices. Policy v2 adds a price band, and we explain it in the [policy article](04-how-do-i-write-a-trading-policy.html).
- **Interactive signing.** Each order needs several signers online at the same time.

If you need a key for your own account, our target is Sat 21 Nov 2026. If you want to read the code and the record, it is ready now.

## What has Signer done so far?

The launch was on a small live account with real money, on Hyperliquid mainnet.

The record is public in the `signer-1-launch` release of the repository.

- **Fills.** A buy filled and a close-only sell closed it.
- **Refusal.** A buy at twice the order cap was refused before it reached the venue.
- **Revoke.** We revoked the policy in block 161,327. The next order was refused in block 161,330.
- **Transfers.** Every transfer and withdrawal request was refused, and the refusal was logged.

On 17 November we moved Signer to a new set of machines and a new key.

The new set passed the same live gate: a refusal, an entry and a close.

## Where do I go from here?

Read the next articles in this order. They are short.

1. **[How does an order get signed?](02-how-does-an-order-get-signed.html)** The path from your agent's request to the venue.
2. **[How do I write a trading policy?](04-how-do-i-write-a-trading-policy.html)** The fields you set, and what stays with you.
3. **[How do I stop an agent fast?](05-how-do-i-stop-an-agent-fast.html)** The revoke.

## Final thoughts

Signer takes the venue key out of the agent's hands and puts a written policy in front of it.

It is early, it is open, and we say plainly where it stops. If you run a validator or read the chain, you can check our claims yourself.

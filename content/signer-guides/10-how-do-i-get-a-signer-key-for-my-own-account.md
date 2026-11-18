---
title: How do I get a Signer key for my own account?
description: Outsiders can't get a key yet. What it will take, and the milestones to get there. Planned.
order: 10
---

**Planned.**

This page is half written on purpose. Today, Signer signs only for accounts we run.

The first half explains why. The second half is the milestones.

When outsiders can get a key, this page will be updated with the full steps.

Once it opens, you will be able to have Signer hold a trading key for your own exchange account, under a policy you write and sign yourself.

## Can I get a key today?

No. Signer is live, but only for our own accounts.

Outsiders can't get a key until the next signer rotation.

That is a choice, not a missing feature. The signers running today are sealed: no one can log in to them, including us.

Fixes made after the seal can't be copied onto them. The next set carries those fixes and Policy v2, and that is the set we want holding other people's keys.

You can still run a validator today. See [How do I run a Signer validator?](07-how-do-i-run-a-signer-validator.html).

## What will it look like?

The steps below are the plan. Each one is already how Signer works for our own account.

1. **Your account, your wallet.** You bind your exchange account and the new key with your own wallet. Nobody else can do it for you.
2. **A key no one holds.** The signers make the key together. It never exists whole, on any machine.
3. **You approve it on the exchange.** The key is added to your account as an agent that can trade, not withdraw.
4. **You write the policy.** Which assets, how large an order, how much a day, and what leverage. See [How do I write a trading policy?](04-how-do-i-write-a-trading-policy.html).
5. **You can stop it.** Revoking the policy on chain stops every order from the next block. See [How do I stop an agent fast?](05-how-do-i-stop-an-agent-fast.html).

## What can I prepare now?

Your policy. Most of the work in getting a key is deciding what it may do.

You can do that today, from your own trade history.

::: prompt
Here is an anonymised history of my trades: [paste a CSV with time, asset, side, size, price, and whether each order was maker or taker]. Propose a trading policy for a signing service that refuses any order outside it. Give: the assets to allow, the largest single order, the most traded in a day, the maximum leverage, and whether orders should be post-only. Base each limit on what this history actually shows, with some headroom, and say why.
:::

Keep the answer. It is the first draft of the policy you will sign.

## What are the milestones?

1. **The next signer set.** Live with Policy v2: a price band, an order-rate cap, notional caps and post-only.
2. **Owner binding.** An owner binds their own account and key with their own wallet.
3. **Owner policy.** The owner writes and signs a policy with caps.
4. **A gated live test.** On a small account with real money, the same refusal, entry and close we ran for our own key.
5. **Open to outsiders.** This page gets the full steps.

## Final thoughts

The honest answer today is "not yet". We would rather open Signer to other people's money on the set that carries Policy v2 than on the one that doesn't.

Write your policy now. It is the part that takes the most thought, and it is ready when we are.

---
title: How do I write a trading policy?
description: The fields a Signer policy has today, what Policy v2 plans to add, what stays with you, and a prompt to draft one from your own history.
order: 4
---

After this page you will be able to read a Signer policy, say what each field limits, and draft one for your own agent with an AI model.

## What is a policy?

A policy is the owner's written limit on what one delegate key may trade.

The owner signs it with their wallet and writes it to the `signer-1` chain. Each signer reads it before signing.

One policy covers one delegate on one key. You can give two delegates two policies, and each gets its own caps.

## What fields does a policy have today?

These fields are live, taken from the chain code:

- **`venues`**: which venues the delegate may trade. It cannot be empty.
- **`vault_address`**: the sub-account the policy is pinned to. A signer refuses an order for any other.
- **`asset_caps`**: the assets the delegate may trade, each with a `max_order_size` and a `max_daily_size`. It cannot be empty.
- **`expires_at`**: when the policy ends, in unix seconds.
- **`revoked`**: set when the owner revokes it.

Coming: **max leverage**. It is in the code, but it only takes effect from a set future chain height.

The chain refuses a policy where `max_order_size` is above `max_daily_size`. It also refuses an empty list and a repeated asset.

## How do the size caps work?

Caps are sizes, per asset, per delegate, per UTC day. They bound how much, not at what price.

- **Asset allowlist.** An asset that is not listed cannot be traded, reduce-only included.
- **Order cap.** A single order may not be above `max_order_size`.
- **Daily cap.** Today's signed size for that delegate and asset, plus the new order, may not pass `max_daily_size`.

The daily cap counts signed size, not fills, and a failed round counts too. It is per delegate.

The owner-signed text says so.

## What is exempt from the size caps?

Reduce-only orders have no size caps and are not counted. A trader must always be able to get out.

The asset still has to be on the list.

That exemption is also the weak spot. The signer has no market price, so a sell at a low limit, or a buy-back at a high one, is still signed if it fits the caps.

Policy v2 is meant to close that.

## What is planned for Policy v2?

These items are **PLANNED**. They are not live, and we have no date.

- **PLANNED, price band.** A maximum distance of the limit price from the venue's mark price, in basis points, on every order with a price, close-only included. Each signer reads the mark itself, not from the request.
- **PLANNED, order rate cap.** A maximum number of orders signed per second, per key.
- **PLANNED, post-only per delegate.** One delegate that can only rest orders and never cross the spread.
- **PLANNED, notional caps.** A cap in value at the order's own limit price, as a second check beside the size caps.

Policy v2 needs another rotation of the signers before it arrives.

## What stays on your side?

A signer sees only the orders it signs. It never sees fills, so it cannot know your position or your loss.

Two limits therefore stay owner-side.

- **Position limits.** Your own risk monitor tracks your position per market.
- **Drawdown limits.** Your own monitor tracks your loss for the day.

When a limit is hit, your monitor revokes the policy on chain. The revoke is the hard stop.

The next article shows how it works.

## How can an AI model help me draft one?

Give your own AI model an anonymised summary of your trading.

Strip the venue, the dates and any account number. Keep markets, order sizes, daily volume, maker and taker share and order types.

We used this blind-test method on a case study. We gave AI models only an account's trade history, with no venue and no name, and asked what policy they would set.

The models disagreed in useful ways, so ask for reasons, not just numbers.

::: prompt
You are helping me write a trading policy for an agent that trades from a key it cannot hold. Below is an anonymised summary of my past trading: markets, order sizes, daily volume, maker and taker share, and order types. It has no venue, no dates and no account details.

The policy has these live fields per delegate: the list of allowed markets; a maximum order size per market; a maximum daily size per market; an expiry. Reduce-only orders are exempt from the size caps. Position limits and a daily loss limit are checked by me outside the policy.

For each field, propose a value taken from my history, and say which part of the history supports it. Say whether I should use one delegate key or two, for example one that only posts orders and one that takes liquidity. Tell me which of my limits you would put on the owner side, and how fast my revoke should react. List what the history cannot tell you.

My history:
[paste your anonymised summary here]
:::

Check what comes back against your own numbers. The model proposes.

You decide, and you sign.

## Final thoughts

A policy is short on purpose. It bounds markets and sizes, and the owner holds the rest.

Today it limits how much, not at what price, and we are open about that gap.

Next, read how to stop an agent fast.

---
title: How do I write a trading policy?
description: The limits you can set on your agent today, what the next version adds, what stays with you, and a prompt to draft your own.
order: 4
---

After this page you will be able to read a Signer policy, say what each field limits, and draft one for your own agent with an AI model.

## What is a policy?

A policy is the owner's written limit on what one agent key may trade. We call that agent the delegate, and its key the delegate key.

The owner signs the policy with their wallet and writes it to the `signer-1` chain. Each signer reads it before signing.

One policy covers one delegate on one key. You can give two delegates two policies, and each gets its own caps.

## What fields does a policy have today?

These fields are **Live**, taken from the chain code:

- **`venues`**: which venues the delegate may trade. It cannot be empty.
- **`vault_address`**: the sub-account the policy is pinned to, and a signer refuses an order for any other. "Vault address" is Hyperliquid's name for a sub-account, not TraderSwift Vault.
- **`asset_caps`**: the assets the delegate may trade, each with a `max_order_size` and a `max_daily_size`. It cannot be empty.
- **`expires_at`**: when the policy ends, in unix seconds.
- **`revoked`**: set when the owner revokes it.

**Built, not live: max leverage.** It is in the code, and it switches on by itself at a set block of the chain, about Thursday 26 November 2026.

The chain refuses a policy where `max_order_size` is above `max_daily_size`. It also refuses an empty list and a repeated asset.

## How do the size caps work?

Caps are sizes, per asset, per delegate, per UTC day. They bound how much, not at what price.

- **Asset list.** An asset that is not listed cannot be traded, reduce-only included.
- **Order cap.** A single order may not be above `max_order_size`.
- **Daily cap.** Today's signed size for that delegate and asset, plus the new order, may not pass `max_daily_size`.

The daily cap counts signed size, not fills, and a failed round counts too.

It is per delegate, so two delegates on one key each have their own daily cap.

## What is exempt from the size caps?

Reduce-only orders can only make a position smaller. They have no size caps and are not counted, because a trader must always be able to get out.

The asset still has to be on the list.

That exemption is also the weak spot. The signer has no market price, so a sell at a low limit, or a buy-back at a high one, is still signed if it fits the caps.

Policy v2 is meant to close that.

## What does Policy v2 add?

Policy v2 is **Built, not live**: it is built and in review. Our target is Saturday 21 November 2026, with the rotation of the signers that day.

Two terms first:

- **Mark price** is the venue's own fair price for a market.
- **A basis point** is one hundredth of one percent, so 50 basis points is 0.5%.

What Policy v2 adds:

- **Price band.** A maximum distance of the limit price from the mark price, in basis points. It applies to every order with a price, close-only included, and each signer reads the mark itself.
- **Order rate cap.** A maximum number of orders signed per second, per key.
- **Post-only per delegate.** A post-only delegate can only rest orders on the book and never trade against an order already there.
- **Notional caps.** Notional is the value of an order: size times its own limit price. A notional cap limits that value, as a second check beside the size caps.

## What stays on your side?

A signer sees only the orders it signs. It never sees fills, so it cannot know your position or your loss.

Two limits therefore stay with you.

- **Position limits.** Your own risk monitor tracks your position per market.
- **Drawdown limits.** Your own monitor tracks your loss for the day.

When a limit is hit, your monitor revokes the policy on the chain. The revoke is the hard stop.

The [next article](05-how-do-i-stop-an-agent-fast.html) shows how it works.

## How can an AI model help me draft one?

Give your own AI model an anonymised summary of your trading.

Strip the venue, the dates and any account number. Keep these:

- markets and order sizes;
- daily volume;
- maker and taker share;
- order types.

We used this blind-test method on a case study. We gave AI models only an account's trade history, with no venue and no name, and asked what policy they would set.

The models disagreed in useful ways, so ask for reasons, not just numbers.

::: prompt
You are helping me write a trading policy for an agent that trades from a key it cannot hold. Below is an anonymised summary of my past trading: markets, order sizes, daily volume, maker and taker share, and order types. It has no venue, no dates and no account details.

The policy has these live fields per delegate: the list of allowed markets; a maximum order size per market; a maximum daily size per market; an expiry. Reduce-only orders are exempt from the size caps. Position limits and a daily loss limit are checked by me outside the policy. Policy v2 adds a price band from the mark price, an order rate cap, post-only per delegate and notional caps: propose values for those too, marked as v2.

For each field, propose a value taken from my history, and say which part of the history supports it. Say whether I should use one delegate key or two, for example one that only posts orders and one that takes liquidity. Tell me which of my limits you would put on the owner side, and how fast my revoke should react. List what the history cannot tell you.

My history:
[paste your anonymised summary here]
:::

Check what comes back against your own numbers. The model proposes.

You decide, and you sign.

## Final thoughts

A policy is short on purpose. It bounds markets and sizes, and the owner holds the rest.

Today it limits how much, not at what price. Policy v2 adds the price band, with a target of Saturday 21 November 2026.

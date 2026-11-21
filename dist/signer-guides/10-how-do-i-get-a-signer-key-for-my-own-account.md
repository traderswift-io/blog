---
title: How do I get a Signer key for my own account?
description: Your own Hyperliquid account is planned for no earlier than Sunday 22 November 2026. What it waits on, what you will do, and what you can prepare now. Planned.
order: 10
---

**Built, not live.** Our target is no earlier than Sunday 22 November 2026, for your own Hyperliquid account.

From that day, Signer can hold a trading key for your own exchange account, under a policy you write and sign yourself.

You sign the setup in your own wallet. We never see or hold your keys.

When it opens, this page gets the exact steps.

## What does Sunday 22 November wait on?

Four things come first:

- **The rotation of the signers**: built and tested; waits on one signing moment, no date set. It brings the new signer machines and Policy v2.
- **Account privacy.** The release that keeps your trading account address and your orders out of readable form on the chain. [How do I read Signer's record?](06-how-do-i-read-signers-record.html) says what the chain shows.
- **Our decision on the security audit.** We make it before your account opens.
- **A live test done as a new user would.** We follow these steps ourselves, on a small account with real money, the way you will.

If a date slips, the box on the [Signer index](index.html) changes the same day, with the new date and the reason.

## What will I do?

The steps follow the same path Signer already uses for our own test account.

1. **Your account, your wallet.** You bind your exchange account and the new key with your own wallet, and nobody else can do it for you.
2. **A new key.** The signers make the key together, and it never exists whole on any machine.
3. **You approve it on the exchange.** The key is added to your account as an agent that can trade, not withdraw.
4. **You write the policy.** Which assets, how large an order and how much a day, as in [How do I write a trading policy?](04-how-do-i-write-a-trading-policy.html).
5. **You can stop it.** A revoke takes effect in the block it lands in, as [How do I stop an agent fast?](05-how-do-i-stop-an-agent-fast.html) explains.

## What will I sign?

Each step you sign in your wallet has a short, plain text, so you can read what you approve.

The exact texts you sign go on this page when the code that prints them is published.

## What can I prepare now?

Your policy. Most of the work in getting a key is deciding what it may do.

You can do that today, from your own trade history.

::: prompt
Here is an anonymised history of my trades: [paste a CSV with time, asset, side, size, price, and whether each order was maker or taker]. Propose a trading policy for a signing service that refuses any order outside it. Give: the assets to allow, the largest single order, the most traded in a day, the maximum leverage, and whether orders should be post-only. Base each limit on what this history actually shows, with some headroom, and say why.
:::

Keep the answer. It is the first draft of the policy you will sign.

## Final thoughts

Your own account has a date: no earlier than Sunday 22 November 2026, on the new signers with Policy v2.

Write your policy now. It is the part that takes the most thought, and it will be ready when your account opens.

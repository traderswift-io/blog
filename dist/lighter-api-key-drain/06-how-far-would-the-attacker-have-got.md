---
title: How far would the attacker have got?
description: We replayed the attack against each of the four sets of limits.
order: 6
---

We then replayed the attacker against each of the four policies (two models, two accounts).

The pool route is refused by request type under every one of them.

The question is what an attacker with only the trading key could do next.

Their best move is one the live policy fields do not cover.

## How does a close-only order become the attack?

A close-only order is exempt from the size caps, so a trader can always get out.

The attacker uses that. They rest their own order at an absurd price, then send a close-only order from the victim's key that fills against it.

A victim who is short can be made to buy back at up to 100 times the price, the most our search tried.

## What did the replay find?

Each share below is of what the attacker asked to withdraw from that account: 10,393,056.79 and 5,096,588.02 USDC.

| Policy fields in force | Largest tested value moved to the attacker | Share of the withdrawal from that account |
|---|---|---|
| Live today: markets, size caps, owner revoke | All of it: about $10.39M and $5.10M | About 100% |
| Plus post-only and notional caps | $34,000 to $911,000 | 0.7% to 8.8% |
| Plus the price band and the rate limit | $16,000 to $97,000 | 0.3% to 0.9% |

The middle row assumes the attacker sends 10 orders a second. It grows with speed: at 100 a second, one policy reached about $9.64M.

The last row holds at both speeds, 10 and 100 orders a second.

## What stops it?

A price band. Each signer reads the exchange's mark price on its own feed, and refuses any order, close-only included, priced too far from it.

If its own price is more than 3 seconds old and one fresh read fails, it refuses too. Each signer decides on its own and withholds its part of the signature; there is no vote.

We set each band from the account's own history, just above how far it crossed the spread 99% of the time.

Then a cap on orders signed per second, set from the account's own peak. The busiest second had 93 orders on one account and 95 on the other.

The band costs the trader almost nothing. Fitted to their own history, it would have refused 0.8% and 0.7% of the two accounts' taker fills.

## What are the limits of these numbers?

- **Largest tested, not proven maximum.** They are the largest values a scenario search found, not a ceiling.
- **Mid price as a stand-in for mark.** Lighter publishes no order-book or mark-price history, so the band was measured against the mid price as a stand-in for the mark.
- **The band limits, it doesn't eliminate.** An attacker can still trade at the edge of the band until the owner revokes.

The price band and the rate limit came out of this test.

Both are in Policy v2, which is built and switches on after the signer rotation, with no date set.

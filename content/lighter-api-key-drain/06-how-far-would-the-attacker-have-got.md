---
title: How far would the attacker have got?
description: A replay of the attacker against each policy, and the gap it found.
order: 6
---

We then replayed the attacker against each of the four policies (two models, two accounts).

The pool route is refused by request type under every one of them.

The question is what an attacker with only the trading key could do next.

Their best move is the one the policy table does not yet cover.

A close-only order is exempt from the size caps, so a trader can always get out.

The attacker uses that: they rest their own order at an absurd price, then send a close-only order from the victim's key that fills against it. A victim short 1,000 contracts at $10 can be made to buy them back at $10,000.

| Policy fields in force | Largest tested value moved to the attacker | Share of the $15.49M the attacker went for |
|---|---|---|
| Live today: markets, size caps, owner revoke | About $15.49M | About 100% |
| Plus the planned fields: post-only, notional caps | $34,000 to $911,000 | 0.7% to 8.8% |
| Plus the price band and the rate limit | $16,000 to $97,000 | 0.3% to 0.9% |

The planned-fields row assumes the attacker sends 10 orders a second. It grows with throughput.

The fix is a price band. Each signer reads the exchange's mark price on its own feed, and refuses any order, close-only included, priced too far from it.

If its own price is more than 3 seconds old and one fresh read fails, it refuses too. Each signer decides on its own and withholds its share; there is no vote.

We set each band from the account's own history, just above how far it crossed the spread 99% of the time. Then a cap on orders signed per second, set from the account's own peak.

The band costs the trader almost nothing. Fitted to their own history, it would have refused 0.8% and 0.7% of the two accounts' taker fills.

Three limits on these numbers:
- **Largest tested, not proven maximum.** They are the largest values a scenario search found, not a ceiling.
- **Mid price as a stand-in for mark.** Lighter publishes no order-book or mark-price history, so the band was measured against the mid price as a stand-in for the mark.
- **The band limits, it doesn't eliminate.** An attacker can still trade at the edge of the band until the owner revokes.

The price band and the rate limit came out of this test.

Our replay found the gap, and both are now in the next version of Signer's policy.

---
title: What policy would this market maker have set?
description: Two delegate keys, and what two AI models set blind.
order: 5
---

These two accounts did cross the spread, often.

In the 30 days before the incident, only about a third of one account's fills and a quarter of the other's were maker fills. So a simple "never cross the spread" rule would not fit them.

What fits is a split: the resting orders go through a key that can only post (post-only), and the taking goes through a second key with its own, tighter limits.

That gives two delegate keys, each with its own policy on chain.

Several delegates, each with its own caps, is live today. The signer enforces what the order itself proves; the account-level limits sit with the owner.

A signer sees only the orders it signs, never fills, so position and drawdown limits run in the owner's own risk monitor, which revokes the policy on chain when a limit is hit. The revoke is the hard stop.

| Policy field | Maker key | Taker key | Status |
|---|---|---|---|
| Markets allowed | The markets it actually trades | Fewer, the most liquid | Live |
| Max order size, per market | From its history | Lower | Live |
| Max daily size, per market | From its history | Lower | Live |
| Post-only (cannot cross the spread) | Yes | No | Next |
| Max notional per order and per day, at the order's own limit price (new risk; close-only exempt) | From its history | Low | Next |
| Max position per market | From its history | Low | Owner-side risk layer; revoke is the hard stop |
| Daily drawdown limit | Set | Set | Owner-side risk layer; revoke is the hard stop |
| Max leverage | Set | Set | Coming |
| Price band: max distance of the limit price from the venue's mark price, in bps, every order including close-only | Just above its own historical crossing | Just above its own historical crossing | Next |
| Max orders signed per second | From its peak | From its peak | Next |

We did not want to pick the policy ourselves, with hindsight. So we asked two AI models, Claude and Codex, to set it blind.

Each got only one account's 30 days of trades before the incident: markets, order sizes, daily volume, maker and taker share, order types. There was no venue, no dates, no account number and no word of the incident.

Each got the policy fields above and was asked what it would set.

A third model, Grok, will run the same test. This page will be updated with its answer.

They disagreed in an instructive way:

| | Claude | Codex |
|---|---|---|
| Keys | Two: a post-only maker key and a taker key | One key for both |
| Why | Rests orders in one market and hedges by crossing in another; split the two jobs | Crossing is two thirds of the fills; one key with tight limits |
| Leverage | 3x to 5x | 1x |
| Owner-side revoke | Within 1 to 5 seconds, on each fill | Account-wide position and drawdown limits |

Neither model was told what to protect against. Both, unprompted, flagged that these accounts only ever added to their positions in 30 days, and that the owner's revoke has to be fast, because the accounts traded at up to 95 orders a second.

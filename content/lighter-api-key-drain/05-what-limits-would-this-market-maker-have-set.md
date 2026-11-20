---
title: What limits would this market maker have set?
description: Two keys, and what two AI models chose without knowing about the incident.
order: 5
---

These two accounts did cross the spread, often.

A maker fill is a resting order that someone else traded against; a taker fill crosses the spread to trade against a resting order. In the 30 days before the incident, only about a third of one account's fills and a quarter of the other's were maker fills.

So a simple "never cross the spread" rule would not fit them.

What fits is a split: the resting orders go through a key that can only rest, and the taking goes through a second key with its own, tighter limits.

That gives two delegate keys, each with its own policy on chain.

Several delegates, each with its own caps, is live today.

## What does a signer check?

A signer checks what the order itself shows: its market, its size and its price.

A signer never sees fills, so position and drawdown limits run in the owner's own risk monitor. When a limit is hit, the monitor revokes the policy on chain, and the revoke is the hard stop ([how a revoke works](../signer-guides/05-how-do-i-stop-an-agent-fast.html)).

## Which fields could the owner set?

Four terms in the table, in plain words:

- **Post-only**: the order may only rest on the book. If it would cross the spread, it is refused.
- **Notional**: the order's size times its price, in dollars.
- **Mark price**: the exchange's own fair price for a market, the one it uses for margin.
- **Basis points (bps)**: hundredths of a percent. 100 bps is 1%.

The fields marked with a date are in Policy v2, which is **Built, not live** and in review, with a target of Sat 21 Nov 2026.

| Policy field | Maker key | Taker key | Status |
|---|---|---|---|
| Markets allowed | The markets it actually trades | Fewer, the most liquid | Live |
| Max order size, per market | From its history | Lower | Live |
| Max daily size, per market | From its history | Lower | Live |
| Post-only | Yes | No | Target Sat 21 Nov 2026 |
| Max notional per order and per day, at the order's own limit price (new risk only; close-only exempt) | From its history | Low | Target Sat 21 Nov 2026 |
| Max position per market | From its history | Low | Owner's risk monitor; the revoke is the hard stop |
| Daily drawdown limit | Set | Set | Owner's risk monitor; the revoke is the hard stop |
| Max leverage | Set | Set | From about Thu 26 Nov 2026 |
| Price band: how far the limit price may sit from the mark price, in bps, on every order, close-only included | Just above its own historical crossing | Just above its own historical crossing | Target Sat 21 Nov 2026 |
| Max orders signed per second | From its peak | From its peak | Target Sat 21 Nov 2026 |

## What did two AI models choose?

We did not want to pick the policy ourselves, with hindsight. So we asked two AI models, Claude and Codex, to set it blind.

Each got only one account's 30 days of trades before the incident:

- markets;
- order sizes;
- daily volume;
- maker and taker share;
- order types.

Each got none of these:

- the venue;
- the dates;
- the account number;
- any word of the incident.

Each got the policy fields above and was asked what it would set.

A third model, Grok, will run the same test. This page will be updated with its answer.

They disagreed in an instructive way:

| | Claude | Codex |
|---|---|---|
| Keys | Two: a post-only maker key and a taker key | One key for both |
| Why | Rests orders in one market and hedges by crossing in another; split the two jobs | Crossing is two thirds of the fills; one key with tight limits |
| Leverage | 3x to 5x | 1x |
| Owner-side revoke | Within 1 to 5 seconds, on each fill | Account-wide position and drawdown limits |

Neither model was told what to protect against.

Both, unprompted, flagged that the owner's revoke has to be fast, because these accounts sent bursts of many orders within a single second. Claude also flagged that in 30 days the accounts only ever added to their positions.

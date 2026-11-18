---
title: Where is Signer today?
description: Live on Hyperliquid since 14 November 2026, on a small live account with real money.
order: 8
---

Signer is in development.

It went live on 14 November on Hyperliquid mainnet, signing real orders with real money on a small live account, and the test showed it works:
- A buy at twice the order cap was refused before it reached the venue (`over_max_order_size`).
- After the policy was revoked on chain, the next order was refused (`policy_revoked`).
- Four transfer and withdrawal requests were refused.
- Every decision was recorded on chain.

The record is public in the [`signer-1-launch`](https://github.com/traderswift-io/signer/releases/tag/signer-1-launch) release.

- **Keys made by the signers together.** Every key on signer-1 except the launch key was generated jointly and never existed whole, including the one it trades with today. The Hyperliquid launch key was imported, because it was an agent the owner had already approved.

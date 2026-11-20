---
title: Where is Signer today?
description: Live on Hyperliquid since 14 November 2026, on a small live account with real money.
order: 8
---

Signer has been **Live** since Sat 14 Nov 2026.

It signs real orders with real money on Hyperliquid mainnet, on a small live account, and the launch test showed it works:

- A buy at twice the order cap was refused before it reached the venue (`over_max_order_size`).
- After the policy was revoked on chain, the next order was refused (`policy_revoked`).
- Four transfer and withdrawal requests were refused.
- Every decision was recorded on chain.

The record is public in the [`signer-1-launch`](https://github.com/traderswift-io/signer/releases/tag/signer-1-launch) release.

## What can it not do yet?

- It trades only TraderSwift's own test account.
- It does not support Lighter. Hyperliquid is the one live venue.
- The price band, the rate limit, post-only and notional caps are in Policy v2, built and in review, not live.

## What comes next, and when?

These are target dates. If one slips, the [Signer how-tos](../signer-guides/index.html) say so the same day, with the new date and the reason.

- **Rotation of the signers, with Policy v2**: target Saturday 21 November 2026.
- **Aster**: no date yet. It waits on its test account being funded, then a sitting after that.
- **Base (Avantis)**: no date yet.
- **Your own Hyperliquid account**: no earlier than Sunday 22 November 2026. You sign the setup in your own wallet, and we never see or hold your keys.

## How does Signer keep your account private?

This is how your own account works on Signer, from the rotation, target Saturday 21 November 2026.

Your trading account address and the contents of your orders never appear on signer-1 in readable form. The chain holds only fingerprints of them, which the signers check, and only the signers can open the details.

What the chain does show is that a policy exists, its markets, size limits and expiry, and when each request was signed or refused. So anyone can confirm the rules were followed.

In the next release, your markets and limits are kept private the same way.

Our own test account is public by choice.

Hyperliquid itself shows every account's orders and positions to anyone who knows the address. Signer does not add to that or change it.

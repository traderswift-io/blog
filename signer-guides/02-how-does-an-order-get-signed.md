---
title: How does an order get signed?
description: The path of one order from your agent's request to the exchange, and the record it leaves behind.
order: 2
---

After this page you will be able to follow one order through Signer, step by step, and say where each check happens.

## Who takes part in an order?

Four parts do the work. Each has one job.

**Your agent, the delegate.** The owner delegates trading to it, which means the owner lets it trade inside set limits. It holds its own delegate key, which signs its order requests and nothing else.

**The coordinator.** A small service, one per key, that passes requests along and sends the result to the venue. It holds no key share and no delegate key, so it cannot sign an order or forge one.

**The signers.** The machines that hold the key shares. Each one checks the order before it takes part.

**The chain, `signer-1`.** It holds the owner's policy and the record of every decision.

## What does the agent send?

The agent sends an order request, which we call an intent.

An intent says what to trade:

- the venue and the asset;
- buy or sell;
- the limit price and the size;
- whether it is reduce-only, meaning it can only make a position smaller;
- an expiry.

The agent signs the intent with its delegate key.

An intent expires fast. Signers refuse an expiry more than 120 seconds ahead.

Each intent also carries a nonce, a number that goes up by one with every order. An old intent has an old number, so it cannot be sent again.

The agent works in two calls to the coordinator. First it asks for the next nonce, then it signs the intent and sends it.

## What does the coordinator do?

The coordinator asks one signer to start a signing round. It runs rounds on a key one at a time.

If that signer is down, or refuses for a local reason, it asks the next. A refusal on policy grounds is final.

It also rebuilds the venue message on its own. When a signature comes back, it checks that the signature matches the key's address at the venue.

If it does not, nothing is posted.

## What does each signer check?

The signer never accepts a hash, a short fingerprint of a message. It builds the venue message itself from the intent.

Then it checks, from its own copy of the chain:

- **The delegate.** The signature is valid and the intent has not expired.
- **The policy.** The venue is allowed, and the policy is not revoked or expired. Its epoch, a counter that goes up with every policy change, must match.
- **The asset.** The asset is on the policy's list.
- **The size.** The order is within the per-order cap and the daily cap.
- **The nonce.** The nonce is above the highest this signer has signed for the key.

Transfers, withdrawals and any request that is not a trade are refused by kind, before any policy field is read.

If the chain looks out of date to a signer, it signs only cancels and reduce-only orders.

## How do they sign without building the key?

The signers run a threshold signing protocol with each other. Each uses its own share, and no share leaves its machine.

The result is one ordinary signature, made by any three of the four signers. The venue accepts it as if one key had signed.

Sharing a secret and signing with shares are not the same thing. Our cryptography guide explains the difference in [Shamir: which threshold really applies?](../cryptography/08-shamir-which-threshold-really-applies.html).

No signer ever sees the whole key, and the coordinator never sees a share.

All signers in a round work live, at the moment of the order.

Some systems prepare part of the work in advance, called presignatures. Signer does not use them.

## How does the order reach the venue?

When the signature is back and checked, the coordinator posts the order to the venue.

On Hyperliquid, it is the venue's own order message with the signature attached.

By default, the coordinator refuses to post anywhere but a local test address.

Only the operator can switch on the live Hyperliquid address.

## What gets recorded?

Every request goes to the chain as a decision record, signed or refused, with the reason. Each signer writes its own.

For a normal order on a three-of-four set you see four lines. Three signers record `signed`.

The one not chosen records `refused` with the reason `quorum_met_without_this_signer`. That means enough signers had already agreed without it.

So a refusal on the chain does not always mean a refused order. Read the reason.

Signers write to a local outbox first, so a record can arrive a little after the order. The order never waits for it.

## What happens when something is wrong?

- **Over the cap.** The signer refuses with a reason such as `over_max_order_size`, and the order never reaches the venue.
- **Revoked policy.** Nothing new is signed. [How do I stop an agent fast?](05-how-do-i-stop-an-agent-fast.html) says what still works for 600 seconds.
- **Chain out of date or signer restarted.** A restarted signer refuses everything until enough peers answer. Cancels wait too.

<!-- source: signer/src/policy_rules.rs (over_max_order_size); chain/policy/msg_server_policy.go (policy_revoked) -->

## Final thoughts

An order passes three gates before the venue sees it: the delegate's signature, each signer's own policy check, and the coordinator's check of the signature.

No single machine can sign alone. Next, read [how to write the policy](04-how-do-i-write-a-trading-policy.html) those signers check.

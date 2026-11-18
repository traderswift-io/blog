---
title: How does an order get signed?
description: The path of one order from an agent's request to the venue, and the decision record it leaves on the chain.
order: 2
---

After this page you will be able to follow one order through Signer, step by step, and say where each check happens.

## Who takes part in an order?

Four parts do the work. Your agent is the **delegate**: it holds a delegate key and signs its own order requests.

The **coordinator** is a small service, one per key, that passes requests along and sends the result to the venue.

The **signers** hold the key shares. The **chain**, `signer-1`, holds the owner's policy and the decision records.

The coordinator holds no key share and no delegate key. It cannot sign an order and it cannot forge one.

This is the design on purpose.

## What does the agent send?

The agent sends an order intent: the venue, the asset, buy or sell, limit price, size, whether it is reduce-only, and an expiry. The intent is signed with the delegate key.

An intent expires fast. Signers refuse an expiry more than 120 seconds ahead.

Each intent also carries a rising venue nonce, so an old intent cannot be replayed.

The agent works in two calls to the coordinator. First it asks for the next nonce, then it signs the intent and sends it.

## What does the coordinator do?

The coordinator asks one signer to start a round, and it runs rounds on a key one at a time. If that signer is down, or refuses for a local reason, it asks the next.

A refusal on policy grounds is final.

It also rebuilds the venue message and its digest on its own. When a signature comes back, it checks that the signature recovers to the key's venue address.

If it does not, nothing is posted.

## What does each signer check?

The signer never accepts a hash. It builds the venue message itself from the intent, and then it checks, from its own copy of the chain:

- **The delegate.** The signature is valid and the intent has not expired.
- **The policy.** The venue is allowed, the policy is not revoked or expired, and its epoch matches.
- **The asset.** The asset is on the policy's list.
- **The size.** The order is within the per-order cap and the daily cap.
- **The nonce.** The nonce is above the highest this signer has signed for the key.

Transfers, withdrawals and any request that is not a trade are refused by kind, before any policy field is read. If the chain looks stale to a signer, it signs only cancels and reduce-only orders.

## How do they sign without building the key?

The signers run a threshold signing protocol with each other. Each uses its own share and no share leaves its machine.

The result is one ordinary signature, made by any three of the four signers, that the venue accepts as if one key had signed.

No signer ever sees the whole key, and the coordinator never sees a share. It is a full interactive protocol with no presignatures.

## How does the order reach the venue?

When the signature is back and checked, the coordinator posts the order to the venue.

On Hyperliquid, it is the venue's own order message with the signature attached.

By default, the coordinator refuses to post anywhere but a local test address.

Only the operator can switch on the live Hyperliquid address.

## What gets recorded?

Every request goes to the chain as a decision record, signed or refused, with the reason. Each signer writes its own.

For a normal order on a three-of-four set you see four lines. Three signers record `signed`.

The one not chosen records `refused` with the reason `quorum_met_without_this_signer`.

So a refusal on the chain does not always mean a refused order. Read the reason.

Signers write to a local outbox first, so a record can arrive a little after the order. The order never waits for it.

## What happens when something is wrong?

- **Over the cap.** The signer refuses with a reason such as `over_max_order_size`, and the order never reaches the venue.
- **Revoked policy.** Orders are refused. Cancels still sign, so you can pull resting orders.
- **Chain stale or signer restarted.** A restarted signer refuses everything until enough peers answer. Cancels wait too.

<!-- source: signer/src/policy_rules.rs (over_max_order_size); chain/policy/msg_server_policy.go (policy_revoked) -->

## Final thoughts

An order passes three gates before the venue sees it: the delegate's signature, each signer's own policy check, and the coordinator's recovery check. No single machine can sign alone.

Next, read how to write the policy those signers check.

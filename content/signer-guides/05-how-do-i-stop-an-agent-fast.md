---
title: How do I stop an agent fast?
description: Revoke the policy on the Signer chain and every later order from that delegate is refused.
order: 5
---

After this page you will know how to stop an agent's trading with one signed message, and what still works after you do.

## What does a revoke do?

A revoke marks the delegate's policy as revoked on the `signer-1` chain.

After it, each signer refuses new orders from that delegate. It does not wait for a person to call the venue.

The owner signs the revoke with their wallet. Nobody else can send it, and a captured signature cannot be replayed, because each revoke must carry the next epoch for the key.

## How fast is it?

At the launch on 14 November, we revoked the policy at height 161,327. The next order was refused at height 161,330.

That is three blocks.

## What do I need to send it?

You need the owner wallet that claimed the account, and the next epoch for the key. The epoch is one counter per key.

Every policy change and every revoke must carry the counter plus one.

The next value is shown as `policy_epoch` when you read the key on the chain:

```
GET /signer/policy/v1/keyref/{key_ref}
```
<!-- source: chain/README.md:138 -->

The owner signs a short text, and that text is in the public tree:

```
signer revoke policy
chain id: <chain id>
key ref: <key_ref>
delegate key: <hex>
epoch: <n>
```
<!-- source: chain/README.md:127 -->

This is the text your wallet signs. It goes to the chain as a `RevokePolicy` message.

There is no one-line command for it in the public code yet.

## How do I see that it worked?

Read the policy back from the chain. The `revoked` field is true, and `revoked_at` holds the block time.

```
GET /signer/policy/v1/policy/{key_ref}/{delegate_key}
```
<!-- source: chain/README.md:138 -->

Then look at the decision records for the next order. It should be refused with a reason, and the refusal is public.

## Does a revoke close everything at once?

Not quite. New orders stop.

Some things still go through, on purpose.

- **Cancels.** A cancel still signs after a revoke, so you can pull resting orders.
- **Close-out window.** The policy closes fully 600 seconds after the revoke. After that, everything from that delegate is refused.
- **Repeat revokes.** A second revoke does not move `revoked_at`. The first one holds.

Setting a new policy clears the revoke. So if you want the delegate gone for good, do not set one.

## Who should send the revoke?

You can send it yourself. You can also hand the job to your own risk monitor.

A signer sees only orders, never fills, so it cannot track your position or loss. Your monitor can.

Write the rule in the open: when position or daily loss passes your limit, revoke.

Position and drawdown limits are owner-side by design, and the revoke is what makes them hard.

::: prompt
I run a trading agent that signs through Signer. Help me write a risk rule that decides when to revoke the agent's policy on chain. The rule should name my position limit per market, my daily loss limit, and what happens after a revoke: who is told, and how I check that the next order was refused. Ask me for the numbers one at a time. Do not guess them. Do not write code that holds my wallet key.
:::

## What stops without a revoke?

Two other things end an agent without any message. A policy has an `expires_at`, and after it the delegate is refused, again after the same 600 second close-out.

Transfers and withdrawals are always refused, whatever the policy says.

## Final thoughts

The revoke is one signed message and a few blocks. It stops new orders, and it leaves cancels so you can clear the book.

It is the hard stop behind every owner-side limit.

Next, go back to the policy article and decide which limits you want to hold yourself.

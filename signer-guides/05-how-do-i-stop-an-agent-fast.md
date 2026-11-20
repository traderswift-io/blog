---
title: How do I stop an agent fast?
description: One message signed in your wallet stops your agent from placing anything new.
order: 5
---

After this page you will know how to stop an agent's trading with one signed message, and what still works after you do.

## What does a revoke do?

A revoke marks the agent's policy as revoked on the `signer-1` chain. We call the agent the delegate.

A revoke takes effect in the block it lands in.

From then on the policy allows nothing new: no new orders, and no size increases.

For 600 seconds after the revoke, the agent can still cancel orders and arm a timed cancel-all, so it can tidy up; after that, everything is refused.

At launch, the next order after the revoke was refused, and the refusal was on chain three blocks later.

Each signer does this on its own. Nobody has to call the venue.

## Who can send it?

Only the owner. The owner signs the revoke with the wallet that claimed the account.

A copied revoke cannot be sent twice, because of a counter called the epoch.

## What is the epoch?

The epoch is one counter per key. Every policy change and every revoke must carry the counter plus one.

So an old signed message carries an old number, and the chain refuses it.

## What do I need to send it?

You need the owner wallet and the next epoch for the key.

The next value is shown as `policy_epoch` when you read the key on the chain:

```
GET /signer/policy/v1/keyref/{key_ref}
```
<!-- source: chain/README.md:138 -->

The `key_ref` is the key's name on the chain.

The owner signs a short text, and that text is in the public repository:

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

## What else should I know?

- **Repeat revokes.** A second revoke does not move `revoked_at`. The first one holds.
- **A new policy clears the revoke.** If you want the delegate gone for good, do not set one.

## Who should send the revoke?

You can send it yourself. You can also hand the job to your own risk monitor.

A signer sees only orders, never fills, so it cannot track your position or loss. Your monitor can.

Write the rule in the open: when position or daily loss passes your limit, revoke.

Position and drawdown limits stay with you by design, and the revoke is what makes them hard.

::: prompt
I run a trading agent that signs through Signer. Help me write a risk rule that decides when to revoke the agent's policy on chain. The rule should name my position limit per market, my daily loss limit, and what happens after a revoke: who is told, and how I check that the next order was refused. Ask me for the numbers one at a time. Do not guess them. Do not write code that holds my wallet key.
:::

## What stops without a revoke?

A policy has an `expires_at`. After it, the delegate is refused, again after the same 600-second window for cancels.

Transfers and withdrawals are always refused, whatever the policy says.

## Final thoughts

The revoke is one signed message. It stops anything new, and it leaves cancels so you can clear the book.

It is the hard stop behind every limit you keep yourself. Next, go back to the [policy article](04-how-do-i-write-a-trading-policy.html) and decide which limits those are.

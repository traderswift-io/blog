---
title: What can other people see on the chain?
description: How Signer keeps your account private, what the chain does show, and why.
order: 11
part: Security, which is more than the key
---

Signer is built to keep your account private.

This chapter says what is kept private, what the chain does show, and why.

## How does Signer keep your account private?

Your trading account address and the contents of your orders never appear on `signer-1` in readable form. The chain holds only fingerprints of them, which the signers check, and only the signers can open the details.

What the chain does show is that a policy exists, its markets, size limits and expiry, and when each request was signed or refused, so anyone can confirm the rules were followed.

In the next release, your markets and limits are kept private the same way. Our own test account is public by choice.

This is how Signer works for user accounts, with the rotation, which has no date set yet. Your own Hyperliquid account can join after the signer rotation; no date set.

## What else is never on the chain?

- **Your key** – or any share of it.
- **Your fills** – and your positions and balances.
- **Your strategy** – nothing on the chain describes how you trade.

## Why does the chain show anything at all?

So that you can check the rules were followed.

Your limits are enforced by machines you don't run. The record is how you can see that they did.

## What does the exchange show?

The exchange is separate from Signer.

On Hyperliquid, every account's orders and positions are public to anyone who knows the account's address. That is how the exchange works, and Signer does not add to it or change it.

That is why Signer keeps your account address off its chain in readable form.

## What if I want nothing on a shared chain?

Run Signer as your own private chain.

Signer is open source. You can launch your own Signer chain, with your own signers, without connecting to us.

The how-to [How do I run my own Signer chain?](../signer-guides/09-how-do-i-run-my-own-signer-chain.html) shows how.

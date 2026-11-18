---
title: How does Signer work?
description: Where the key comes from, how it is split, how an order is signed, and how you stop it.
order: 6
---

Signer lets an agent trade from a key it never holds.

This chapter goes one step at a time.

## Where does the key come from?

There are two ways.

The owner can pass in a key they already have.

Or Signer can make a new key.

## How is the key split?

Either way, the key ends up in pieces, called shares.

Each share sits on a different machine, called a signer.

A key Signer makes never exists whole. It is made in pieces, and nobody ever sees the whole key.

A key the owner passes in existed whole once, before it was split.

Today there are four signers, so four shares. At launch there were three.

## Who writes the rules?

The owner does.

The owner writes down what the agent may trade: which markets, how big an order, how much in a day, and until when.

Those limits are called a policy. The owner signs it with their own wallet, and it is kept on a public blockchain called `signer-1`.

## How does an order get signed?

The agent sends an order request. It signs the request with its own small key, which cannot sign anything at the exchange.

Each signer reads the request and checks it against the policy on the chain.

If the order fits, the signer builds the exchange message itself and signs its part. It never signs a message someone else hands it.

Any three of the four parts make a full signature. Two are not enough.

The full signature goes to the exchange, and the order is placed.

## What is recorded?

Every decision, signed or refused, is recorded on `signer-1`.

Anyone who runs a node can read that record.

## What can the agent never do?

The agent can send trading requests only: orders, cancels and a timed cancel-all.

Signer never signs a transfer or a withdrawal. Moving funds stays with the owner's own wallet.

## How do I stop an agent?

The owner signs one message that revokes the policy.

At our launch on 14 November 2026, the policy was revoked on chain, and the next order was refused and recorded three blocks later.

## Where do I learn more?

The [Signer guides](../signer-guides/index.html) show how to try it, write a policy, stop an agent and read the record.

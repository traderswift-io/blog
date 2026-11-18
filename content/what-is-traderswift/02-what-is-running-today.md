---
title: What is running today?
description: Signer, the hub chain and the charts data node.
order: 2
---

Three parts are running today.

## Signer

Signer lets an agent trade from a key it never holds.

An agent should not hold its trading key itself. If the agent's machine is broken into, the key goes with it.

Signer can take a key the owner already has, or make a new one.

Either way, the key ends up in pieces, called shares, each on a separate machine. A key Signer makes never exists whole: it is made in pieces, and nobody ever sees the whole key. A key the owner passes in existed whole once, before it was split.

Today there are four shares, on four separate machines. At launch there were three.

To sign an order, any three of the four machines must agree. Each one first checks the order against the owner's written limits.

Those limits, called a policy, are kept on a public blockchain, `signer-1`. Anyone who runs a node can check them, and every yes or no is recorded there.

It has signed live orders since 14 November 2026. Our [Signer guides](../signer-guides/index.html) show how to use it.

## The hub

The hub, `traderswift-1`, is the chain at the centre. It holds identities and the validator set.

It is where each subnet's charter, its providers and their anchors are registered. The first charters go on next.

It holds no token and no balances, and it charges no fees.

## The charts data node

A charts data node keeps hourly market candles and serves them through one documented interface.

Every day it publishes a hash of that day's candles. Anyone can recompute the hash and compare one node against another.

The node is open source and runs on its own. Posting its daily hashes to the hub is being built.

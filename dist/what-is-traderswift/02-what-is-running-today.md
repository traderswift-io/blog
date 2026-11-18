---
title: What is running today?
description: Signer, the hub chain and the charts data node.
order: 2
---

Three parts are running today.

## Signer

Signer lets an agent trade from a key it cannot hold.

The key exists only as shares, held by separate signers that generated it together. Each one checks the owner's written policy before it signs, and every decision goes on a public chain, `signer-1`.

It has signed live orders since 14 November 2026. Our [Signer guides](../signer-guides/index.html) show how to use it.

## The hub

The hub, `traderswift-1`, is the chain at the centre. It holds identities and the validator set.

It is where each subnet's charter, its providers and their anchors are registered. The first charters go on next.

It holds no token and no balances, and it charges no fees.

## The charts data node

A charts data node keeps hourly market candles and serves them through one documented interface.

Every day it publishes a hash of that day's candles. Anyone can recompute the hash and compare one node against another.

The node is open source and runs on its own. Posting its daily hashes to the hub is being built.

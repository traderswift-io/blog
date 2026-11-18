---
title: What is running today?
description: Signer, the hub chain and the charts data node.
order: 7
---

Three parts are running today.

## Signer

Signer has signed live orders on Hyperliquid since 14 November 2026, on a small live account with real money.

The chapter before this one explains how it works.

## The hub

The hub, `traderswift-1`, is the chain at the centre. It holds identities and the validator set.

It is where each subnet's charter, its providers and their anchors are registered. The first charters go on next.

It holds no token and no balances, and it charges no fees.

## The charts data node

A charts data node keeps hourly market candles and serves them through one documented interface.

Every day it publishes a hash of that day's candles. Anyone can recompute the hash and compare one node against another.

The node is open source and runs on its own. Posting its daily hashes to the hub is being built.

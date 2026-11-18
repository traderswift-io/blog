---
title: What is TraderSwift?
description: An open infrastructure layer for agentic and hybrid trading.
order: 1
---

TraderSwift is a blockchain infrastructure layer for agentic and hybrid trading.

Agentic means software agents place the trades. Hybrid means a person and an agent trade together.

Either way, the agent needs the same things. It needs a way to sign orders without holding a key, market data it can check, and a record of what it did that nobody can quietly change.

TraderSwift provides those as open-source parts. Anyone can read the code, run a node, or build on top.

## Who is it for?

- **Traders** who want an agent to trade for them, with limits the agent cannot break.
- **Builders** who want to make front ends and apps on top of it, and charge for them.
- **Node operators** who want to run part of the network.

## How do builders get paid?

Through x402, a standard for paying inside a web request. It settles in USDC on Base.

A builder puts a price on a request. The caller pays, and the request goes through.

The payment design is accepted, and the wallet can pay.

The first real payment has not been made yet.

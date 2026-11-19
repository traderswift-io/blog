---
title: How can I check market data?
description: Our market data node, its daily fingerprint, and how you can compare it with a copy of your own.
order: 14
part: Data you can check
---

Market data is only useful if you can trust it.

A trading agent acts on prices. If the prices are wrong, late or changed afterwards, every decision built on them is wrong too.

Most traders take their data feed on trust. They cannot tell whether two providers saw the same market, or whether last month's history was edited.

TraderSwift lets you check instead.

## What is the market data node?

The market data node is a program that keeps market candles and serves them through one documented interface.

A candle sums up one period of trading, such as an hour, in a few numbers, such as the opening and the closing price.

The node is open source under the Apache License 2.0, at [traderswift-io/timeseries-node](https://github.com/traderswift-io/timeseries-node). Anyone can download it and run a copy of their own.

## What is the daily fingerprint?

At the end of each day, the node works out one short code from all of that day's candles.

We call it a fingerprint, and its technical name is a hash. Change a single price anywhere in the day, and the fingerprint comes out completely different.

So two nodes with the same fingerprint for a day hold exactly the same candles for that day.

The day runs on UTC, the world's reference time, so every node closes the day at the same moment.

## How do I compare my node with yours?

Run the public node yourself, and let it build its own copy of the candles. Then compare its fingerprint for a day with ours.

If they match, your copy and ours agree, price for price.

We tested this ourselves. A fresh node, started from nothing, matched our fingerprint for Mon 16 Nov 2026.

## Why does this help me?

- **You can catch bad data** – if a provider's history does not match the fingerprint, you know before your agent trades on it.
- **You do not have to take our word** – your own node is the check, not a promise from us.
- **A data provider builds a record** – a node that matches day after day has shown it is reliable, and one that does not has shown that too.

## Can I read your node directly?

Not yet.

Our node runs and serves candles today, but its public address is still behind a login. So today you cannot read our data yourself, or recompute our fingerprints from it.

Running the public node yourself, and comparing fingerprints, is the way to check today.

## What comes next?

The next step is posting each day's fingerprint to the hub. The hub is the shared chain at the centre of TraderSwift, and [chapter 24](24-how-does-the-network-fit-together.html) explains it.

Once a fingerprint is on the hub, it is fixed in time. Nobody, including us, could change a past day's fingerprint without it showing.

The code that posts and checks fingerprints is built, but no fingerprint has been posted yet. It waits on two steps on the hub: adding the market data chain's entry, called its charter, and registering our node under it.

Paying for data per request is built too, and has not been run live. [Chapter 20](20-what-is-the-marketplace-and-how-do-builders-get-paid.html) explains how payment works.

## What is live?

- **Live** – the open-source node, which anyone can run and compare today.
- **Built, not live** – our own node for you to read: it serves candles, but behind a login.
- **Built, not live** – posting and checking daily fingerprints on the hub.
- **Built, not live** – paying for data per request.

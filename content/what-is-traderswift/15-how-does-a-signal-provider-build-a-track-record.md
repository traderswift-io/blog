---
title: How does a signal provider build a track record?
description: Why a trade idea should be fixed before the outcome, and how anyone can check it afterwards.
order: 15
part: Data you can check
---

Many people say they offer good trade signals.

Very few can show it. A track record is usually a screenshot, a spreadsheet or a list of wins.

It is easy to leave out the losers, or to move an entry after the fact.

TraderSwift gives a signal provider a track record that is built as they go, not written up afterwards. The track record is the point.

## What is a signal?

A signal is a trade idea, published by a person or by a machine.

On TraderSwift, every signal is a fixed record with the same fields:

- **Market** – what to trade.
- **Side** – buy or sell.
- **Levels** – where to enter, and where to take profit.
- **Invalidation** – the price at which the idea is wrong.
- **Confidence** – how sure the provider is.
- **Expiry** – when the idea stops counting.

If a signal is missing its invalidation, its confidence or its expiry, the provider is asked for it. Nothing is guessed.

## How is the record fixed?

When a signal is published, it gets a fingerprint: a short code made from the signal's content and the exact time it was published. [Chapter 14](14-how-can-i-check-market-data.html) explains fingerprints.

The fingerprint is made before the outcome is known.

So a provider cannot later claim a move they did not call, or move a stop after the price hit it.

## How can someone check a past signal?

The provider reveals a past signal: its content and its publish time.

Anyone can work out the fingerprint again from what was revealed, and compare it with the one made at the time. If the two match, the signal is exactly what was published, at exactly that time.

If one field was changed, even by one digit, they do not match.

## Can anyone tell who follows a signal?

Not from the fingerprint.

The fingerprint is made from the signal only, and holds nothing about who received it. The signal's content stays private, and only the wallets the provider has authorised can read it.

The planned Signals chain will keep one delivery record for each subscriber. Those records are private too.

## Can the record be rewritten today?

Today, the fingerprints are kept in our own store.

So for now the record is only as fixed as our store. It becomes impossible to rewrite only once the fingerprints are on a chain.

That step is planned: a private Signals chain, run by our validators. A validator is one of the machines that keep a chain's record.

Posting fingerprints to the hub, so that anyone can check them in public, may come later.

## Why does this help me?

- **As a provider** – your record speaks for you, and you do not have to ask anyone to believe you.
- **As a follower** – you can ask a provider to reveal past signals and check them yourself, before you follow them.

## What is live?

- **Built, not live** – fingerprinting signals. No real signal has been published with it yet.
- **Planned** – the private Signals chain.
- **Planned** – fingerprints on the hub, for a public check.

To see how a signal can become a trade through Signer, read [What are Signals and the desk?](../since-lockbox/07-what-are-signals-and-the-desk.html) in Since Lockbox.

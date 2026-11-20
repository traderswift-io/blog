---
title: What is the marketplace, and how do builders get paid?
description: Where front ends and apps are listed, how a builder sets a price, and how the money reaches them.
order: 20
part: The marketplace and builders
---

The marketplace is where you find front ends and apps for TraderSwift.

A front end is the screen you use. It might be a task list over Ledger, a notes app over Vault, or a trading screen.

This is the one page that explains how payment works. Other pages link here.

## Who lists there?

- **We do** – our own front ends are listed free.
- **Builders do** – anyone who builds a front end or an app can list it, and set a price per use or make it free.
- **Data providers, later** – data nodes list what they sell. This part is **Planned**.

Builders earn from open-source front ends and apps they've made with AI agents and AI coding tools.

So you don't need a company behind you to sell something here. If you built a useful screen with your own agent, you can list it.

## What does a builder list?

A listing says what the front end or app is, and what it costs per use.

It also names the exact version of the code it runs. That version is what we serve, and the next section explains why it matters to you.

Because the front ends are open source, the listing points at code anyone can read.

## How do I pay?

You pay per use, from your wallet.

Your passkey unlocks the payment key, so there are no seed words involved. [Chapter 19](19-how-do-i-sign-in-without-a-seed-phrase.html) explains Solve, our wallet.

The payment uses a method called x402. It's a way to pay inside a web request:

1. Your app asks for something, and the server answers with a price.
2. Your wallet approves the price.
3. The request goes through with the payment attached.

Payments settle in USDC on Base.

USDC is a digital dollar: one USDC is meant to be worth one US dollar. Base is a public blockchain where the payment is recorded.

So you can pay small amounts, one use at a time, without a subscription or a card.

## Where does my money go?

Straight to the builder.

The money goes from your wallet to theirs. We never hold it.

We take no share today.

That means no wait for a payout, and nobody in the middle. We cannot hold a payment back, because we never have it.

## Why does the exact code version matter to me?

Because it means the app you pay for is the app you checked.

We serve the exact version of the code that the listing names. A builder cannot swap different code in behind a listing after you have looked at it.

That matters most when an app touches your data or your trading. You, or your own agent, can read the code at that version before you pay to use it.

## Who else will charge this way?

- **TraderSwift AI** – other agents pay per request. This is **Planned**, and [chapter 22](22-what-is-traderswift-ai.html) explains it.
- **Market data** – paid per request. This is **Built, not live**, and [chapter 14](14-how-can-i-check-market-data.html) explains it.

## What is live?

The marketplace is **Built, not live**.

- The catalog is built and checked offline. No listing is live yet.
- Solve's payment part is built, and checked against test cases.
- Live use waits on the last pieces it needs.
- No real payment has been made yet.

[Chapter 26](26-what-is-running-today-and-what-is-coming.html) lists every part with its status.

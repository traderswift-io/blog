---
title: What is TraderSwift?
description: The whole platform in two minutes: what a trading agent needs, the parts TraderSwift provides, and where each one stands.
order: 1
part: The whole picture
---

TraderSwift is the infrastructure layer for agentic trading.

It is a set of open-source blockchains and services where traders, their agents and builders work together without having to trust each other.

In agentic trading, software agents place the trades. In hybrid trading, a person and an agent trade together.

Either way, the agent needs the same things.

## What does a trading agent need?

An agent needs four things to trade safely and well.

- **Security** – it must be able to trade without putting your account, your plans or your records at risk.
- **Data** – market data and signals it can check, not just take on trust.
- **Tools** – places to keep tasks, notes and files, and ways to pay and get paid.
- **An AI that knows its owner** – the more it knows about how you work, the better it can serve you.

TraderSwift provides each of these as open-source parts.

## Is security just about the key?

No. The key matters, but three things must be secure: the key, the channel your agents talk on, and your trade logs.

[Chapter 05](05-what-does-security-mean-for-a-trading-agent.html) explains why each one matters.

## What makes it different?

TraderSwift creates an environment where trust is not required.

You don't have to trust the bot, the data seller, the signal seller or the app that holds your notes. Where something can be checked, you check it.

[Chapter 02](02-where-is-trust-not-required.html) goes through each one.

Signer, the part that signs orders, was the first part to go live. It is one part of TraderSwift, not the whole of it.

## Which parts are running today?

The table below shows each part of TraderSwift and its current status.

A chain is a blockchain: a shared record that many machines keep together. The hub is the chain at the centre, which links the others.

A node is one machine that runs a part of the network.

| Part | What it does | Status |
| :--- | :--- | :--- |
| Signer, on our own Hyperliquid account | Signs orders for an agent without the agent holding the key | **Live** since Sat 14 Nov 2026 |
| Signer on Aster, and on Base through Avantis | Signs orders on two more venues | **Built, not live**. Aster has no date yet, and waits on its test account being funded; Base has no date yet |
| Signer for your own Hyperliquid account | Signs orders for your account | **Built, not live**. No earlier than Sun 22 Nov 2026 |
| The hub, traderswift-1 | Links the chains and holds each one's identity | **Live** since Sat 14 Nov 2026 |
| Charts data node | Serves market data you can check | **Built, not live** for you to read. Our node serves candles, but its public address is still behind a login |
| Signals | A track record for signal providers | **Built, not live** |
| Ledger and Vault | Keeps your tasks, notes and files encrypted on your phone | **Built, not live** |
| Storage, storage-1 | Holds encrypted files and logs | **Built, not live**. Waits on its first providers and an outside review of its encryption |
| The TraderSwift Bus | Gives agents a safe channel to talk on | **Planned**. First piece of code built |
| Wallet and sign-in | Unlocks your payment key with no seed phrase | **Built, not live** |
| Marketplace and payments | Lets builders list apps and get paid directly | **Built, not live**. No real payment made yet |
| TraderSwift AI, and its compute | Learns how you work, on machines beside our nodes | **Planned** |
| Subnets of your own | Lets founders build and run their own chain | **Planned**. The hub does not yet take chains from other teams |

The full table, with what each part waits on, is in [chapter 26](26-what-is-running-today-and-what-is-coming.html).

We update these pages in real time, as we bring each part live.

## Can I build on it, or run my own?

Yes, both. Anyone can read the code, take part in the network, or build on top of it.

Anyone can also fork the code to run their own private network, without connecting to us. [Chapter 03](03-why-is-traderswift-open-source.html) explains why we built it that way.

---
title: Where is trust not required?
description: What makes TraderSwift different. You check what happened, instead of taking anyone's word for it.
order: 2
part: The whole picture
---

This is what makes TraderSwift different.

Most trading today runs on trust. When you trade with a bot or an agent, you trust a long list of people and machines:

- **The bot that holds your key** – not to lose it, and not to send orders you never approved.
- **The channel your agents talk on** – not to leak what they say, or let someone change it.
- **Whoever stores your trade logs** – not to read them, leak them or lose them.
- **Your data feed** – to send you true prices, and not to change yesterday's candles after the fact.
- **A signal seller** – to show you a real track record, not only the calls that worked.
- **The app that holds your notes and tasks** – not to read them, sell them or shut down.
- **The platform that pays builders** – to pass the money on.
- **An agent you hire** – to be as good as it says it is.
- **Code you cannot read** – to do what its makers say, and nothing hidden.

Each of these can go wrong, and most of the time you would never know.

On TraderSwift, the aim is simple. Where something can be checked, you check it, instead of taking anyone's word for it.

## What can you check?

Each item below has its own chapter. Here is the short version.

### Can my agent break its limits?

You write down what your agent may trade, and every order is checked against those limits before it is signed. The agent cannot break them.

This helps you because a bot that is broken into can still trade only inside your limits. Signer never signs a transfer or a withdrawal.

[Chapter 09](09-how-does-an-order-get-signed-and-how-do-i-stop-it.html) explains how. **Live** on our own account since 14 Nov 2026.

### Would I know if someone tried to break in?

Every order request is recorded, signed or refused. A refused order is your alarm.

[Chapter 10](10-how-would-i-know-if-someone-tried-to-break-in.html) explains. **Live.**

### Can someone read what my agents say?

Your agents talk to each other about what to trade. If someone reads that, they read your plan.

The TraderSwift Bus will be an encrypted channel for agents, with a rule for who may write what.

[Chapter 12](12-how-do-agents-talk-to-each-other-safely.html) explains. **Planned**, with the first piece of code built.

### Can someone read my trade logs and files?

Your trade logs are your strategy written down. A leak could let someone copy it.

With Storage, your files are encrypted on your phone before they leave it. The providers who store them hold only a scrambled copy they cannot read.

[Chapter 13](13-where-do-my-trade-logs-notes-and-files-live.html) explains. **Built, not live.**

### Can I trust my data feed?

A charts data node makes a fingerprint of each day's market data. Anyone can run the same open-source node, compare fingerprints, and see whether two nodes agree.

This helps you because a feed that changes its history can be caught.

[Chapter 14](14-how-can-i-check-market-data.html) explains. **Built, not live** for you to read: our node serves candles, but behind a login.

### Is a signal seller's track record real?

Many people say they offer good signals. Few can show it.

Here, each signal gets a fingerprint and a time when it is published, before the outcome is known. A provider builds a track record, not a claim.

The fingerprint says nothing about who received the signal.

[Chapter 15](15-how-does-a-signal-provider-build-a-track-record.html) explains. **Built, not live.**

### Who can read my notes and tasks?

Ledger keeps your tasks and decisions. Vault keeps your notes and files.

Both are encrypted on your phone, and you decide who else may read them. No company holds them for you.

[Chapter 16](16-what-are-ledger-and-vault.html) explains. **Built, not live.**

### Does the money reach the builder?

When you pay for a builder's app, the money goes straight to the builder.

This helps builders because nobody sits between them and their pay.

[Chapter 20](20-what-is-the-marketplace-and-how-do-builders-get-paid.html) explains. **Built, not live.**

### Is an agent I hire any good?

Signer creates a verification layer for our agentic review system, used in our planned marketplace.

A review of an agent can rest on what it actually did, not on what it claims.

[Chapter 21](21-how-does-an-agent-prove-it-is-any-good.html) explains. **Planned.**

### What does the code really do?

The code is open source. You can read it, or have your own AI agent read it for you.

Signer, the hub chain and Signals Desk are public on GitHub today. [Chapter 03](03-why-is-traderswift-open-source.html) explains why that matters.

## Why does this matter?

A promise costs nothing. A record you can check is worth more.

When the record can be checked, a good agent, a good signal provider or an honest data node can prove it. That is the reward for doing honest work, and it is what makes TraderSwift unique.

## Is all of it live?

Not yet.

Signer and the hub are live today. The rest is being built, and [chapter 26](26-what-is-running-today-and-what-is-coming.html) says exactly where each part stands.

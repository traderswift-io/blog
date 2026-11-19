---
title: What does security mean for a trading agent?
description: Security is more than the key. The channel your agents talk on and your trade logs need protecting too.
order: 5
part: Security, which is more than the key
---

Most talk about trading security is about one thing: the key.

The key matters, because whoever has it can trade your account. But it is not the only thing a trader can lose.

## What must be secure?

Three things, first of all.

- **The key** – it lets an agent place orders on your account.
- **The communication channel** – it is where your agents talk to each other, and to you, about what to trade.
- **The trade logs** – they are the record of every order, every fill and every reason.

After those come your signals, your notes and your files. They hold your research, your entries and your plans.

## Why do trade logs matter so much?

Your trade logs are your strategy, written down.

Even a leak of your trade logs could let someone reverse-engineer your strategy. Once they know when you buy, when you sell and why, they can trade ahead of you, or against you.

## Why does the channel matter?

Agents talk to each other all day: what to watch, what to buy, when to stop.

Someone who can read that channel can read your plan before you act on it. Someone who can write to that channel can tell your agents what to do.

## What leaks, and what covers it?

Here is each risk, and the TraderSwift part that covers it.

| What leaks | What an attacker gains | Which part covers it | Status |
| :--- | :--- | :--- | :--- |
| The key | Control of your account | [Signer](08-how-does-signer-hold-a-key.html) | **Live** on our own account since 14 Nov 2026. For your own account, **Built, not live**, target Sat 21 Nov 2026 |
| The channel your agents talk on | Your plan, and a way to give your agents orders | [The TraderSwift Bus](12-how-do-agents-talk-to-each-other-safely.html) | **Planned**, first piece of code built |
| Your trade logs | Your strategy, and a way to trade against it | [Storage](13-where-do-my-trade-logs-notes-and-files-live.html) | **Built, not live**. Test passed 18 Nov 2026 |
| Your signals | Your edge, before the market moves | [Signals](15-how-does-a-signal-provider-build-a-track-record.html) | **Built, not live** |
| Your notes and files | Your research and your plans | [Ledger and Vault](16-what-are-ledger-and-vault.html) | **Built, not live** |

The chapters that follow start with the key, because a leaked key is the fastest way to lose money.

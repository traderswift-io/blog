---
title: How are trading keys held today, and what goes wrong?
description: Where a bot's key usually lives, the ways it leaks, and a live example.
order: 5
---

Before we explain Signer, it helps to see how trading keys are usually held today.

## Where does a bot's key live?

A trading bot needs a key to sign its orders at the exchange.

Usually it holds that key whole, in one of these places:

- **An environment variable** or a config file on the machine that runs the bot.
- **A secrets store** that the bot reads when it starts, and then keeps in memory.
- **A file the agent itself can read and write**, sometimes by accident.

Wherever it sits, the bot can read the whole key. So can anything that takes control of the bot.

## What can go wrong?

**The machine is broken into.** Whoever gets in can read the key.

**Prompt injection.** An AI agent reads text from web pages, messages and documents. Text written to trick it can tell it to reveal or misuse anything it can reach. If the agent can read the key, the key is at risk.

**The key ends up in the agent's notes.** Many agents keep their memory in Markdown files, a vault of notes they read and write. A key can be copied into those notes, and notes get synced, shared and sometimes published.

**It leaks through logs or code.** A key printed in a log, or committed to a repository, is a key someone else can find.

**One key can do everything.** Many exchange keys can trade, and some can also move funds. When the key leaks, everything it allows is open.

There is more than this. A full guide on each risk is planned, and this chapter will link to it.

## What does a leak look like?

On 16 November 2026, a leaked trading key let an attacker take about $10.4 million from a trader's accounts on Lighter, a perpetuals exchange, and try for $5.1 million more.

The key did exactly what it was allowed to do.

Our case study walks through it step by step: [Defined Trading Policy – What the Lighter API-Key Drain Shows](../lighter-api-key-drain/index.html).

The next chapter shows how Signer holds a key instead.

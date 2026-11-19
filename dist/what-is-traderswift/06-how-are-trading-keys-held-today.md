---
title: How are trading keys held today?
description: Where a trading bot's key usually lives, and the main problem with keeping it there.
order: 6
part: Security, which is more than the key
---

Before we explain Signer, it helps to see how trading keys are usually held today.

## Why does a bot need a key?

A trading bot needs a key to sign its orders at the exchange.

The signature tells the exchange the order really came from you. Without it, the order is refused.

## Where does the key live?

Usually the bot holds that key whole, in one of these places:

- **An environment variable or a config file** – the key sits in plain text on the machine, so the bot can read it when it starts.
- **A secrets store** – the bot reads the key when it starts, and then keeps it in memory.
- **A file the agent itself can read and write** – an AI agent with access to the folder can open the key, sometimes by accident.

Each of these is common, and each one is easy to set up.

## What is the main problem?

Wherever the key sits, the bot can read all of it. So anything that takes control of the bot also takes control of the key.

That could be a person who breaks into the machine. It could be a bug, or a piece of text that tricks an AI agent.

## Is that the only problem?

No. There is a lot more.

[The next chapter](07-what-goes-wrong-with-keys-today.html) goes through each way a key can leak, with a real example from November 2026.

---
title: What goes wrong with keys today?
description: Each common way a trading key leaks, one at a time, ending with a real example.
order: 7
part: Security, which is more than the key
---

There are many ways a trading key can leak.

Here they are, one at a time.

## How do environment variables leak a key?

Many bots keep their key in an environment variable: a named setting the machine passes to every program it starts.

It is easy, and it is everywhere. But any program running as the same user can often read it, and it can turn up in crash reports and debug output.

## How does prompt injection reach a key?

An AI agent reads text from web pages, messages and documents. Text written to trick it can tell it to reveal or misuse anything it can reach.

This is called prompt injection. If the agent can read the key, the key is at risk.

## How does a key end up in an agent's notes?

Many agents keep their memory in Markdown files: a vault of notes they read and write. Ours do too.

A key can be copied into those notes by mistake. Notes get synced, shared and sometimes published.

## How do logs leak a key?

Programs write logs to show what they did. When an order fails, a bot often logs the whole request, and the key can go with it.

A key printed in a log, even once, is a key someone else can find. Logs are often kept for a long time and read by many people.

## What happens when a key is committed with the code?

A key saved in a code file can be committed to a repository by mistake.

Once it is pushed, deleting the file later does not help. The key stays in the history.

## What if someone breaks into the machine?

Whoever gets into the machine that runs the bot can read anything the bot can read. That includes the key.

Once they have copied it, they don't even need to stay on your machine to use it.

## Why is one key that can do everything a risk?

Many exchange keys can trade, and some can also move funds.

When a key like that leaks, everything it allows is open at once.

## Can the signing code leak the key by itself?

Yes, with no break-in at all.

Signing uses a number that must be used only once, called a nonce. If the code reuses it, the key can be worked out from the signatures.

## What does a leak look like?

On 16 November 2026, a leaked trading key let an attacker take about $10.4 million out of a trader's account on Lighter, a perpetuals exchange, and try for $5.1 million more.

The key did exactly what it was allowed to do.

Lighter's post-mortem says the key was exposed by signing code outside its official tools that reused nonces ([Lighter](https://x.com/Lighter_xyz/status/2122394446343946717)).

Our case study walks through it step by step: [What Would Written Limits on One Key Have Stopped at Lighter?](../lighter-api-key-drain/index.html)

[The next chapter](08-how-does-signer-hold-a-key.html) shows how Signer holds a key instead.

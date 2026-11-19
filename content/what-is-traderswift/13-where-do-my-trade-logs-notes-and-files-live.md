---
title: Where do my trade logs, notes and files live?
description: Your files are encrypted on your phone, and the people who store them can only see scrambled data.
order: 13
part: Security, which is more than the key
---

Your trade logs, notes and files are some of the most valuable things you own as a trader.

They hold your strategy, your research and your mistakes. As [chapter 05](05-what-does-security-mean-for-a-trading-agent.html) explains, even a leak of your trade logs could let someone work out your strategy.

## Where do they live today?

Usually on a company's servers: a cloud drive, a note app, or the logging service your bot writes to.

That company holds your data and can usually read it. [Chapter 17](17-why-not-just-use-the-tools-i-have-today.html) says what else that costs you.

## What does TraderSwift do instead?

Your files are encrypted on your phone, before they go anywhere.

Encrypted means locked with a key that only you hold. The locked, scrambled form is called ciphertext, and it looks like random noise to anyone without your key.

If you later choose to store a copy with someone else, they hold ciphertext and nothing else. They cannot read your logs, your notes or your files.

## What is Storage?

Storage is the part of TraderSwift where providers will hold that encrypted data for you.

It runs on its own chain, `storage-1`. The chain checks that each provider still holds what it promised to hold.

This helps you because a provider cannot lose your data without it showing. If it no longer holds your files, the chain can tell.

## How do I choose where my data goes?

By default, your data stays encrypted on your phone only, and nothing leaves the device.

Keeping a copy with TraderSwift Storage as well will be your choice. [Chapter 18](18-where-is-my-data-kept-and-who-can-read-it.html) explains the choices, and who you can share with.

## Where does it stand?

**Built, not live.** A full test round of the storage node passed on Wed 18 Nov 2026: data went in, and came back out intact.

Before it holds real data, it waits on two things:

- **Founding providers** – the first people who will store data on it.
- **An outside review** – of how it encrypts your data.

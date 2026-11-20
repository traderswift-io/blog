---
title: Why is TraderSwift open source?
description: If someone else's code manages your keys and your money, reading that code is the bare minimum.
order: 3
part: The whole picture
---

For me, open code is the bare minimum when someone else's code manages your money.

That code may hold your keys, place your trades and keep your records. You should be able to read it.

## Can I check it myself?

Yes. Today anyone can point their own AI agent at the code to audit it.

You don't need to be a programmer, or read every file yourself. Give this prompt to your own AI agent:

::: prompt
Read the repository at https://github.com/traderswift-io/signer. Tell me, in plain words, what the code does with a trading key. Check whether any code path could send a key, a key share or funds anywhere other than where the documentation says. List anything that looks unsafe, with the file and line. Do not run any of the code.
:::

You don't need to take our word for what the code does. Your agent can tell you.

## Am I tied to you?

No.

Anyone can fork the code, run it privately as their own network, or even compete with us.

## Does open code make it safer?

Usually, yes. Open source usually means more people harden the code, which helps everyone.

When more people read the code, more of its weak spots are found. Each fix makes the code stronger for everyone who runs it, including us.

## What if I want to build something of my own on it?

We support founders who want to build a part of the network themselves.

[Chapter 25](25-can-i-build-a-subnet-of-my-own.html) explains how a founder can build and run a chain of their own.

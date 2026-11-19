---
title: What is the TraderSwift Bus?
description: The channel our agents and machines will talk on, and why orders never use it.
order: 9
---

The TraderSwift Bus is the channel our agents and machines will use to talk to each other.

A trading agent's messages matter as much as its key. If someone can read or change them, they can learn or steer what the agent does.

## What is it designed to do?

- **Encrypted channels** between agents and machines.
- **A policy per channel**, setting who may write what.
- **Channels, threads and direct messages.**
- **An audit record** that is anchored, so it can be checked later.

It speaks Nostr, an open messaging standard, so Nostr tools can connect to it.

## What never travels on it?

Orders never go over the Bus.

That is a fixed rule: orders go only through Signer.

## Where does it stand?

The Bus is **Planned**.

The design is accepted, and the first piece of code is built and checked: the part that applies the write policy. It is not deployed.

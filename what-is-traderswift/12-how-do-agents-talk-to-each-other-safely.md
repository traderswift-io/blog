---
title: How do agents talk to each other safely?
description: The channel your agents talk on, and why it needs the same care as the key.
order: 12
part: Security, which is more than the key
---

Agents talk to each other all day.

One watches the market and another plans a trade. A third checks the plan, and a person may join in.

All of that talk runs over some channel. Today that is often a chat app or a shared server.

## Why does the channel need protecting?

Protecting the key is not enough if someone can take over the messages your research agent sends to your trading agent.

Whoever can read the channel can read your plan before you act on it. Whoever can write to it can tell your agents what to do.

A leaked key loses you an account. A leaked channel can lose you your edge, every day, without you knowing.

## What will the TraderSwift Bus be?

The TraderSwift Bus will be the channel for agents and the machines they run on.

It is designed to give you:

- **Encrypted channels** – only the agents and people in a channel will be able to read it.
- **A rule for each channel** – each message will go out under a written rule for who may write what, and where.
- **Channels, threads and direct messages** – the way people already work in chat apps.
- **An audit record** – a record of what was said, with its fingerprint fixed on a chain, so it cannot be changed later.

The rule for each channel helps you because a taken-over agent will not be able to send messages it was never meant to send.

## Will it work with tools I already have?

It is designed to.

The Bus will use Nostr to carry its messages. Nostr is an open way of sending signed messages through servers that pass them along, and many apps already use it.

So Nostr apps will be able to connect to the Bus.

## Will orders travel on the Bus?

No, never.

Orders go only through Signer, under your limits. The Bus will carry talk, not trades.

That rule is fixed. Even a channel that is broken into will not be able to place an order.

## Where does it stand?

**Planned**, with the first piece of code built.

The design is accepted. The first piece, the part that will check each message against the channel's rule, is built and checked.

Encrypted channels, threads, direct messages and the audit record are designed, not built. Nothing is running yet.

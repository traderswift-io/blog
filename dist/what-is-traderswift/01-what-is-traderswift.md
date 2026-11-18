---
title: What is TraderSwift?
description: What a trading agent needs, and the open-source parts TraderSwift provides for it.
order: 1
---

TraderSwift is a blockchain infrastructure layer for agentic and hybrid trading.

Agentic means software agents place the trades.

Hybrid means a person and an agent trade together.

Either way, the agent needs the same things.

## What does a trading agent need?

At the top level, it needs three things.

- **Security.** A way to place orders without holding the key to the account, and limits it cannot break.
- **Data.** Market data it can check, not just take on trust.
- **Tools.** Ways to pay and get paid, to keep its notes and files, and to show a record of what it did.

TraderSwift provides each of these as open-source parts.

## Which part does what?

- **Security is Signer.** It signs orders for an agent without the agent ever holding the key. It is live today.
- **Data is the charts data node.** It serves market candles and publishes a daily hash that anyone can check. It is live today.
- **Tools are payments, Ledger, Vault, Storage and the marketplace.** These are being built.

Each part is explained in its own chapter of this update.

## Can I build on it, or run my own?

Yes, both.

Anyone can read the code, take part in the network, or build on top of it.

You can also fork the code and run your own private network, without connecting to us.

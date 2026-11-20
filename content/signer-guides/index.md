---
title: Signer – How to Run, Test and Trade with It
description: Twelve how-tos for people interested in Signer, each with steps and prompts for your own agent. Some are planned, and say so.
kind: guide
order: 1
---

Signer lets a trading agent place orders without ever holding the key to the account.

The key is cut into pieces, and each piece sits on a different machine.

To sign an order, most of those machines must agree. Before they do, each one checks the order against limits the owner writes down.

Those limits are called a policy. We explain each of these words as we go.

Signer is open source. You can launch your own Signer chain, on its own, without connecting to us.

::: notice
**Signer is live on Hyperliquid today, trading TraderSwift's own test account.**

These are our target dates. If a date slips, this box changes the same day, with the new date and the reason.

- **Rotation of the signers**, with Policy v2: target Saturday 21 November 2026. Waits on the seal of the four new machines, and on the sitting that runs the rotation.
- **Aster**: no date yet. Waits on its test account being funded, then a sitting after that.
- **Base (Avantis)**: no date yet. Waits on its code passing its checks, on confirming the venue's minimum order size, and on funding.
- **Your own Hyperliquid account**: no earlier than Sunday 22 November 2026. You sign the setup in your own wallet, and we never see or hold your keys.

Your own account waits on three things:

- the rotation;
- a live test on a second account;
- our decision on the security audit.

From the rotation, target Saturday 21 November 2026, your trading account address and your orders never appear on `signer-1` in readable form. The chain shows only that your policy exists, its markets, size limits and expiry, and when each request was signed or refused.

Our own test account is public by choice.

Follow the planned venues on [GitHub](https://github.com/traderswift-io/signer/issues?q=is%3Aissue+label%3Avenue).
:::

These pages show you how to use it. You can run a validator, run your own chain, and learn every part of it today.

Every page has steps you can follow and a prompt you can give your own AI agent.

Pages marked **Planned** describe work that isn't finished yet. Each says what exists today, what we plan, and the milestones.

When the work is done, the page is updated.

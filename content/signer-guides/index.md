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

::: notice
**Signer is live on Hyperliquid today, trading TraderSwift's own account.**

These are our target dates, each with what it waits on. If a step slips, this box changes the same day, with the new date and the reason.

- **Next rotation of the signers**, with the next version of the policy: target Friday 20 November 2026. Waits on the new build passing its second review and its tests, then a live test on a small real account.
- **Aster**: target Friday 20 November 2026, in the same session. Waits on a new key from the signers, approved and funded on Aster, and a live test.
- **Base (Avantis)**: target Friday 20 November 2026, in the same session. Waits on a new key from the signers, approved on Avantis, and a live test.
- **Your own Hyperliquid account**: target Saturday 21 November 2026. Waits on the rotation, a final security decision, then a live test done the way a new user would do it. You sign the setup in your own wallet; we never see or hold your keys.

Follow the planned venues on [GitHub](https://github.com/traderswift-io/signer/issues?q=is%3Aissue+label%3Avenue).
:::

Signer is open source. You can launch your own Signer chain, on its own, without connecting to us.

These pages show you how. You can run a validator, run your own chain, and learn every part of it today.

Every page has steps you can follow and a prompt you can give your own AI agent.

Pages marked **Planned** describe work that isn't finished yet. Each says what exists today, what we plan, and the milestones.

When the work is done, the page is updated.

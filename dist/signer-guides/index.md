---
title: Signer – How to Run, Test and Trade with It
description: Twelve how-tos for people interested in Signer, each with steps and prompts for your own agent. Some are planned, and say so.
kind: guide
---

Signer lets a trading agent place orders without ever holding the key to the account.

The key is cut into pieces, and each piece sits on a different machine.

To sign an order, most of those machines must agree. Before they do, each one checks the order against limits the owner writes down.

Those limits are called a policy. We explain each of these words as we go.

Signer is open source. You can launch your own Signer chain, on its own, without connecting to us.

::: notice
**Signer is live on Hyperliquid today, trading TraderSwift's own test account.**

These are our target dates. If a date slips, this box changes the same day, with the new date and the reason.

- **Rotation of the signers**, with Policy v2: target Friday 20 November 2026. Waits on the new build passing its review and its tests, then a live test on a small real account.
- **Aster**: target Friday 20 November 2026, in the same session. Waits on a new key from the signers, approved and funded on Aster, and a live test.
- **Base (Avantis)**: target Friday 20 November 2026, in the same session. Waits on a new key from the signers, approved on Avantis, and a live test.
- **Your own Hyperliquid account**: target Saturday 21 November 2026. You sign the setup in your own wallet, and we never see or hold your keys.

Your own account on Saturday 21 November waits on four things:

- the rotation of Friday 20 November;
- the release that keeps your account private;
- our decision on the security audit;
- a live test done the way a new user would do it.

From Saturday 21 November, your trading account address and your orders never appear on `signer-1` in readable form. The chain shows only that your policy exists, its markets, size limits and expiry, and when each request was signed or refused.

Our own test account is public by choice.

Follow the planned venues on [GitHub](https://github.com/traderswift-io/signer/issues?q=is%3Aissue+label%3Avenue).
:::

These pages show you how to use it. You can run a validator, run your own chain, and learn every part of it today.

Every page has steps you can follow and a prompt you can give your own AI agent.

Pages marked **Planned** describe work that isn't finished yet. Each says what exists today, what we plan, and the milestones.

When the work is done, the page is updated.


## Chapters

1. [What is Signer, and who is it for?](01-what-is-signer.md)
2. [How does an order get signed?](02-how-does-an-order-get-signed.md)
3. [How do I try Signer on my own computer?](03-how-do-i-try-signer-on-my-own-computer.md)
4. [How do I write a trading policy?](04-how-do-i-write-a-trading-policy.md)
5. [How do I stop an agent fast?](05-how-do-i-stop-an-agent-fast.md)
6. [How do I read Signer's record?](06-how-do-i-read-signers-record.md)
7. [How do I run a Signer validator?](07-how-do-i-run-a-signer-validator.md)
8. [How do I launch a node with one link?](08-how-do-i-launch-a-node-with-one-link.md)
9. [How do I run my own Signer chain?](09-how-do-i-run-my-own-signer-chain.md)
10. [How do I get a Signer key for my own account?](10-how-do-i-get-a-signer-key-for-my-own-account.md)
11. [How do I hold my own key shares?](11-how-do-i-hold-my-own-key-shares.md)
12. [How do I run a private Signer network on ESP32s?](12-how-do-i-run-a-private-signer-network-on-esp32s.md)

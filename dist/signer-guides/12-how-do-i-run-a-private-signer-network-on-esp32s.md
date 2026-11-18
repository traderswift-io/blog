---
title: How do I run a private Signer network on ESP32s?
description: A household quorum: ESP32s approve each order, two Raspberry Pis hold the shares. Planned.
order: 12
---

**Planned.**

This page is half written on purpose. The first half explains the design and what each device does.

The second half is the milestones, starting with a bench test. When the bench passes, this page will be updated with the full build.

Once it is built, you will be able to run a small Signer network in your own home, where nothing signs for you unless your own devices agree.

## What is a household quorum?

A few cheap devices in your home that must agree before your trading key signs. We call it a household quorum.

Each device has a different job:

- **Two Raspberry Pis hold the shares.** They hold two of the three shares of your key, and together they can sign.
- **Three ESP32s approve.** Each one checks the exact order, then approves it with its own device key. It does not hold a share of your trading key.
- **The network holds one share.** On its own it can never sign. It is your backup.

## Why can't an ESP32 hold a share?

Because of the kind of key exchanges need. Hyperliquid uses the same signature type as Ethereum.

Splitting that kind of key takes heavy maths in every signing round, which a Pi can do and an ESP32 can't do in reasonable time.

So the ESP32s approve and the Pis sign. Each Pi refuses to take part in signing unless two of the three ESP32s have approved that exact order.

## Does it remove trust in the network?

Yes, in this form. The network holds one share and it takes two to sign, so the network can never sign alone.

Your approvals are checked by your own Pis, not by us.

That only holds because the shares are on your machines. If the network held the shares and your devices only approved, it would protect you against a stolen agent key, but you would still be trusting the network.

## Does it need the devices to be near each other?

They talk over Bluetooth, but Bluetooth can be relayed, so it doesn't prove distance.

What the design checks is that the devices taking part have recently heard each other, with authentication. We make no claim about where they are.

If a device stops hearing the others, it suspends itself. It takes two of your enrolled devices to bring it back.

## What can I do now?

If you have the parts, you can start on the device side.

Every device should show the exact order it approves, and never sign blind.

::: prompt
I want to build an order approver on an ESP32. It should make its own signing key on the device with flash encryption on, show the order it is asked to approve, wait for a button press, then sign the order digest. List the ESP32 settings I need (secure boot, flash encryption, where the key is stored), the libraries to use for secp256k1 signing, and how to show the order on a small screen. Don't write any network code yet.
:::

## What are the milestones?

1. **Two Pis sign together.** Timed over Bluetooth and over the network, 100 runs each.
2. **The household check.** Each Pi refuses to sign without two of three ESP32 approvals of the exact order.
3. **The relay test.** Prove what Bluetooth can and can't show.
4. **Freshness.** A spec for trusted time and when trust expires.
5. **Recovery.** A spec for travel, a lost device and total loss.
6. **Real use.** Only after the steps above, with a throwaway key first.

Bigger groups, such as 8 of 13 or 13 of 21, come later, once we can show the devices fail independently.

## Final thoughts

A household quorum puts the final say on your trades in your own home, on hardware that costs very little.

The design is set: ESP32s approve, Pis sign, and the network is the backup.

The bench comes first. When it passes, this page gets the full build.

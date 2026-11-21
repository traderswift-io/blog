---
title: What is running today, and what is coming?
description: Every part of TraderSwift, what state it is in, and the date or the step each one waits on.
order: 26
part: The network, and where it stands
---

This page is the honest list of what runs today, and what does not yet.

We update this page as we bring each part live. Checking a part's status here before you connect anything shows you what works now, and what is still waiting.

::: notice
Last checked: Thu 19 Nov 2026.

Every future date below is a target, and each one waits on its final checks.
:::

## What do the status words mean?

We use three words, the same way on every page:

- **Live** – running for real.
- **Built, not live** – the code exists and passed its checks, but it is not serving anyone yet.
- **Planned** – a design or an intention. Nothing is running.

Where we have a date, we give it. Where we do not, we say what the part waits on.

## Signer

The table below shows the status of Signer and its planned limits.

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| Signer on Hyperliquid, for TraderSwift's own account | **Live** | Since Sat 14 Nov 2026; pauses today, Sat 21 Nov, for the signer rotation. This test account is public by choice |
| Stopping an agent with one signed message | **Live** | Since Sat 14 Nov 2026 |
| Signer on Aster | **Built, not live** | [Proof run](https://github.com/traderswift-io/signer/blob/main/docs/ASTER_PROOF.md) on Sat 21 Nov 2026 through Signer on a test account: orders filled, closed and cancelled, and one order over the cap refused. Waits on the new signer set and a standing policy |
| Signer on Base, through Avantis | **Built, not live** | No date yet |
| New limits: a price band, a cap on how often orders go out, and caps on order value | **Built, not live** | Switches on after the signer rotation, no date set |
| A cap on leverage | **Built, not live** | Switches on by itself at a set block, about Thu 26 Nov 2026 |
| Signer for your own Hyperliquid account | **Built, not live** | No earlier than Sun 22 Nov 2026 |
| Your markets and limits kept private, the same way as your account and orders | **Planned** | The next release |
| Holding your own key shares, and a private network on devices at home | **Planned** | |
| Starting a node from one link | **Planned** | |

Signer for your own account waits on three steps:

- the rotation, built and tested and waiting on one signing moment with no date set, when a new set of signers takes over and privacy for user accounts comes with it, so your trading account address and your orders never appear on the chain in readable form;
- a live test on a second account;
- our decision on an outside audit.

[Chapter 11](11-what-can-other-people-see-on-the-chain.html) explains what the chain shows, and what it never shows.

## The network

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| The hub, `traderswift-1` | **Live** | Since 14 Nov 2026 |
| The hub's admin held by a multisig, so several keys must agree | **Live** | Since 18 Nov 2026 |
| The first subnet charters on the hub | **Planned** | No date. Waits on one security review, then final approval |
| Subnets started by founders | **Planned** | The hub does not yet take charters from other teams |

## Data and signals

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| Our charts data node | **Built, not live** | Serves candles, but its public address is still behind a login |
| The public node, for anyone to run and compare | **Live** | Open source; a fresh node matched our 16 Nov 2026 fingerprint |
| Daily fingerprints posted to the hub | **Built, not live** | Waits on the market data charter and our node's registration |
| Paying for data per request | **Built, not live** | Not run live |
| Fingerprinting signals | **Built, not live** | No real signal published with it yet |
| The private Signals chain | **Planned** | |
| Signals Desk, our fork of an open-source trading desk | **Live** | Public since 15 Nov 2026; placed live orders through Signer on 17 Nov 2026 |
| Pathiel, our fork of a second open-source desk | **Built, not live** | Public since 16 Nov 2026 |

## Your own tools

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| Ledger and Vault chains, `ledger-1` and `vault-1` | **Live** | Since Thu 19 Nov 2026. Nothing writes to them yet |
| The encrypted store on your phone, and the choice screen | **Built, not live** | Merged 18 Nov 2026; not yet used on a real phone |
| Recovery after a lost phone | **Planned** | A printed recovery code and a spare device. Until it is built, losing the phone loses the saved items |
| Phone + Base, and Phone + TraderSwift Storage | **Planned** | Shown as "Coming soon" on the choice screen |
| Storage, `storage-1` | **Built, not live** | Test round passed 18 Nov 2026; waits on first providers and an outside review of its encryption |
| The TraderSwift Bus | **Planned** | The first piece of code is built |

## Solve, our wallet, and sign-in

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| The passkey unlocking the payment key, with no seed words | **Built, not live** | |
| Our own sign-in gate | **Built, not live** | |
| The device ring, and its recovery times | **Planned** | Design accepted 16 Nov 2026 |

## Marketplace, AI and compute

| Part | Status | Date, or what it waits on |
| :--- | :--- | :--- |
| The marketplace and payments per use | **Built, not live** | No listing live; no real payment made; live use waits on the last pieces |
| Reviews of agents, backed by Signer's record | **Planned** | |
| TraderSwift AI | **Planned** | What it does at launch is not decided |
| Compute for the AI | **Planned** | Starts on our own machines beside our nodes |

## Has anyone outside checked the security?

Not yet. [Chapter 27](27-why-shouldnt-i-use-traderswift-yet.html) says what that means for you.

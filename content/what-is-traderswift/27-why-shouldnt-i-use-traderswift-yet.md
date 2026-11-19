---
title: Why shouldn't I use TraderSwift yet?
description: The honest reasons to wait, and who should wait for what.
order: 27
part: The network, and where it stands
---

TraderSwift is early, and you should know exactly how early.

These are the reasons to wait.

## How long has it been running?

Signer has signed live orders since 14 Nov 2026.

That is days, not years. A system that handles money earns trust over time, and ours has not had that time yet.

## Has anyone outside reviewed the security?

No.

No outside security review has been done or booked yet. We have had internal reviews only.

If you need an outside review before you trust code with money, wait for one.

## Which venues are live?

Today Signer is **Live** on Hyperliquid only, and only for TraderSwift's own account.

Signer for your own Hyperliquid account has a target date of Sat 21 Nov 2026. Aster has a target of Fri 20 Nov 2026, and Base has no date yet.

If you trade elsewhere, there is nothing for you to connect yet.

## Are the other tools live?

Ledger, Vault, Storage, the marketplace and the wallet are **Built, not live**.

The Bus, TraderSwift AI, its compute and founder subnets are **Planned**. [Chapter 26](26-what-is-running-today-and-what-is-coming.html) lists every part with its status.

## What does the chain show about me?

Your trading account address and the contents of your orders never appear on the chain in readable form.

The chain does show that your policy exists, with its markets, size limits and expiry, and when each request was signed or refused. That is how anyone can confirm the rules were followed.

In the next release, your markets and limits are kept private the same way. [Chapter 11](11-what-can-other-people-see-on-the-chain.html) explains all of it.

If you want nothing about your trading on a shared chain, you don't have to use ours. Signer can run as your own private chain, with your own signers, as [How do I run my own Signer chain?](../signer-guides/09-how-do-i-run-my-own-signer-chain.html) shows.

## What if I lose my phone?

Recovery after a lost phone is not built yet.

Until it is, losing your phone loses what you saved in Ledger and Vault.

## Has a real payment gone through?

No.

The marketplace and its payments are built, and checked against test cases. No real payment has gone through yet.

## So who should wait?

- **If you need audited code** – wait for an outside review.
- **If you trade on another venue** – wait for that venue's date.
- **If you cannot afford to lose your notes** – wait for recovery.
- **If you want to sell a front end** – wait for the first live listing.

## Who can start now?

- **If you build** – read the code, run Signer on your own computer, and point your own agent at it.
- **If you want to check data** – run the public charts node and compare its fingerprints with ours. [Chapter 14](14-how-can-i-check-market-data.html) shows how.
- **If you just want to see it work** – read the [Signer how-tos](../signer-guides/index.html).

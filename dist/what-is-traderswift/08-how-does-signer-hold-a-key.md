---
title: How does Signer hold a key?
description: Where the key comes from, how it is split into pieces, and where those pieces sit.
order: 8
part: Security, which is more than the key
---

Signer lets an agent trade from a key it never holds.

This chapter shows where that key comes from, and where it sits.

## Where does the key come from?

There are two ways. Signer can take a key you already have, or it can make a new one for you.

## How is the key split?

Either way, the key ends up in pieces, called shares. Each share sits on a different machine, called a signer.

No single share can sign anything. A share on its own is useless to a thief.

## Does the whole key ever exist?

A key Signer makes never exists whole. It is made in pieces from the start, so nobody holds the whole key, not even us.

A key you bring existed whole once, before it was split. After that, it lives only as shares.

If you can, let Signer make a new key. Then there is no moment when the whole key sits on one machine.

## How many shares are there?

Today there are four shares, on four signers. Any three of them can sign together, and two are not enough.

So one signer can be down, or broken into, and your orders still get signed safely.

At launch on 14 November 2026 there were three signers, and any two could sign.

On 17 November we moved to four new signers on new machines, and they made a new key together. The old key was never moved, and trading did not stop.

The [rotation update](../trading-key-rotation/index.html) explains how.

## Is it running?

Signer has signed live orders on Hyperliquid since 14 November 2026, on our own account with real money. **Live.**

For your own Hyperliquid account, it is **Built, not live**. The target is Sat 21 Nov 2026, and it waits on four things:

- the change of signers on Fri 20 Nov 2026;
- account privacy for user accounts, which [chapter 11](11-what-can-other-people-see-on-the-chain.html) explains;
- a decision on a security audit;
- a live test with a new user.

Aster, and Base through Avantis, are **Built, not live**, with a target of Fri 20 Nov 2026.

Holding your own key shares, on a few cheap devices at home, is **Planned**. It has no date yet.

If you want to check how splitting a key works, our cryptography chapter on [which threshold really applies](../cryptography/08-shamir-which-threshold-really-applies.html) walks through it with worked code.

[The next chapter](09-how-does-an-order-get-signed-and-how-do-i-stop-it.html) shows how an order gets signed, and how you stop it.

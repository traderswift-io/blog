---
title: How do I sign in without a seed phrase?
description: The TraderSwift wallet uses the passkey on your phone, not a list of words you must write down and hide.
order: 19
part: Tools for a person
---

Most crypto wallets start by handing you twelve or twenty-four words.

That list is called a seed phrase. You are told to write it down, hide it and never lose it.

Anyone who finds it owns your money. If you lose it, the money may be gone for good.

The TraderSwift wallet has no seed phrase.

## What is a passkey?

A passkey is a sign-in your phone or computer already knows how to make.

You unlock it with your face, your fingerprint or your screen lock. Its secret stays on your device.

## What does the passkey do in the wallet?

It unlocks the wallet's payment key.

That is the key that approves payments, such as paying a builder for a front end. [Chapter 20](20-what-is-the-marketplace-and-how-do-builders-get-paid.html) explains payments.

There are no seed words to write down, and none to steal.

Your passkey also gives Ledger and Vault their own encryption key, kept separate from the payment key. [Chapter 18](18-where-is-my-data-kept-and-who-can-read-it.html) explains it.

## Is that the same as signing in to an account?

Not yet.

Today the passkey unlocks the payment key. Signing in to TraderSwift apps is a separate step, done by the sign-in gate further down this page.

## What is it like to use?

You are inside the wallet before any setup.

Looking around needs nothing. A key is made only at the first action that needs one.

One wallet works across many chains. Addresses stay out of the way unless you ask to see them.

## Can a nice-looking skin trick me?

No.

The wallet is one shared core with skins on top. A skin is the look: colours, layout and style.

The core owns every approval screen and the text you approve. So a skin can change how the wallet looks, but never what you are agreeing to.

We have three skins today: Glass, Orbit and Night Key.

## What if I lose my device?

Our plan for that is called the device ring.

Your account would be owned by your own devices, any two of three. One phone alone is never enough.

If you lose everything, recovery would take seven days by default, and never less than three.

During that time, any of your enrolled devices could cancel it. So if a thief started a recovery, you would see it, and stop it.

The device ring is a design, accepted on 16 Nov 2026. Its screens are not built yet.

## How do I sign in to TraderSwift apps?

We built our own sign-in gate, so that we decide who gets in, not a third party.

You sign in with a passkey or with a wallet. The gate checks each signed session, and each app still checks every request on its own.

The story of why is in [Why did we build our own sign-in?](../since-lockbox/06-why-did-we-build-our-own-sign-in.html), in Since Lockbox.

## What is live?

- **Built, not live** – the passkey unlocking the payment key, with no seed words.
- **Built, not live** – the sign-in gate.
- **Planned** – the device ring and its recovery times.

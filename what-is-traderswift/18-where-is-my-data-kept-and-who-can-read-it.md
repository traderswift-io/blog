---
title: Where is my data kept, and who can read it?
description: Your choices for where your data lives, how you let an app or an agent read it, and what happens if you lose your phone.
order: 18
part: Tools for a person
---

You decide where your data is kept.

By default, it stays on your phone, encrypted, and nothing leaves the device.

## What does encrypted mean here?

Encrypted means scrambled with a key, so that it reads as noise to anyone without that key. Your data is encrypted on your phone before it is saved.

The key comes from your passkey, the sign-in your phone already uses. [Chapter 19](19-how-do-i-sign-in-without-a-seed-phrase.html) explains passkeys.

That key is separate from the one Solve, your wallet, uses for payments. So approving a payment and opening your notes never rely on the same key.

## What are my choices?

The table below shows the three storage options on the choice screen.

| Choice | What it means | Status |
| :--- | :--- | :--- |
| Encrypted on my phone only | The default. Nothing leaves the device | **Built, not live** |
| Phone + Base | A copy kept with the help of Base, a public blockchain | **Planned** |
| Phone + TraderSwift Storage | A scrambled copy held by storage providers, who cannot read it | **Planned** |

On the choice screen, the two later choices are shown greyed out until they are built.

Phone + TraderSwift Storage waits on Storage's first providers, and on an outside review of its encryption. [Chapter 13](13-where-do-my-trade-logs-notes-and-files-live.html) explains Storage.

Phone + Base still needs its design. Anything written to Base stays there for good, in public, and every piece costs a fee, so we will not simply copy your files onto it.

## How do I let an app or an agent read my data?

You give it a grant.

A grant names who may read, and which part of your data they may read. That part is called a scope.

For example, you could let one agent read your trading notes, and not your personal tasks.

The chain records the grant. The key that opens that scope is wrapped up and kept with your data, never on the chain.

## Can anyone see which apps I use?

No.

The chain does not keep the name of the app or agent you share with. It keeps a scrambled value, made from that name mixed with a random value.

With the random value, you can prove the grant exists. Without it, the scrambled value says nothing.

This is called a salted commitment. It means nobody can read the chain and list the apps and agents you use.

## Can anyone see when I am busy?

No, not from the chain.

If you choose, a short fingerprint of your encrypted data can go on the chain, at most once a day. It proves your data has not been changed behind your back.

The chain takes one fingerprint per person per day, so it does not show when in the day you were editing. Padding and batching those sends is **Planned**.

## What if I lose my phone?

Today, losing your phone loses the items saved on it, because recovery is not built yet.

The design is a printed recovery code plus a spare device. Nothing is held by us.

Until recovery is built, do not keep anything in the phone store that you cannot afford to lose.

## What is live?

- **Built, not live** – the encrypted store on your phone, and the choice screen. Both were merged on Wed 18 Nov 2026, and neither has been used on a real phone yet.
- **Built, not live** – grants and daily fingerprints, part of the two chains in [chapter 16](16-what-are-ledger-and-vault.html) that run since Thu 19 Nov 2026. Nothing writes daily fingerprints yet; the first writer, on the ledger chain, has a target of Mon 23 Nov 2026.
- **Planned** – Phone + Base, and Phone + TraderSwift Storage.
- **Planned** – recovery by printed code and spare device.

---
title: How do I hold my own key shares?
description: Any two of three pieces of your key can sign: two on your own machines, one on the network, so the network alone never can. Planned.
order: 11
---

**Planned.**

This page is half written on purpose. The first half explains the design and why it matters.

The second half is the milestones. When it is built, this page will be updated with the full steps.

Once it is built, you will be able to keep most of your own trading key on your own machines, so the network can never sign for you on its own.

## Why hold your own shares?

With Signer today, the network's signers hold every share, every piece, of a key. They check your policy before signing, and every decision goes on the chain.

But you are still trusting them not to work together against you.

Holding your own shares removes that trust.

## How does it work?

The key is split so that any two of three shares can sign. This is called 2-of-3.

- **Two shares on your machines.** For example, two small computers at home. Together they can sign without the network.
- **One share on the network.** On its own it can never sign. It is your backup if one of your machines is lost, and it is how your key joins the network.

This works because of one rule: the network must hold fewer shares than it takes to sign.

With any two of three, and one share on the network, it does.

## How is that different from approving on my phone?

There is a lighter option: your devices approve each order, while the network holds the shares.

That protects you against a stolen agent key, because nothing signs without your approval.

But it still trusts the network signers. If they worked together, they could sign without you.

Only shares on your own machines remove that trust.

## What will it ask of me?

- **Two machines you control.** They must be sealed before they take part in making the key: no remote login, not even for you.
- **A recovery plan.** What happens if you travel, lose a device, or lose everything. We write this down before anyone uses it with real money.

## What can I do now?

Think through your recovery before your machines. This prompt helps:

::: prompt
I plan to hold two of three shares of a trading key on two small computers at home, with the third share held by a network as a backup. Walk me through what happens if: I travel for a month, one computer dies, both die, or someone steals one. For each case, tell me whether I can still trade, whether I can recover, and what I should set up now.
:::

## What are the milestones?

1. **Recovery spec.** Travel, a lost device, total loss, and a malicious recovery attempt.
2. **Any two of three.** Two shares on your machines and one network share, so the network alone can never sign.
3. **Sealed or refused.** The signer software refuses to make a key unless your node is sealed.
4. **Your node, launched for you.** Your share node launched by the [one-link launcher](08-how-do-i-launch-a-node-with-one-link.html).
5. **A gated test.** With a throwaway key.
6. **First real account.** This page gets the full steps.

## Final thoughts

This is the version of Signer where the network can't sign for you at all.

It needs two machines of yours and a recovery plan you have thought through.

The design is set. The milestones above are what stands between it and your account.

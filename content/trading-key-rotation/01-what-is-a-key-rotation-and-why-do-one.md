---
title: What is a key rotation, and why do one?
description: What a rotation is, and the three reasons we did one.
order: 1
---

A rotation moves Signer's work to a new set of machines.

Signer keeps a trading key as shares on separate machines, called signers, and signs an order only if it fits the owner's written limits. [How does Signer hold a key?](../what-is-traderswift/08-how-does-signer-hold-a-key.html) explains it in full.

You rotate when the old machines should no longer be trusted with the key: they're being retired, their setup has a known weakness, or the set needs to grow.

Ours did all three.

Before, the launch set was three signers, any two of which could sign, plus a fourth machine that only ran the chain.

After, we wanted four machines that each run the chain and sign, any three of which can sign, prepared to a stricter standard.

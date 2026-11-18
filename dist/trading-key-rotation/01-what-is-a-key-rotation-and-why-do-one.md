---
title: What is a key rotation, and why do one?
description: What a rotation is, and the three reasons we did one.
order: 1
---

Signer keeps a trading key cut into pieces, called shares. Each share sits on a different machine, called a signer.

Enough of the signers must agree before an order is signed. Each one first checks the order against the owner's written limits, called a policy, which are kept on a public blockchain.

A rotation moves that job to a new set of machines.

You do one when the old machines should no longer be trusted with it: they're being retired, their setup has a known weakness, or the set needs to grow.

Ours did all three. The launch set was three signers, any two of which could sign, plus a fourth machine that only ran the chain.

We wanted four machines that each run the chain and sign, any three of which can sign, prepared to a stricter standard.

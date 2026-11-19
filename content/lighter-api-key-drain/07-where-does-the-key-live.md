---
title: Where does the key live?
description: How Signer makes a trading key, and who holds it.
order: 7
---

Nowhere, whole.

Signer's signers make each venue key together. Each one keeps only its own part of the key, called a share.

Nobody creates it, nobody stores it, and no third-party cloud holds a copy.

Every key on signer-1 was made that way except the launch key, including the one it trades with today. The Hyperliquid launch key was imported, because it was an agent the owner had already approved.

Since 17 November there are four signers, and any three must agree to sign.

Each one checks every request against the policy on the chain before it signs.

An attacker would need enough signers to agree, or a delegate key, and a delegate key only reaches as far as its policy.

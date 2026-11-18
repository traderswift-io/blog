---
title: What happened to Lockbox?
description: Halting and archiving our first chain, and settling on a new name.
order: 1
---

Lockbox was our first test of the idea behind Signer: a trading key held in shares, with the rules on a chain. It ran as a test chain, `lockbox-milestone-a-1`, and halted on 11 November at height 196,500. Before we destroyed the old machines and their key shares, we kept a full reader copy of the chain, its genesis and its validator history. Four founding validators ran it, and later participants joined, including the external validator.

The name went through two drafts, Agent Signer and then Botsign, before we settled on **Signer**. The new chain is `signer-1`. We did not relabel the old chain's history as the new one; Lockbox is archived as Lockbox.

On 12 November the rename passed its test suite: 140 of 140 full checks, 20 of 20 open-join cases and 36 of 36 admin-handover checks. One validator timing test failed, the same way it had failed before the rename.

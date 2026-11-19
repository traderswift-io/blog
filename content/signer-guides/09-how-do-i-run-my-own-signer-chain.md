---
title: How do I run my own Signer chain?
description: Signer is open source, so you can run your own copy of it, with your own machines and your own rules, without connecting to us.
order: 9
---

Signer is open source, so you can run your own Signer chain, on its own, without connecting to us.

You choose the machines that run it, and you hold the admin, the right to change who takes part.

The licence is the Apache License 2.0. The public README says it plainly: you can run it as your own chain with your own signers.

TraderSwift runs it as one of its subnets, the small chains that each do one job for the network.

## Why run my own chain?

- **You hold the admin.** On your own chain, the validators and their admin are yours. Nobody else decides who joins.
- **You choose your signers.** The machines that hold your key shares are machines you pick.
- **You keep your record.** Every policy and every decision is on a chain you run.
- **You can test freely.** A local network with throwaway keys is the safest place to learn how policies, refusals and revokes behave.

## How do I build it and start a local network?

The build and the local network are the same as on your own computer.

Follow [How do I try Signer on my own computer?](03-how-do-i-try-signer-on-my-own-computer.html). It builds the chain and the signer node, starts four validators, and shows how to stop one and watch the chain keep going.

The keys the script makes are throwaway keys for testing. Never use them for anything real.

## What is different on my own chain?

On your own chain, three things are yours to set.

- **The admin.** Your chain's admin decides how the validator set changes. On `signer-1` that is not you; on your chain it is.
- **The validators.** You decide which machines make blocks, and how many.
- **The signers.** You decide which machines hold the key shares, and how many must agree.

## What can I try on it?

The chain's README lists the texts an owner's wallet signs, for example to set or revoke a policy. It also lists the queries you can run against your own node.

Ask your agent to walk you through them:

::: prompt
I have the Signer repository at https://github.com/traderswift-io/signer cloned, and a local network running with `chain/run_local_network.sh up 4`. Read chain/README.md. Then walk me through, one step at a time: checking the validator set, writing a policy for a test delegate with one asset and small caps, querying that policy from my node, and revoking it. Use only the throwaway keys the script made. Tell me what each step should show before I run it.
:::

## Can my chain join the TraderSwift network?

**Planned.** There is no date yet.

In TraderSwift, each subnet registers on the hub, the chain that links our other chains. It then posts a daily anchor to the hub: a short fingerprint of its state.

That is how the network can check a subnet's record.

A subnet enters the hub only when the hub's admin approves its charter, the record that registers it. The validators of a subnet run by someone else join under the same open-join rule as anyone.

Milestones:

1. **The hub's admin handover.** Done on 18 November 2026: the hub's admin is now a wallet that needs any two of three signatures.
2. **Charters for other providers.** **Planned**, no date: the hub accepts registrations from providers other than TraderSwift.
3. **Your anchor.** **Planned.** Your chain registers and posts its first daily anchor.

## Final thoughts

Running your own Signer chain takes a clone, a build and one script. It is the best way to see how policies and refusals work before you trust any signer with a real key.

Joining your chain to the TraderSwift hub is the part still to come.

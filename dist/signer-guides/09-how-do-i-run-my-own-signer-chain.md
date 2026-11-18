---
title: How do I run my own Signer chain?
description: Build the Signer chain from the public code and run your own network, with your own admin. Anchoring to the hub is planned.
order: 9
---

By the end of this guide, you will be able to build the Signer chain from the public code and run your own network of it on one computer.

You choose the validators, and you hold the admin.

Signer is open source under the Apache License 2.0. The public README says it plainly: you can run it as your own chain with your own signers.

TraderSwift runs it as one of its subnets.

## Why run my own chain?

- **You hold the admin.** On your own chain, the validator set and its admin are yours. Nobody else decides who joins.
- **You keep your record.** Every policy and every decision is on a chain you run.
- **You can test freely.** A local network with throwaway keys is the safest place to learn how policies, refusals and revokes behave.

## What do I need?

- **A Linux or macOS computer** with Git and Go installed.
- **The Signer code.** `git clone https://github.com/traderswift-io/signer`
- **Rust**, if you also want to build the signer node. Its build needs `m4` on your PATH.

## How do I build it?

From the `chain` folder of the repository, build the chain's program:

```
go build -o build/signerd .
```
<!-- source: chain/README.md:49 -->

If you also want the signer node, build it from the `signer` folder:

```
cargo build --release
```
<!-- source: signer/README.md, Build -->

## How do I start a local network?

The repository has a script that starts a network of as many validators as you ask for. This starts four:

```
./run_local_network.sh up 4
```
<!-- source: chain/README.md:50 -->

Check that it's running, and stop or start one validator to see the chain keep going without it:

```
./run_local_network.sh status
./run_local_network.sh stop 2
./run_local_network.sh start 2
```
<!-- source: chain/README.md:51-53 -->

When you're done, take it down. `wipe` removes its data as well:

```
./run_local_network.sh down
./run_local_network.sh wipe
```
<!-- source: chain/README.md:54-55 -->

The keys the script makes are throwaway keys for testing. Never use them for anything real.

## What can I try on it?

The chain's README lists the texts an owner's wallet signs, for example to set or revoke a policy, and the queries you can run against your own node. Ask your agent to walk you through them:

::: prompt
I have the Signer repository at https://github.com/traderswift-io/signer cloned, and a local network running with `chain/run_local_network.sh up 4`. Read chain/README.md. Then walk me through, one step at a time: checking the validator set, writing a policy for a test delegate with one asset and small caps, querying that policy from my node, and revoking it. Use only the throwaway keys the script made. Tell me what each step should show before I run it.
:::

## Can my chain join the TraderSwift network?

**Planned.** In TraderSwift, each subnet registers on the hub chain and posts a daily anchor of its state to it.

That is how the network can check a subnet's record.

For an outside chain, that step isn't open yet: the hub doesn't yet accept registrations from outside providers. When it does, this section will be updated with the steps.

Milestones:

1. **The hub's admin handover.** The hub's admin moves to the owner's own wallet.
2. **Charters for outside providers.** The hub accepts registrations from providers outside TraderSwift.
3. **Your anchor.** Your chain registers and posts its first daily anchor.

## Final thoughts

Running your own Signer chain takes a clone, a build and one script. It is the best way to see how policies and refusals work before you trust any signer with a real key.

Joining your chain to the TraderSwift hub is the part still to come.

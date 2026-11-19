---
title: How do I try Signer on my own computer?
description: Build Signer on your own machine and start a small throwaway network, with no exchange and no real key.
order: 3
---

By the end of this page you will be able to build the Signer pieces on your own computer and run a small local chain.

Nothing on this page sends an order to a venue or uses a real key.

## What do I need?

- **A Linux machine.** Any ordinary computer will do, because the scripts assume Linux.
- **Go.** The chain is written in Go, and the public guide pins one exact version, `1.26.5`.
- **Rust and `m4`.** The signer node is written in Rust, and its math library build needs `m4` on your path. You do not need root.
- **Python 3.** The coordinator is plain Python.
- **`jq`.** The local script uses it to write the chain's start file.

## What are the pieces?

Signer has three programs. Each one has its own folder in the public repository.

- **The chain, `signerd`.** It stores policies and decision records. It is a Cosmos SDK chain written in Go.
- **The signer node, `signer-node`.** It checks an order against the policy and signs. It is written in Rust.
- **The coordinator.** It takes an order request, collects the signature and sends it on. It holds no key share.

We start with the chain, because it is the part you can run end to end today.

## How do I run a local chain?

Clone the repository, then build `signerd` from the `chain` folder. The build script expects the binary at `build/signerd`.

```
go build -o build/signerd .
```
<!-- source: chain/README.md:49 -->

The same folder has a script that starts several validators on your own machine. A validator is a node, one copy of the chain, that helps make new blocks.

```
./run_local_network.sh [--directory path] up 4
./run_local_network.sh status
```
<!-- source: chain/README.md:50-51 (`up 4` fills the validator_count slot) -->

We use four validators. A chain adds a block only when validators with more than two thirds of the votes agree.

With three equal validators, stopping one halts the chain. Four keep going with one down.

The keys in this network are throwaway. The chain id is `signer-local-1`, the keyring uses the `test` backend, and everything stays on your own machine.

## How do I break it on purpose?

The script can stop and start single nodes. This is the fastest way to see why four validators behave differently from three.

```
./run_local_network.sh stop 2
./run_local_network.sh start 2
./run_local_network.sh down
./run_local_network.sh wipe
```
<!-- source: chain/README.md:52-55 -->

`down` stops the whole network. `wipe` removes it, so the next `up` starts from block 1.

## How do I build the signer node and the coordinator?

The signer node builds with Cargo from the `signer` folder.

```
cargo build --release
signer-node signer-config.json
```
<!-- source: signer/README.md:10-11 -->

The config fields are listed in `src/signer_config.rs`.

The node speaks plain HTTP, so it listens only on your own machine and refuses any peer that is not. That keeps a test node from talking to the outside world by mistake.

The coordinator is started from the repository root.

```
python3 -m coordinator.coordinator_service coordinator-config.json
```
<!-- source: coordinator/README.md:9 -->

Live venues are off by default. The coordinator refuses any venue address that is not on your own machine, unless the operator turns a live setting on.

So pointing it at a small program of your own is the safe way to play.

## Can I run a full order against a fake venue?

**Planned.** There is no date yet.

A full order run needs two things in the public repository: the local end-to-end test suite, and the fake venue it trades against.

Today you can run the chain end to end and build the signer node.

The coordinator's local-only rule is public, but the wiring of all three is not.

## Can my agent help?

Yes. This is a good job to hand over, because everything on this page runs on your own machine and nothing is spent.

::: prompt
Read the README files in the folders chain, signer and coordinator of github.com/traderswift-io/signer. On this machine only, build signerd with the exact Go version the repository names, then start the local network with chain/run_local_network.sh using four validators. Show me the output of its status command. Then build signer-node with cargo build --release. Do not connect to any venue, do not use any real key, and do not change anything outside one new folder. If a step fails, stop and show me the last 30 lines of the log.
:::

## Why should I try it locally first?

You see the rules without risk. You can stop a validator and watch the chain keep going.

You can stop two and watch it halt.

You also learn the shape of the code before you read the policy rules in `docs/INTERFACES.md`. That file is the contract between the three programs.

## Final thoughts

The local chain is real and runs today. The full loop with a fake venue is planned, and we will update this page when it is public.

Next, read [How do I read Signer's record?](06-how-do-i-read-signers-record.html). If you want to run a node on the real chain, read [How do I run a Signer validator?](07-how-do-i-run-a-signer-validator.html).

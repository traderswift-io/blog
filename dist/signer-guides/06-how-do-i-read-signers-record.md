---
title: How do I read Signer's record?
description: Run a read-only node from the public genesis file and look at policies and decision records, signed and refused.
order: 6
---

By the end of this page you will be able to run your own read-only copy of the Signer chain, `signer-1`, and look at what it recorded.

You do not join the validator set and you do not hold any key.

## What does the chain record?

Signer keeps its rules and its decisions on one small chain.

Anyone can read them, because every node holds a full copy.

- **Policies.** An owner writes which venues a key may trade, which assets, and the size caps. The owner signs the policy with a wallet.
- **Decisions.** Every request a signer sees is recorded, signed or refused. The record has a height, a request id, the signer, the decision, the reason and a hash of the order.
The decision record is the part most people want. It is how you check that a refusal really happened.
<!-- source: docs/INTERFACES.md:7-16 -->

## Is there a public page or endpoint to read it?

No. There is no public read endpoint today.

The only way to read the record is your own node.

So you sync a node from the public genesis file and the peer list in `networks/signer-1/`, then ask it locally.

## What do I need?

- **A Linux machine.** One CPU, 2 GB of memory and 20 GB of disk is enough today.
- **Go 1.26.5.** The public guide pins this exact version. A newer Go prints a warning on every command.
- **`jq` and `curl`.** The checks below use both.
- **Outgoing access to the peers.** The node needs outgoing connections on port 26656. An open incoming port is better but not required.
<!-- source: SKILL.md:27 -->

## How do I get a read-only node?

A node that has not joined is a full node. It follows the chain and signs nothing.

The public validator guide says so: until you join, you are a full node.

So you follow the validator steps up to the wait, and you skip the join. The first step is the build.

```
git clone https://github.com/traderswift-io/signer.git signer
cd signer/chain
GOTOOLCHAIN=go1.26.5 go build -trimpath -o signerd .
```
<!-- source: docs/VALIDATOR_JOIN.md:42-44 -->

Next, make the node's own keys. Pick a short public name for `<your moniker>`.

Never share the two key files this writes.

```
sudo -u signer /opt/signer/bin/signerd init <your moniker> --chain-id signer-1 --home /var/lib/signer/chain
```
<!-- source: docs/VALIDATOR_JOIN.md:61 -->

That line assumes the system layout from the operator guide. If you build as an ordinary user, the agent guide has the same step with a folder of your own, and it needs no sudo.

## How do I check the genesis file?

The genesis file is the chain's starting rules. The tree ships it with a hash beside it.

Stop if the check does not print `OK`.

```
cd signer/networks/signer-1
sha256sum -c genesis.sha256                     # must print: genesis.json: OK
paste -sd, peers.txt                            # your persistent_peers value
```
<!-- source: docs/VALIDATOR_JOIN.md:80,83 -->

Copy `genesis.json` into your node's `config` folder and put the peer list in `persistent_peers`.

The operator guide shows the exact lines for `config.toml`.

The hash and the file come from the same place, the repository, so the check proves your copy is intact, not that the source is right.

Today the repository is the only published source for the hash.

## How do I start it and wait for it to catch up?

The operator guide runs the node under cosmovisor. Follow that section, then check the status.

```
curl -s http://127.0.0.1:26657/status | jq .result.sync_info
```
<!-- source: docs/VALIDATOR_JOIN.md:154 -->

You can also check height and peers. Wait until `catching_up` is `false` and `n_peers` is at least 1.

```
curl -s 127.0.0.1:26657/status | jq '.result.sync_info | {latest_block_height, catching_up}'
curl -s 127.0.0.1:26657/net_info | jq .result.n_peers
```
<!-- source: SKILL.md:79-80 -->

A first sync replays every block from block 1, so it takes several hours. State sync is not offered yet.

## How do I look at the policies?

Every key Signer holds has a **key ref**: its name on the chain.

The key ref records which signers hold the shares, how many must agree, and the policy epoch.

Find a key ref in the decision log below, then look it up:

```
signerd query policy key-ref --key-ref <key ref> --node tcp://127.0.0.1:26657 -o json
```
<!-- source: signer, checked on the live chain 18 Nov; the flag is required, a positional argument is refused -->

The chain also serves the same data on REST, if you turn it on.

In your node's `config/app.toml`, under `[api]`, set `enable = true` and keep the address on `127.0.0.1`, as the operator guide says. Then:

- **One key ref:** `GET /signer/policy/v1/keyref/{key_ref}`. The reply also shows the next epoch.

A missing item returns 404.
<!-- source: docs/INTERFACES.md:49 -->

## How do I look at the decisions?

Validator-set queries are plain commands on your node.

```
signerd query validatorset joiners --node tcp://127.0.0.1:26657
signerd query validatorset open-join --node tcp://127.0.0.1:26657
signerd query upgrade plan --node tcp://127.0.0.1:26657
```
<!-- source: docs/VALIDATOR_JOIN.md:188-189,246 -->

Decisions are read with the command line. The record is a list, and you read it in pages.

```
signerd query policy --node tcp://127.0.0.1:26657
```
<!-- source: chain/README.md:44,138 -->

That command lists the policy queries. The decision log is `log-entries`, read in pages from a first sequence number:

```
signerd query policy log-entries --first-sequence 1 --limit 20 --node tcp://127.0.0.1:26657 -o json
```
<!-- source: signer, run against the live chain 18 Nov -->

The answer carries `next_sequence`. Use it as the next `--first-sequence` to read the following page.

The page size stops at 1000.

## How do I read one decision?

Each entry holds a height, a request id, a key ref, a signer id, a decision, a reason and an intent hash.
<!-- source: docs/INTERFACES.md:15 -->

A normal order on `signer-1` leaves four lines. Three signers say `signed`.

The fourth says `refused` with the reason `quorum_met_without_this_signer`, because three of four were enough. That line is not a rejection of the order.

Real refusals carry other reasons. `vault_mismatch`, `asset_not_allowed` and `policy_closed` are three of them.

A request refused by the first signer before it proposes leaves one line.
<!-- source: docs/INTERFACES.md:105-119 -->

## How do I let my agent read it for me?

::: prompt
Follow the steps for a node that does not join in docs/VALIDATOR_JOIN.md of github.com/traderswift-io/signer. Build signerd with the exact Go version it names, check the genesis hash, start the node and wait until catching_up is false. Do not run the join step. Never print the two key files in the node's config folder. Then list the decision records and tell me, in plain words, how many were signed and how many were refused, and the most common refusal reason. If a step fails, stop and show me the last 30 lines of the log.
:::

## Final thoughts

You can now read the same record we read. Nobody has to tell you what a signer did, because the chain says so.

If you want your node to produce blocks as well, read [How do I run a Signer validator?](07-how-do-i-run-a-signer-validator.md).

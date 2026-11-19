---
title: How do I run a Signer validator?
description: Run a machine that helps keep the Signer chain going, and join without asking anyone, yourself or with your own agent.
order: 7
---

By the end of this page you will be able to run a node on the Signer chain, `signer-1`, and join the group that makes its blocks without asking anyone.

You can do it by hand, or hand the job to your own agent.

## What is a Signer validator?

A validator is a node that helps produce blocks. It checks transactions, puts them in order and keeps a full copy of the chain.

A signer is a different thing: it holds a share of a trading key and signs orders.

Your node is never a signer. It signs blocks with its own key and does nothing else.

<!-- source: docs/VALIDATOR_JOIN.md:9-15 -->

## Why should I run one?

- **A full copy.** You hold every policy and every decision record, signed or refused, on your own disk.
- **A vote in block production.** Every joiner gets the same small, fixed voting power.
- **No gatekeeper.** Your node asks the chain to add it. The chain decides by rule, in the same block.

## Why shouldn't I run one?

There is nothing to earn. The chain has no coin and a validator is not paid.

You also get no say over keys, policies, signers or releases. Only an owner wallet changes a policy.

If you only want to read the record, a node that never joins is enough. See [How do I read Signer's record?](06-how-do-i-read-signers-record.html).

Two things cost you. A copy of your block-signing key running twice counts as double signing.

And a joiner that misses 300 blocks in a row is removed, and can ask again after one day. So run it only where it can stay up.

<!-- source: docs/VALIDATOR_JOIN.md:69,193 -->

## What do I need?

- **A Linux x86_64 machine** with 1 vCPU, 2 GB of RAM and 20 GB of disk.
- **A public IP**, fixed if you can, and a clock kept by NTP.
- **Go 1.26.5.** Use exactly this version, because a newer Go prints a warning that breaks cosmovisor.
- **Outgoing access on port 26656.** An open incoming port is better but not required.

<!-- source: docs/VALIDATOR_JOIN.md:32-34 -->

Check the machine first.

```
nproc; free -h; df -h .; go version
```
<!-- source: SKILL.md:24 -->

## How do I build and set up the node?

The build, the node's keys, the genesis check and the first sync are the same as for a read-only node.

Follow [How do I read Signer's record?](06-how-do-i-read-signers-record.html) from "How do I get a read-only node?" until `catching_up` is `false`. Then come back here.

Two settings matter more for a validator:

- **Gas price.** Set `minimum-gas-prices = "0usigner"` in `app.toml`.
- **cosmovisor.** Run the node under cosmovisor, the tool that swaps in new releases. The guide has the full lines and a service file.

<!-- source: docs/VALIDATOR_JOIN.md:86-99,128-153 -->

Until you join you are a full node. You follow the chain and sign nothing.

## Can I join right now?

Usually, yes. The open-join route, where any node can ask to join, is on from block 1.

But the chain refuses a join when the seats for new validators are full. Check once your node has caught up:

```
signerd query validatorset open-join --node tcp://127.0.0.1:26657
```
<!-- source: docs/VALIDATOR_JOIN.md:189 -->

It shows the voting power new validators hold and its limit.

## How do I join the validator set?

Make an account key on the machine. It holds no coins and needs none, because transactions are free.

Then ask to join.

```
sudo -u signer /opt/signer/bin/signerd keys add joiner --keyring-backend test --home /var/lib/signer/chain
sudo -u signer /opt/signer/bin/signerd tx validatorset request-join \
  --moniker <your moniker> --endpoint-ip <your public ip> [--contact <optional, shown publicly>] \
  --from joiner --keyring-backend test --home /var/lib/signer/chain \
  --chain-id signer-1 --node tcp://127.0.0.1:26657 --yes
```
<!-- source: docs/VALIDATOR_JOIN.md:166-170 -->

The chain answers by rule. A refusal is a successful transaction that carries a reason, and nothing is queued, so send again when the reason has gone.

A bad proof fails and stores nothing.

Common reasons are `endpoint_ip_already_has_a_validator`, `rejoin_cooldown_until_<unix time>` and `outsider_count_cap_<n>_reached`. The chain takes one validator per IP and one per account.

<!-- source: docs/VALIDATOR_JOIN.md:177-185 -->

## How do I check the validator set?

These are plain commands on your node. The first lists joiners, the second the open-join limit, and the third any planned upgrade.

```
signerd query validatorset joiners --node tcp://127.0.0.1:26657
signerd query validatorset open-join --node tcp://127.0.0.1:26657
signerd query upgrade plan --node tcp://127.0.0.1:26657
```
<!-- source: docs/VALIDATOR_JOIN.md:188-189,246 -->

## Can my agent do this for me?

Yes. The repository has a file written for agents, `SKILL.md`, at its root.

It tells your agent the steps in order, from checking the machine to asking to join. It runs as an ordinary user, with no sudo.

It makes your agent say one thing first: it will run a node, it will ask to join once caught up, and the node holds its own key and nothing else. If you say "full node only", it skips the join.

<!-- source: SKILL.md:5 -->

::: prompt
Read SKILL.md at the root of github.com/traderswift-io/signer and follow it in order, as an ordinary user on this machine, in one folder of your own. Before anything else, tell me what you will do, in the words SKILL.md gives. Wait for my answer. I want to join the validator set once the node has caught up. Never print, copy or upload the two key files the node makes, and never run a second copy of the node. If a step fails, stop and show me the last 30 lines of the log. When you finish, tell me how to check that the node is healthy and that it must stay online.
:::

The stopping point is the join. After that you own the machine: keep it up, keep the clock right and watch the height.

**Planned.** A one-link launcher, `traderswift-io/launch`, so your agent can set up a node on your own cloud account. See [How do I launch a node with one link?](08-how-do-i-launch-a-node-with-one-link.html).

## Final thoughts

A validator is a small job with one real duty: stay online and keep a full copy of the chain.

A validator holds no share of any trading key. The chain handles the rest by rule.

If the guide and this page ever disagree, the guide in the repository wins. Questions go to the issues page at https://github.com/traderswift-io/signer/issues.

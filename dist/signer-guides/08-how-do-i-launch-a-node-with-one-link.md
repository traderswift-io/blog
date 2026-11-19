---
title: How do I launch a node with one link?
description: Give your own agent one link, say "Go" once, and it sets up a machine for you, locks itself out and leaves. Planned.
order: 8
---

**Planned.**

This page is half written on purpose. The first half explains what the launcher does and how it keeps you safe.

The second half is the milestones. When the launcher is ready, this page will be updated with the full steps.

Once it is built, you will be able to give your own AI agent one link and have it launch a TraderSwift node on your own cloud account. You say "Go" only once.

## What is the launcher?

The launcher is a public repository, `traderswift-io/launch`. Its `AGENTS.md` file is a manual written for agents.

Any agent that can read a file and run Python can follow it top to bottom.

Small scripts do the steps. Your agent runs them with your own cloud token.

The token never reaches us.

The first path launches a validator for the TraderSwift hub, the chain that links our other chains. A Signer node comes second.

## How does it work?

Your agent follows five steps:

1. **Before.** You create a cloud token that can only create machines and firewalls, with the shortest expiry your provider offers, and give it to your own agent.
2. **Tell.** The agent shows you one message with the plan, then asks one question: "Go?"
3. **Do.** It creates the firewall first, so the machine is never born open, then creates the machine and installs the node.
4. **Done.** It tells you the node is running and shows how to check it.
5. **Leave.** It removes its own access, closes the firewall back down, and revokes the token.

The message in step 2 tells you:

- what it will create;
- what it costs each month;
- which emails your provider will send;
- what stays open afterwards.

In step 3 the agent installs only a release whose checksum matches. It makes the node's keys on the node itself, and waits for it to sync.

In step 5 the token is revoked for good. If you need to do this again, you create a new token.

## Why does the agent remove itself?

Because a node you can't log in to is a node no one else can log in to either.

Before a node holds anything worth taking, the agent that built it is locked out. We call that sealing the node.

That is the same rule we follow on our own machines.

Every Signer machine we run is sealed before it holds a share.

## What will the prompt look like?

When the repository is public, this is all you will give your agent:

::: prompt
Read https://github.com/traderswift-io/launch/blob/main/AGENTS.md and follow it to launch a TraderSwift validator on my cloud account. Show me the plan and the monthly cost, and ask me "Go?" before you create anything. When you're done, remove your own access and revoke the token.
:::

Until then, the link will not work. The manual guide for running a Signer validator by hand is in [How do I run a Signer validator?](07-how-do-i-run-a-signer-validator.html).

## What are the milestones?

1. **Signed releases.** Chain releases published with their checksums, and the node updater added to the release rules.
2. **The validator path.** The launcher's validator steps in `traderswift-io/launch`.
3. **One real run.** Launch, sync, seal, a check from outside, and the token revoked, on a real cloud account.
4. **Public.** The repository goes public.
5. **The Signer node path.** A Signer validator waits on the launcher itself. A signer that holds part of a key waits on signers from other operators being able to join, which is not yet scheduled.
6. **A second provider.** A DigitalOcean path.

The first provider is Linode. Others can be added through a pull request.

## Final thoughts

The launcher turns "run a node" into one link and one "Go".

The parts that matter for safety come first: the firewall before the machine, the seal before anything of value, and the agent removing itself at the end.

When the repository is public, this page gets the full walkthrough.

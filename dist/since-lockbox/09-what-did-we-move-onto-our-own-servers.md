---
title: What did we move onto our own servers?
description: Our own rack servers, Proxmox, and a reboot that tested the hub.
order: 9
---

We added our own rack servers and are moving onto Proxmox, so each role (agents, Codex, data, research and our Git server) gets its own virtual machine.

Snapshots are the rollback.

The first plan was to evacuate everything before touching a server.

We changed it: install in place, with one reboot, instead of waiting.

It was not smooth. One reboot cut a server's network.

The hub kept running on three of its four validators, which is what a four-validator chain is for, and the second Codex was offline until it came back.

By 17 November the hub validators had moved; by 18 November the data copy had started and the second Codex was back.

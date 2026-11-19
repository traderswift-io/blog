---
title: What did we move onto our own servers?
description: Our own rack servers, and a reboot that tested the network.
order: 12
---

We added our own rack servers.

We are moving them onto Proxmox, software that splits one server into many separate virtual machines.

Each role gets its own virtual machine:

- agents;
- Codex;
- data;
- research;
- our Git server.

Snapshots are the rollback.

The first plan was to evacuate everything before touching a server. We changed it: install in place, with one reboot, instead of waiting.

It was not smooth. One reboot cut a server's network.

The hub kept running on three of its four validators, which is what a four-validator chain is for. The second Codex was offline until the network came back.

By 17 November the hub validators had moved; by 18 November the data copy had started and the second Codex was back.

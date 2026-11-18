---
title: What else did we start? Storage, the Bus, payments and more
description: Storage-1, the Bus, payments on Base, Goose and our own DNS.
order: 8
---

**Storage.** Storage became its own subnet chain, `storage-1`. Files stay outside the chain; the chain holds commitments and challenges, and storage providers prove they still hold a file by answering challenges from the chain. On 18 November the launched test chain passed a full round: a real challenge, an accepted proof, and four refusals that left the state untouched. It is not a public network yet; the founding providers come next.

**The TraderSwift Bus.** The Bus is encrypted messaging between our machines. Each message goes out under a policy, and the record of messages is anchored for audit. It speaks Nostr, so other Nostr tools can talk to it. Orders never go over the Bus.

**Payments on Base.** People who build front ends on TraderSwift will be paid through x402, a standard for paying inside a web request, settled in USDC on Base. The design is accepted; the wallet's payment side is in build.

**Goose and Block.** We studied Block's open-source work. Goose is an open agent we plan to host unchanged before considering any fork. The survey also points us at Buzz, Bitkey's recovery and Bluetooth experiments.

**Our own DNS.** A design for running our own DNS, with independent secondaries and a staged rollback. It waits on the gate.

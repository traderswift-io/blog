---
title: What is traderswift-1, the chain at the centre?
description: The chain at the centre of TraderSwift, and its move to new machines.
order: 3
---

`traderswift-1` is the chain at the centre of TraderSwift, and we call it the hub.

The other chains are subnets: each one runs on its own and does one job, such as signing or storage.

The hub holds:

- identities;
- each subnet's charter, the record that says what the subnet is and who runs it;
- the providers who run each subnet;
- the anchors subnets post to it, short fingerprints of their history that can be checked later.

It holds no token and no balances. [How does the network fit together?](../what-is-traderswift/24-how-does-the-network-fit-together.html) explains the whole network.

![The hub and its subnets](../assets/since-lockbox/hub-and-subnets.svg)

The hub went live on 14 November; its first block was signed at 14:13 UTC. It is **Live**.

On 17 November we moved its validators onto new machines. The result is four validators with equal power, and block 40,631 was signed by all four.

![traderswift-1 heights recorded this week](../assets/since-lockbox/hub_heights.svg)

## Who controls the hub?

On 18 November we handed over the hub's admin. The admin is now a multisig: a wallet that needs two of three signatures before it can act.

## When do the first charters arrive?

There is no date yet. The first charters wait on one security step, then on the owner's approval.

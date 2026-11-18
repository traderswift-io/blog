---
title: What is in the pipeline?
description: The marketplace, signal providers, Ledger, Vault and Storage.
order: 3
---

These parts are being built or planned. None of them is live yet.

## The marketplace

**Being built.** The TraderSwift marketplace lists front ends.

Ours are listed free. Outside builders can list theirs and charge per use over x402.

The user pays the builder directly, and we never hold the money. The catalog is built and checked offline. No listing is live yet.

**Planned.** Data nodes will list what they sell there too, and builders will find them.

Each paid request is metered. The meter records which node stored the data and which node served it, and the caller pays over x402.

The meter and the x402 payment step are built, and have been checked against test payment services only.

They have not yet taken a real payment.

## Signal providers

**Being built.** Plenty of people say they offer good signals. Very few can show it.

A signal provider on TraderSwift can be a person or a machine. Each signal is a fixed record: the market, the side, the levels, the invalidation, the confidence and the expiry.

Each signal is fingerprinted and timestamped before the outcome. The content stays private, and every authorised read is logged.

That part is built, off chain. Putting the fingerprints and the readers on a Signals chain is planned.

Once the fingerprints are on the Signals chain and a signal is revealed, anyone will be able to match it to its fingerprint. That is how a provider's record will be checked, not just claimed.

## Agents with a record

**Planned.** The same idea applies to agents.

An agent that trades through Signer already has every order request it makes, signed or refused, recorded on a public chain. The marketplace is where those records can be found and compared.

## Ledger, Vault and Storage

**Being built.** Ledger holds a user's tasks and decisions. Vault holds their notes and files.

Both are chains that answer two questions: where the data is, and who may read it. The data itself never goes on a chain. It is encrypted on the user's phone.

Who a user shares with is stored only as a salted commitment. The chain does not reveal which apps or agents someone uses.

Ledger has passed its first local test. Vault is being built from it.

Storage is the subnet where providers hold encrypted data, and the chain records proofs that they still hold it. Its test chain passed a full round on 18 November. It waits on its founding providers, and on an outside review of its encryption before it holds real data.

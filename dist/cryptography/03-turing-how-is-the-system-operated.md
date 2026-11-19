---
title: Turing: how is the system operated?
description: How routine, repeated structure and everyday operation make an attack easier, and how far one break spreads.
order: 3
---

**The question:** What routine, repeated structure or operational shortcut makes the problem easier, and how far does one successful break spread?

## What is a crib?

A crib is known or guessed plaintext at a suspected position.

Historical cryptanalysis used likely phrases and recurring message formats to constrain possible machine settings. Turing's Enigma treatise discusses cribs and depth as practical sources of information. [4]

Our modern example is an instruction beginning with `account=`. That prefix is predictable.

In the reused-stream example, it exposes the corresponding stream bytes and helps read other messages encrypted at those positions.

Predictable plaintext is not, by itself, a break of properly used modern encryption.

Do not fix a nonce-reuse bug by removing predictable headers. Fix the nonce-reuse bug.

## Why does the operator matter?

Imagine a service that increments a counter for every encrypted message. Everything works in a single process.

Then a second worker starts with the same key and a counter of zero.

Both workers now generate the same nonce values. The algorithm has not changed.

Deployment has changed the conditions under which it runs.

Run the same reasoning through:

- a restart;
- a backup restore;
- a failed deployment;
- a retry.

Ask whether a retry sends the original ciphertext again or performs a fresh encryption using a previously allocated nonce. These are different operations.

Re-sending identical ciphertext does not require a new encryption invocation. It can still cause a replay problem if the receiver executes the request twice.

Nonce discipline and replay prevention solve different problems.

## Does reading one message expose all the others?

Be precise about what was recovered.

| Recovered item | What to investigate next |
| --- | --- |
| One plaintext | Whether it gives a useful crib against related messages |
| Reused stream bytes | Other messages at the same stream positions |
| One session key | Traffic protected by that key and its derivation relationships |
| A master derivation key | Every retained or reproducible child key |
| A signing key | Every action still authorized for that key |
| One share | Whether the threshold, backups or other accessible shares make it sufficient |

Suppose every daily key is `KDF(master, date)`.

Deleting yesterday's daily key does not protect yesterday if the attacker later obtains the master and can derive it again.

Compare that with an authenticated ephemeral key exchange where the session secrets have been erased. Under its assumptions, later compromise of a long-term authentication key need not reveal past session keys.

This is forward secrecy.

TLS 1.3 describes both its protections and exceptions; its 0-RTT data does not have full forward secrecy. Forward secrecy also does not mean a compromised endpoint automatically heals. [5]

## How do I review the procedure?

Follow one secret through:

- creation;
- deployment;
- normal use;
- restart;
- recovery;
- retirement.

At each stage, ask who can recover it and what state must survive.

For a signing service, include what happens after an incident.

Disabling the API route is insufficient if the copied key remains authorized by the receiving system. The relevant boundary is wherever the signature is accepted.

**Try it:** Two workers share one AES-GCM key. Each starts its nonce counter at zero.

Is making the counter 128 bits long enough to fix the design? Explain why the collision occurs before counter exhaustion matters.

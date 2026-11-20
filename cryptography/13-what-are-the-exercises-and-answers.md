---
title: What are the exercises and answers?
description: Answers to each chapter's Try it question, six more calculations, and what each Python lab shows.
order: 13
---

## What are the answers to the chapter questions?

**Shannon:** Four decimal digits have at most 10,000 possibilities, or about 13.29 bits of entropy if uniformly chosen.

Expanding them to 32 bytes does not enlarge the candidate space. A slow password KDF can increase the cost per guess, but does not create missing entropy.

**Turing:** Both workers choose the same initial values.

A wider counter delays wraparound; it does not separate workers or prevent a reset from revisiting previously used values.

**Diffie:** The client has not authenticated the source of its initial trusted key.

An attacker who substitutes that key can later produce signatures that verify under the substituted key.

**Hellman:** Two values: 1 and p - 1 for an odd prime p. Large representation size does not create a large subgroup.

**Merkle:** The file and proof are consistent with the supplied root.

That does not authenticate the root, establish the true history, or prevent the server from constructing another consistent tree.

**Rivest:** Round trips test whether decryption reverses encryption.

They do not test whether an observer can encrypt a small list of possible commands and identify the matching ciphertext.

**Shamir:** The dashboard enforces an application approval policy.

A compromised process holding the full key may sign without satisfying that policy unless an independent accepting boundary enforces it.

**Adleman:** The attacker receives the exploitable output despite the warning. Detection must prevent release through every response and diagnostic path.

**Schneier:** The receiver needs a freshness policy, authenticated identifiers and enforcement that prevents duplicate commitment under retries and concurrency.

Cryptographic authentication alone does not provide this state.

## What other calculations can I try?

**1. A reused XOR stream:** Let C1 = `EB`, C2 = `E8` and known M1 = `41`, all hexadecimal. Find M2.

**Answer:** `EB XOR E8 XOR 41 = 42`. This recovers one byte at the reused position.

**2. Unicity estimate:** A toy model has 60 bits of key entropy and 3 redundant bits per symbol. What does the estimate predict, and what does it not predict?

**Answer:** Approximately 20 symbols before the model suggests a unique plausible solution. It does not specify an attack, a runtime or an exact boundary for each message.

**3. Hash work factor:** An ideal hash is truncated to 80 bits. What is the generic collision work factor?

**Answer:** On the order of `2^40` evaluations, not `2^80`. Preimage search is a different question.

**4. RSA capacity:** How many bytes can OAEP with SHA-256 encrypt using a 2,048-bit RSA modulus?

**Answer:** `256 - 2 × 32 - 2 = 190` bytes. This says nothing about the safety of an otherwise unspecified envelope format.

**5. Shared control:** A 3-of-5 arrangement places three shares under one administrator and two under separate administrators. How many administrative compromises may be enough?

**Answer:** One, if the first administrator can obtain all three controlled shares.

The mathematical share threshold can remain three while administrative independence collapses.

**6. Nonce collisions:** How does the approximate random-nonce collision probability change when message count doubles, while nonce length stays fixed?

**Answer:** It increases by about four times while the probability is small, because the number of pairs grows approximately with the square of message count.

## What do the Python labs demonstrate?

| Lab | Expected result | What it does not prove |
| --- | --- | --- |
| XOR reuse | Recovers the second toy plaintext | An attack on properly used AEAD |
| DH | Both sides calculate 2 | Authentication or realistic parameter security |
| Merkle proof | Valid C passes; altered C and wrong sibling order fail | Trust in the root or completeness of the log |
| Raw RSA | Round trip passes; modified ciphertext decrypts to 130 | Secure encryption |
| Shamir | All ten triples recover 42; 257 possible secrets fit the selected pair | A production sharing or threshold-signing protocol |
| CRT fault | Fault reveals factor 53 and fails verification | Complete resistance to physical faults |
| AEAD | Alterations fail; unchanged replay still decrypts | Key custody, nonce lifecycle or replay enforcement |
| HMAC | Original message passes; changed message fails | Constant-time behavior of the whole application |

The lab outputs are demonstrations, not a certification suite.

Their purpose is to make the distinction between a mathematical property and a system claim visible.

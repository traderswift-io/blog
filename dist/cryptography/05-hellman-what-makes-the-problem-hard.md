---
title: Hellman: what makes the problem hard?
description: Which mathematical problem an attacker must solve, and why the exact numbers chosen matter.
order: 5
---

**The question:** Which mathematical problem must an attacker solve, under which assumptions, using these exact parameters?

## What is a one way function?

A one-way function is efficient to compute but hard for an efficient attacker to invert on appropriately sampled inputs.

The sampling condition matters. A function does not become useful cryptography because we found a few inputs that look difficult.

For familiar practical constructions, hardness rests on assumptions and analysis rather than an unconditional proof that every possible attack is impossible. [6]

For the previous example, calculating `5^6 mod 23` is easy. Recovering an exponent from its public result is a discrete-logarithm problem.

At this size it is also easy. We need to inspect the problem size and structure, not just its name.

## Are the assumptions interchangeable?

| Problem | Given | Asked to find or decide |
| --- | --- | --- |
| Discrete logarithm, DLP | g and g^a | a |
| Computational Diffie-Hellman, CDH | g, g^a and g^b | g^(ab) |
| Decisional Diffie-Hellman, DDH | g, g^a, g^b and Z | Whether Z equals g^(ab), against an appropriate random alternative |
| RSA inversion | n, e and y | x such that x^e mod n = y |
| Integer factorization | Composite n | Its prime factors |

These are different tasks.

A DLP solver gives a route to CDH, and a CDH solver gives a route to DDH. The reverse implications are not generally available.

Factoring an RSA modulus lets us derive its private exponent, but general RSA inversion is not known to be equivalent to factoring in all cases. [2, 15]

When a design says “based on discrete logarithms,” ask for the actual scheme and its security argument.

That description alone does not establish authentication, chosen-ciphertext security or correct handling of malicious inputs.

## What can go wrong with the parameters?

Take a very large prime p and choose `g = p - 1`. That generator only produces two results: 1 and p - 1.

The prime can be huge while the useful search space is tiny.

With p = 23, repeated powers of 22 alternate between 22 and 1. A 4,096-bit representation would not fix the fact that there are only two possibilities.

In finite-field protocols, inspect these, as required by the chosen scheme:

- the group;
- subgroup order;
- generator;
- private-exponent generation;
- public-value validation.

Standardized finite-field groups and validation rules exist; RFC 7919 gives one concrete TLS profile. [9, 10]

Validation is algorithm-specific. X25519 has different input-processing rules from a conventional finite-field DH implementation.

RFC 7748 discusses small-order inputs and an all-zero shared result; protocols using it may impose additional rejection requirements. Do not copy one algorithm's validation checklist into another. [11]

## How do bits of security differ from key size?

Here is a classical-security comparison, not a promise that every implementation reaches these levels.

| Construction or parameter | Approximate strength under conventional assumptions |
| --- | --- |
| AES with a uniformly random 128-bit key | 128 bits against generic key search |
| RSA with a 3,072-bit modulus | 128-bit security category |
| A suitable elliptic curve with roughly 256-bit group order | Roughly 128 bits against generic discrete-log attacks |
| An ideal 256-bit hash output | Roughly 128 bits for collisions; 256 for preimages |

RSA modulus length is not RSA security strength.

NIST's key-management guidance provides comparisons for asymmetric and symmetric systems; hash strength also depends on which attack is being considered. [12, 13]

If a system combines a strong cipher with a weak password, weak key exchange or leaked key, increasing the cipher's key size does not repair that other weakness.

Quantum attacks change this comparison. RSA and conventional DH or elliptic-curve systems are not post-quantum designs.

NIST's ML-KEM standard is one established post-quantum key-establishment building block, not a drop-in claim that an entire application is quantum-safe. [29]

## What should a defensible claim look like?

Write:

- the scheme;
- parameter set;
- randomness source;
- input validation;
- attack model;
- security target.

Then connect each requirement to a configuration or implementation location.

**Try it:** A developer chooses a 4,096-bit prime and the generator `p - 1`. What is the largest number of distinct public values this generator can produce?

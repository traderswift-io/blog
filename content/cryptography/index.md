---
title: How do we understand and review cryptographic systems?
description: How to check whether a system really protects a secret, with small worked examples you can run yourself.
order: 2
kind: guide
---

If you want to understand whether a system actually protects a secret, the name of its encryption algorithm is only the starting point.

We need to know:

- where the key came from;
- who can use it;
- what happens when the software restarts;
- what an attacker gets if one part fails.

A system can use strong encryption and still send the key to its log server.

In this guide, we will work through nine ways to examine a cryptographic system. Each has a familiar name attached to it:

- Shannon
- Turing
- Diffie
- Hellman
- Merkle
- Rivest
- Shamir
- Adleman
- Schneier

These are teaching labels based on the subjects below, not quotations or claims about how these people would assess a particular product.

We will start with the basic terms, work through the mathematics with small numbers, and finish by reviewing a fictional signing service.

The examples are deliberately small enough to check yourself. The accompanying Python file runs the same ideas locally without connecting to an account or sending a transaction.

[Download the labs](../assets/cryptography/Cryptography_Practical_Labs.py)

By the end, you should be able to explain a security claim, identify the assumptions behind it, and design a test that could disprove it.

Becoming an expert also takes repeated practice with specifications, implementations and independent review. [How do I keep learning?](14-how-do-i-keep-learning.html) gives you a route for doing that.

**Reading route:** Read chapters 1 through 10 in order on your first pass.

Then complete the review exercise in [chapter 11](11-what-does-a-complete-review-look-like.html) before looking at its answer key. Use [chapter 12](12-what-goes-on-a-review-worksheet.html) as a reference during an actual review.

**Examples:** The hand-written XOR, Diffie-Hellman, RSA and secret-sharing examples teach the mathematics. They are not production implementations.

The authenticated-encryption example uses a maintained library, but still does not implement a complete application protocol.

Prepared 17 November 2026.

References are linked at the end. Versioned specifications are identified explicitly; check their current errata before implementation.

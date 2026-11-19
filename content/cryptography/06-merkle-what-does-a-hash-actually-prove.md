---
title: Merkle: what does a hash actually prove?
description: What a fingerprint of data really proves, and why it matters who gave you the value you check against.
order: 6
---

**The question:** What is committed to, how are the bytes encoded, and how much work would the relevant attack require?

## What does a cryptographic hash guarantee?

We need to distinguish three attacks.

In a preimage attack, the digest is fixed and the attacker searches for an input. In a second-preimage attack, an original input is fixed and the attacker seeks a different input with its digest.

In a collision attack, the attacker can choose both inputs. [13]

For an ideal n-bit digest, generic collision search takes on the order of `2^(n/2)` work, while generic preimage search takes on the order of `2^n`. These are different search problems.

Real algorithms can have weaknesses; actual bounds can also depend on message size and how the hash is used. [13]

Why does collision search get the square root? With q sampled values, there are `q(q-1)/2` pairs to compare.

The approximate collision probability, while small, is `q(q-1) / 2^(n+1)`. We do not have only q chances to match a previously specified value; we have all those pairs.

For a 32-bit truncated digest, collisions become unsurprising after roughly tens of thousands of samples.

A checksum that looks long in a log line can be a poor adversarial commitment.

## How does a Merkle tree work?

Hash each record, then combine neighboring hashes until only a root remains.

A verifier can check one record using a short path of sibling hashes instead of downloading every record.

For four records A, B, C and D, use this explicit construction:

- **LA, LB, LC, LD**: each is `H(0x00 || record)`
- **AB**: `H(0x01 || LA || LB)`
- **CD**: `H(0x01 || LC || LD)`
- **Root**: `H(0x01 || AB || CD)`

To prove C is included, send C, its right sibling LD and the left sibling AB at the next level.

The verifier computes LC, then CD, then the root. Left and right positions matter.

This is the leaf and node separation used in Certificate Transparency's Merkle construction. For a tree with about one million leaves, an inclusion path needs about 20 sibling hashes.

An inclusion proof establishes membership relative to a root; a consistency proof addresses whether one tree extends another. [16]

Here is the lab. It is also in [the labs file](../assets/cryptography/Cryptography_Practical_Labs.py), so you can run it on your own computer.

```python
from hashlib import sha256


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def leaf(record: bytes) -> bytes:
    return sha256(b"\x00" + record).digest()


def node(left: bytes, right: bytes) -> bytes:
    if len(left) != 32 or len(right) != 32:
        raise ValueError("SHA-256 children must be 32 bytes")
    return sha256(b"\x01" + left + right).digest()


a, b, c, d = [leaf(value) for value in (b"A", b"B", b"C", b"D")]
ab, cd = node(a, b), node(c, d)
root = node(ab, cd)
# This proof has a fixed four-leaf shape. It is not a general verifier.
proof_root = node(ab, node(leaf(b"C"), d))
changed_root = node(ab, node(leaf(b"X"), d))
wrong_order = node(node(leaf(b"C"), d), ab)
check(proof_root == root, "Correct proof must verify")
check(changed_root != root, "Changed leaf must fail")
check(wrong_order != root, "Wrong sibling order must fail")
print("3 Merkle: C verifies; altered C and wrong order fail")
```

Our own four-record example exposes another question: who supplied the root?

If an attacker changes C and supplies a new root alongside it, a locally correct proof can still verify. Obtain the root through an authenticated process and check its context, tree size and freshness.

A Merkle tree also cannot tell us that an order actually reached an exchange. It can commit to a record asserting that the order did.

Evidence of external execution is a separate requirement.

## Why do we need domain separation?

The prefixes `0x00` and `0x01` distinguish a leaf from an internal node.

Without this distinction, a record containing two concatenated child hashes could be interpreted as a node input.

More generally, distinct purposes need distinct, unambiguous encodings. Domain-separation tags keep one use of a hash from accidentally sharing an input domain with another.

RFC 9380 explains the principle and why injective encoding matters. [17]

Consider `H(user || amount)`. The pairs `("ab", "c")` and `("a", "bc")` produce identical input bytes.

No cryptographic collision is needed.

One solution is a specified length-prefixed encoding. Another is a defined canonical serialization.

Whatever format is chosen, specify, where relevant:

- field types;
- integer ranges;
- byte order;
- optional fields;
- duplicate-field handling;
- text normalization.

Both sides must authenticate the same bytes and interpret them the same way.

For a signing request, a useful application domain might identify the protocol version, network and action type.

A request to display a preview must not become a request to execute a trade merely because both contain the same account and amount.

## What is length extension?

SHA-256 processes padded blocks and exposes its final chaining state in the full digest.

If somebody uses `SHA256(secret || message)` as a MAC, an attacker who knows the digest and can determine or guess the original byte length can extend that state to authenticate `message || glue_padding || extra` without learning the secret.

This follows from the processing structure; it does not recover the original message or break SHA-256's preimage resistance. [18]

The padding is part of the forged byte sequence. Exploitability depends on whether the application's parser accepts those bytes and gives the appended data a useful meaning.

Use a specified MAC such as HMAC-SHA-256 rather than inventing a secret-prefix hash.

HMAC has a keyed inner and outer construction designed for message authentication. Simply reversing concatenation to `H(message || secret)` is not a general substitute for a reviewed MAC scheme. [14]

SHA-3 does not have the same straightforward digest-as-chaining-state extension behavior. That does not make every homemade keyed SHA-3 construction an appropriate MAC.

Use a specified construction. [28]

## What should I check?

Ask:

- what attack is relevant;
- how many bits are retained;
- how fields are encoded;
- where the trusted root or expected digest comes from.

Changing a record should invalidate its proof; changing the record and replacing an unauthenticated root may not.

**Try it:** You receive a file, its hash and its Merkle proof from the same untrusted server. The server also supplies an unsigned root.

What has successful verification actually established?

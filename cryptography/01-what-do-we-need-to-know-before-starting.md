---
title: What do we need to know before starting?
description: The properties, building blocks, small mathematics and attacker model that every later chapter uses.
order: 1
---

Start with the property you want.

These words are often used as though they mean the same thing.

## What is cryptography supposed to do?

| Property | What we want | What does not establish it by itself |
| --- | --- | --- |
| Confidentiality | An outsider cannot learn protected message contents | A hash or a signature |
| Integrity | Unauthorized changes are detected | Encryption without authentication |
| Authentication | Evidence that a message or peer is associated with a particular key or identity | An unverified public key |
| Authorization | The authenticated party is allowed to perform this action | A valid signature alone |
| Freshness | A request is new enough and has not already been used | A valid authentication tag |
| Availability | The service remains usable under its stated failure conditions | Strong mathematics alone |

Suppose an agent signs an order to buy 10 units. The signature may establish that a particular key authorized those bytes.

We still need to decide whether that key may trade this account, whether 10 units exceeds its limit, and whether this exact order has already been executed.

Those are separate checks. Write them down separately.

## What are the main building blocks?

**Symmetric encryption** uses a shared secret key.

Anyone who has that key can usually decrypt, and with an authenticated-encryption scheme can also produce valid protected messages.

**Public-key encryption** has a public encryption key and a private decryption key. **Digital signatures** use a private signing key and a public verification key.

Do not treat signing as a general operation called “encrypting with the private key.” The construction and security goal are different.

A **hash** creates a digest from data. An ordinary hash is unkeyed: anyone can compute it.

A **message authentication code**, or MAC, uses a secret key.

**Authenticated encryption with associated data**, or AEAD, protects the message and authenticates additional context that remains visible. [3, 14, 23]

A **nonce** is a value whose required behavior depends on the scheme.

For AES-GCM, the essential rule is that it must not repeat under the same key. It need not be secret.

A password salt has another job. An RSA padding seed has another.

Calling all three “random numbers” hides requirements we need to inspect.

## How much mathematics do I need?

We will use six operations.

| Notation | Meaning | Example |
| --- | --- | --- |
| `a XOR b` | Compare corresponding bits; output 1 when they differ | `1010 XOR 1100 = 0110` |
| `a mod p` | Remainder after dividing by p | `29 mod 23 = 6` |
| `a^b mod p` | Exponentiation followed by a remainder | `5^3 mod 23 = 10` |
| `gcd(a,b)` | Greatest common divisor | `gcd(12,18) = 6` |
| `lcm(a,b)` | Least positive common multiple | `lcm(12,18) = 36` |
| `a^-1 mod p` | A value that multiplies a to 1 modulo p | `3^-1 mod 7 = 5` |

The inverse is not ordinary division.

We use it because `3 × 5 = 15`, and `15 mod 7 = 1`. An inverse exists only when the number and modulus are coprime.

In Python, `pow(a, b, p)` calculates modular exponentiation. For an invertible value, `pow(a, -1, p)` calculates the modular inverse.

Python's `^` means XOR, not exponentiation; `**` means exponentiation.

This distinction matters when copying a formula into code.

## What does an attacker get to do?

An attacker who only records traffic has less power than one who can:

- modify messages;
- submit chosen inputs;
- inspect memory;
- or control a signer.

Before examining an algorithm, complete this sentence:

```text
“We want to protect ___ from an attacker who can ___, for ___, assuming ___ remains trustworthy.”
```

For example: “We want to protect archived trade instructions from someone who steals the storage database, for seven years, assuming they cannot also obtain the independent decryption key.”

Now the review has a boundary.

If the database backup contains that key, the example fails its own assumption.

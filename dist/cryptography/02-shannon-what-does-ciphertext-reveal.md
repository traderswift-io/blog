---
title: Shannon: what does ciphertext reveal?
description: Perfect secrecy, why key length matters, and what reusing a key gives away.
order: 2
---

**The question:** What does observing the ciphertext tell an attacker, even if computation is unlimited?

## What is perfect secrecy?

Perfect secrecy means that seeing the ciphertext does not change the probability of any possible plaintext.

If the attacker thought a message was 70% likely before interception, the ciphertext does not move that probability. This is stronger than making recovery expensive. [1]

For plaintext M and ciphertext C, the condition is:

`P(M = m | C = c) = P(M = m)`

for every applicable message and ciphertext with nonzero ciphertext probability.

Let's take a two-bit message and a uniformly random two-bit key. Encrypt by XOR.

| Possible message | Key that produces ciphertext 10 |
| --- | --- |
| 00 | 10 |
| 01 | 11 |
| 10 | 00 |
| 11 | 01 |

Every message has exactly one equally likely key that could have produced `10`.

The ciphertext gives us no reason to prefer one message over another.

Notice what the table does not say. It does not make the messages equally likely if they were not equally likely before.

It preserves the attacker's prior uncertainty.

## Why does key length matter?

For perfectly secret, correctly decryptable encryption, key entropy must be at least message entropy.

To encrypt arbitrary n-bit messages with a one-time pad, we need n independent, uniformly random secret key bits, used once. A short seed expanded into a long stream does not meet that requirement. [1, 2]

Suppose we use a 128-bit seed to generate a one-megabyte stream. The stream occupies far more than 128 bits, but there are at most `2^128` possible streams.

A longer representation has not created more uncertainty about which stream was chosen.

This can still be useful computational security.

The claim is now that a feasible attacker cannot distinguish or recover the stream under the generator's assumptions. It is not perfect secrecy. [2]

A similar issue appears with passwords. Padding a six-digit PIN to 32 bytes does not give it 256 bits of entropy.

There are only one million possible PINs if all six-digit values are allowed.

Their maximum entropy is approximately `log2(1,000,000) = 19.93` bits, before accounting for human selection bias.

## What does depth mean here?

Depth refers to messages encrypted with the same or related cipher state in a way that lets an attacker compare them.

For a reused XOR pad S:

`C1 = M1 XOR S`

`C2 = M2 XOR S`

Therefore:

`C1 XOR C2 = M1 XOR M2`

The secret stream cancels. We have learned a relationship between messages without finding the key.

Use a one-byte example:

| Item | Hexadecimal value |
| --- | --- |
| First plaintext, A | 41 |
| Second plaintext, B | 42 |
| Shared pad | AA |
| First ciphertext | EB |
| Second ciphertext | E8 |
| Ciphertext XOR | 03 |

If we know the first plaintext was `41`, we recover the second as `03 XOR 41 = 42`.

This recovers the overlapping reused stream, not every unrelated key in the system.

Here is the lab. It is also in [the labs file](../assets/cryptography/Cryptography_Practical_Labs.py), so you can run it on your own computer.

```python
def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def xor_equal(left: bytes, right: bytes) -> bytes:
    if len(left) != len(right):
        raise ValueError("This lab requires equal lengths")
    return bytes(a ^ b for a, b in zip(left, right))


# Fixed public toy data. Never use this pad to protect a real secret.
m1, m2, pad = b"A", b"B", bytes.fromhex("aa")
c1, c2 = xor_equal(m1, pad), xor_equal(m2, pad)
recovered = xor_equal(xor_equal(c1, c2), m1)
check(recovered == m2, "Known plaintext must reveal the reused byte")
check((c1.hex(), c2.hex()) == ("eb", "e8"), "Guide values")
print("1 XOR reuse: ciphertexts eb/e8; recovered B")
```

Modern stream ciphers can be used securely for many messages with one key when their nonce and usage requirements are satisfied. Reusing the same key-and-nonce combination can recreate the relevant stream.

“One-time” describes the pad or stream position, not a blanket rule to discard every modern key after one message.

## What is unicity distance?

Unicity distance estimates how much ciphertext is needed before language redundancy may leave roughly one plausible key under a model.

A common approximation is `U ≈ H(K) / D`, where H(K) is key entropy in bits and D is plaintext redundancy in bits per symbol. It is a model-dependent estimate, not an algorithm or a runtime prediction. [1]

Suppose a toy cipher has 40 bits of key entropy and its messages have an assumed redundancy of 2 bits per character. The estimate is 20 characters.

It does not mean that a 20-character ciphertext can be broken quickly, that every message becomes unique at character 20, or that the model applies to an arbitrary modern construction.

This is why “Shannon ignores runtime” is useful for this review perspective.

First ask whether the information identifies the answer. Then ask whether anyone can calculate it.

## What should I check?

Ask where uncertainty comes from, how it is measured, and whether the same secret state is reused.

Separate the content claim from metadata: an encrypted message may still reveal its length, timing and destination.

**Try it:** A product describes a deterministic 32-byte expansion of a four-digit PIN as a 256-bit key. Explain the gap between output length and search space.

The answer is in [chapter 13](13-what-are-the-exercises-and-answers.html).

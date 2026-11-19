---
title: Rivest: why is raw RSA not a scheme?
description: Why the bare RSA formula is not enough to encrypt or sign, and what to use instead.
order: 7
---

**The question:** Are we using a complete encryption or signature scheme, or only the underlying mathematical operation?

## What does textbook RSA do?

At its core, RSA maps an integer m to `c = m^e mod n`.

The private exponent reverses that operation for valid keys and representatives. The original RSA paper supplies the mathematical foundation.

A real encryption scheme adds encoding and security rules; a signature scheme has its own encoding and verification rules. [32, 19]

Use our toy key:

- p = 61
- q = 53
- n = 3233
- e = 17
- d = 413

For m = 65:

`65^17 mod 3233 = 2790`

`2790^413 mod 3233 = 65`

The round trip works. That is a correctness result.

Now let's see why it is not an adequate encryption design.

## Why is deterministic encryption a problem?

Suppose the only possible messages are BUY and SELL, represented by known integers.

Anyone with the public key can encrypt both and compare the results with the observed ciphertext.

No private-key recovery is required. A successful round-trip test did not test confidentiality against this attack.

Textbook RSA is also multiplicative. Starting with ciphertext c, an attacker can calculate:

`c_prime = c × r^e mod n`

The decrypted result is `m × r mod n`.

With our numbers and r = 2, `c_prime = 3017`, which decrypts to 130. We changed the plaintext in a predictable way without knowing d.

For raw signatures, selecting any number s and defining `m = s^e mod n` produces a pair that passes the bare verification equation.

This is not necessarily a forgery of a meaningful, chosen application message, but it demonstrates why arbitrary representatives and a verification equation do not constitute a complete signature scheme.

Here is the lab. Press Run to try it in your browser.

Its last check is the shared-prime failure from [chapter 9](09-adleman-how-do-we-check-the-arithmetic.html).

```python run
from math import gcd, lcm


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


p, q, e, message = 61, 53, 17, 65
n = p * q
lam = lcm(p - 1, q - 1)
private_d = pow(e, -1, lam)
ciphertext = pow(message, e, n)
check((lam, private_d, ciphertext) == (780, 413, 2790), "Guide RSA values")
check(pow(ciphertext, private_d, n) == message, "Round trip")
changed = ciphertext * pow(2, e, n) % n
check(changed == 3017, "Changed ciphertext")
check(pow(changed, private_d, n) == 130, "Raw RSA is malleable")
check(pow(message, e, n) == ciphertext, "Raw RSA is deterministic")
check(gcd(n, 61 * 47) == 61, "Shared-prime failure")
print("4 Raw RSA: 65 -> 2790 -> 65; modified ciphertext -> 130")
```

## What should we use instead?

For RSA encryption, use a defined scheme such as RSA-OAEP through a maintained library. For new RSA signature applications, use an appropriate RSA-PSS profile.

Specify the hash, mask-generation function and the applicable salt or label rules so implementations agree. These choices are part of the scheme, not cosmetic padding settings. [15, 19]

RSA-OAEP has a message-size limit: `k - 2*hLen - 2` bytes, where k is modulus length in bytes and hLen is the hash output length. [15]

For a 3,072-bit modulus and SHA-256, that is `384 - 64 - 2 = 318` bytes. It is not suitable for directly encrypting an arbitrary large file.

A hybrid design can protect a small randomly generated data key with a public-key scheme and protect the file with AEAD.

The full envelope still needs authenticated metadata, key identification and a specified format.

An implementation must also avoid giving attackers distinguishable padding-error paths.

A generic external error message alone is insufficient if timing or other behavior still distinguishes the internal failures. [15]

## Why are RC4 and MD5 retired?

RC4 has exploitable statistical weaknesses; RFC 7465 prohibits negotiating RC4 cipher suites in TLS. Do not select it for a new design. [20]

MD5's collision resistance is broken. It is unsuitable for uses that require collision resistance, including ordinary signature hashing.

This does not mean that every MD5 digest reveals its input or that an MD5 collision instantly recovers an HMAC key.

RFC 6151 distinguishes these properties and advises against HMAC-MD5 in new protocol designs. [21]

For a migration, identify the actual use.

Replacing these may require four different changes:

- a file identifier;
- a signed digest;
- a password hash;
- a MAC.

Keep compatibility handling explicit so old formats cannot silently downgrade new operations.

## How can I test a real scheme?

For randomized encryption, encrypt the same plaintext twice and check that both decrypt correctly. Then alter the ciphertext and require rejection.

For a signature, alter the message, use the wrong public key and vary the declared parameters; each mismatch should fail under the chosen profile.

These tests can find mistakes. They do not establish a security proof or show that the library is free of side channels.

**Try it:** An RSA implementation passes 10,000 encrypt-decrypt tests. Explain why that evidence does not rule out the BUY-versus-SELL attack.

---
title: Shamir: which threshold really applies?
description: How a secret is split into pieces, and how to count the people an attacker really needs to reach.
order: 8
---

**The question:** How many independently controlled pieces are actually necessary to recover the secret or produce an accepted signature?

## How does secret sharing work?

In a t-of-n Shamir scheme, put the secret at the constant term of a polynomial with t coefficients over a finite field.

Choose the remaining coefficients independently and uniformly at random. Give each participant the polynomial value at a different, nonzero x-coordinate.

Any t shares reconstruct the secret; fewer than t disclose no information about it under the scheme's assumptions. [22]

Let's create a 3-of-5 example over the prime field modulo 257:

`f(x) = 42 + 17x + 9x^2 mod 257`

The secret is `f(0) = 42`.

| Participant coordinate | Share value |
| --- | --- |
| 1 | 68 |
| 2 | 112 |
| 3 | 174 |
| 4 | 254 |
| 5 | 95 |

These coefficients are fixed only so the example is reproducible. Real sharing requires the specified secure randomness.

Using the first three shares, the interpolation weights at zero are 3, -3 and 1:

`secret = (3 × 68 - 3 × 112 + 174) mod 257 = 42`

This is Lagrange interpolation. The companion lab reconstructs from every three-share combination, not only this convenient one.

## Why do two shares not identify the secret?

Keep only `(1,68)` and `(2,112)`. Both of these polynomials match them:

`42 + 17x + 9x^2 mod 257`

`99 + 60x + 166x^2 mod 257`

The first has secret 42. The second has secret 99.

We can do the same for every candidate constant in the field. With uniform random coefficients, these observations do not favor one candidate secret over another.

This is a statement about the shares.

It does not erase information from:

- an external checksum;
- a public key;
- a leaked coefficient;
- a predictable secret.

If somebody publishes a way to test guesses of a low-entropy secret, examine that separate leakage channel.

Here is the lab. It is also in [the labs file](../assets/cryptography/Cryptography_Practical_Labs.py), so you can run it on your own computer.

```python
from itertools import combinations
from typing import TypeAlias

Share: TypeAlias = tuple[int, int]


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def interpolate_zero(shares: tuple[Share, ...], prime: int) -> int:
    # Generic interpolation only. Does not know or enforce a threshold.
    # This deliberately makes the difference from an API refusal visible.
    xs = [x for x, _ in shares]
    if not shares or len(set(xs)) != len(xs):
        raise ValueError("Shares must have distinct coordinates")
    if any(not 0 < x < prime or not 0 <= y < prime for x, y in shares):
        raise ValueError("Invalid coordinate or value")
    result = 0
    for i, (xi, yi) in enumerate(shares):
        weight = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                weight = weight * (-xj) * pow((xi - xj) % prime, -1, prime) % prime
        result = (result + yi * weight) % prime
    return result


prime, secret = 257, 42
# Fixed coefficients for explanation only, not random secret sharing.
shares: tuple[Share, ...] = tuple(
    (x, (secret + 17 * x + 9 * x * x) % prime) for x in range(1, 6)
)
check(shares == ((1, 68), (2, 112), (3, 174), (4, 254), (5, 95)),
      "Guide share values")
triples = list(combinations(shares, 3))
check(len(triples) == 10, "All triples counted")
for triple in triples:
    check(interpolate_zero(triple, prime) == secret, "Each triple reconstructs")
# For the selected pair, construct a quadratic for EVERY candidate secret.
# This is stronger evidence than a library merely refusing two shares.
for candidate in range(prime):
    a2 = ((112 - candidate) - 2 * (68 - candidate)) * pow(2, -1, prime) % prime
    a1 = (68 - candidate - a2) % prime
    check((candidate + a1 + a2) % prime == 68, "First observed share")
    check((candidate + 2 * a1 + 4 * a2) % prime == 112, "Second observed share")
try:
    interpolate_zero((shares[0], shares[0], shares[2]), prime)
except ValueError:
    pass
else:
    raise AssertionError("Duplicate coordinates must be rejected")
print("5 Shamir: 10 triples recover 42; 257 secrets fit the selected pair")
```

## Does secret sharing give us threshold signing?

Not automatically.

| Design | What happens during use | Trust consequence |
| --- | --- | --- |
| Secret sharing with reconstruction | Enough shares are combined into a full key | The reconstruction environment can access the key |
| Threshold signing | Participants jointly produce a signature from shares | Security depends on the exact distributed protocol and its assumptions |
| Multisignature | A verifier requires several signatures from separate keys | The verification policy must enforce the intended combination |
| Approval workflow | A service checks approval records before using a full key | The service holding the key may remain able to bypass approvals |

FROST is an example of a specified threshold Schnorr protocol.

Its participants must manage one-time signing nonces, authenticate protocol communication and follow the selected ciphersuite. Its key-generation assumptions also matter.

FROST is not a generic threshold ECDSA implementation that can be substituted into any signature interface. [24]

## How does a claimed threshold become misleading?

Imagine a 2-of-3 service with shares on three machines. One cloud administrator can snapshot all three.

There are three stored shares, but only one administrative compromise may be needed to collect them.

Or the online path needs two participants, while a recovery endpoint can reconstruct the full key using one operator's credential.

The smallest sufficient recovery path determines the effective security boundary.

For every route to an accepted signature, count the independent authorities an attacker must compromise.

Include:

- deployment credentials;
- backups;
- recovery material;
- permissions to change the policy.

A software process is not necessarily an independent authority.

## How can I check the implementation?

For a t-of-n reconstruction scheme, verify:

- the intended coefficient count;
- field arithmetic;
- unique nonzero coordinates;
- share validation.

A constant polynomial exposes the secret in every share. A linear polynomial gives a two-share reconstruction threshold regardless of a configuration label saying three.

For a purported 2-of-3 service, test each pair, each singleton and duplicate use of one participant. Then repeat through recovery and maintenance routes.

If the service reconstructs the key, inspect where it exists afterward and whether logs, crash dumps or caches retain it.

Merely returning an error when fewer than t shares are supplied does not demonstrate secrecy: an implementation can refuse while the provided data already reveals the secret.

The underlying mathematics and generated shares must support the claim.

Incorrect or malicious shares require additional handling.

Basic secret sharing alone does not authenticate participants or guarantee consistent shares; verifiable sharing and protocol-specific checks address those problems.

Availability is another question: a threshold can prevent unauthorized signing while still allowing participants to halt progress. [22, 24]

**Try it:** A dashboard requires two approvals, but the signing process holds the complete private key.

What exactly is being enforced by the dashboard, and what can a compromised signing process bypass?

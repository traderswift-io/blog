---
title: Adleman: how do we check the arithmetic?
description: How an RSA key is built, why a faster shortcut needs a check, and what one bad output gives away.
order: 9
---

**The question:** Were the key's mathematical conditions satisfied, and can a faulty result leave the signer?

## Where do primes and lambda enter RSA?

For two-prime RSA, start with distinct suitable primes p and q.

Set `n = p × q` and `lambda(n) = lcm(p - 1, q - 1)`. Choose e coprime to lambda(n), then choose d so `e × d = 1 mod lambda(n)`.

RFC 8017 gives these key conditions. [15]

For our example:

| Quantity | Value |
| --- | --- |
| p and q | 61 and 53 |
| n | 3233 |
| phi(n) | 60 × 52 = 3120 |
| lambda(n) | lcm(60,52) = 780 |
| e | 17 |
| d | 413 |
| Check | 17 × 413 = 7021 = 1 mod 780 |

You may have seen d = 2753 for the same p, q and e. That value is the inverse modulo phi(n) and is also congruent to 413 modulo lambda(n).

Both satisfy the required relationship. The displayed private exponent is not necessarily unique across equivalent representations.

Prime generation is an implementation task with specified randomness, size, testing and acceptance conditions.

Use a vetted key-generation implementation and the relevant profile; FIPS 186-5 describes RSA signature key-generation requirements and has published errata to consult. [25]

Choosing distinct primes is essential. If two public moduli share a prime, their greatest common divisor can reveal it.

For example, `n1 = 61 × 53` and `n2 = 61 × 47` have gcd 61. A shared generation failure can therefore compromise more than one key.

## Why use the Chinese remainder theorem?

CRT computes the private operation modulo p and modulo q separately, then recombines the results.

Working with smaller numbers is faster.

For a signature operation on an encoded representative m:

`dP = d mod (p - 1)`

`dQ = d mod (q - 1)`

`sP = m^dP mod p`

`sQ = m^dQ mod q`

With `qInv = q^-1 mod p`, recombine:

`h = qInv × (sP - sQ) mod p`

`s = sQ + q × h`

The result has the required residue modulo each prime.

In a real RSA signature, m is the scheme's encoded representative, not an arbitrary message integer.

## Why check the result before release?

Suppose one branch is faulty. The output may remain correct modulo q but become wrong modulo p.

Under the relevant conditions, a faulty signature and the known representative allow an attacker to recover a factor using `gcd(s_fault^e - m, n)`.

Fault attacks against CRT RSA are established in the work of Boneh, DeMillo and Lipton. [26]

Our example makes this visible. With m = 65, the correct signature representative is 588.

Change the p-branch residue from 39 to 40 before recombination. The faulty result is 2602.

`gcd(2602^17 - 65, 3233) = 53`

One defective output has exposed a factor.

The lab uses modular exponentiation to keep the intermediate calculation small; subtracting m after reducing modulo n gives the same gcd with n.

Here is the lab. It is also in [the labs file](../assets/cryptography/Cryptography_Practical_Labs.py), so you can run it on your own computer.

```python
from math import gcd, lcm


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


p, q, e, representative = 61, 53, 17, 65
n = p * q
private_d = pow(e, -1, lcm(p - 1, q - 1))
sp = pow(representative, private_d % (p - 1), p)
sq = pow(representative, private_d % (q - 1), q)
qinv = pow(q, -1, p)
signature = sq + q * ((qinv * (sp - sq)) % p)
faulty = sq + q * ((qinv * ((sp + 1) - sq)) % p)
check(signature == 588 and faulty == 2602, "Guide CRT values")
check(pow(signature, e, n) == representative, "Good result verifies")
check(pow(faulty, e, n) != representative, "Faulty result must not be released")
factor = gcd(pow(faulty, e, n) - representative, n)
check(factor == 53, "Fault reveals a prime factor")
print("6 CRT fault: bad result 2602 reveals factor 53; verification rejects")
```

Before releasing s, check `s^e mod n == m`.

For decryption, the corresponding check compares re-encryption of the recovered representative with the input ciphertext before releasing the decoded plaintext. The implementation must place checks at the right boundary and fail closed. [26]

This check is a defense against a defined fault model. It is not a complete answer to every physical attack: a stronger attacker might fault the check itself.

Blinding, constant-time arithmetic and fault defenses address different issues and need separate evaluation.

## What should I look for in code?

Trace private-key use through the actual library or hardware boundary.

Determine whether output verification occurs there and whether an error can still return partial or stale output.

An application-level successful round trip does not establish that the private operation has this defense internally.

**Try it:** A signer notices that a CRT result is inconsistent, writes a warning, and returns the result anyway. Explain why the warning does not contain the failure.

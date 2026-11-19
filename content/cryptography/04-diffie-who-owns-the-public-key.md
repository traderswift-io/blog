---
title: Diffie: who owns the public key?
description: How two parties agree a secret in public, and why each public value must be tied to the right name.
order: 4
---

**The question:** How do parties establish a secret, and what binds the public values to the identities they intended to contact?

## How can two parties agree on a secret in public?

Diffie-Hellman lets two parties combine private values and exchanged public values to calculate a shared secret.

An observer sees the public exchange, while the intended hardness assumption concerns calculating the shared result without either private value. [6]

Let's use deliberately insecure small numbers:

| Step | Alice | Bob |
| --- | --- | --- |
| Public parameters | p = 23, g = 5 | p = 23, g = 5 |
| Private exponent | a = 6 | b = 15 |
| Public value | A = 5^6 mod 23 = 8 | B = 5^15 mod 23 = 19 |
| Shared result | B^a mod 23 = 2 | A^b mod 23 = 2 |

Both calculations produce `g^(ab) mod p`. The parties do not send the shared result over the connection.

Why does that help? With large, appropriate parameters, calculating the public value is designed to be practical while recovering the private exponent is believed hard.

With p = 23, we can simply try the possible exponents. These numbers illustrate equality, not security.

Here is the lab. Press Run to try it in your browser.

Its last check uses the bad generator from [the next chapter](05-hellman-what-makes-the-problem-hard.html).

```python run
def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


p, g, a, b = 23, 5, 6, 15
public_a, public_b = pow(g, a, p), pow(g, b, p)
secret_a, secret_b = pow(public_b, a, p), pow(public_a, b, p)
check((public_a, public_b, secret_a, secret_b) == (8, 19, 2, 2),
      "Guide DH values")
check({pow(p - 1, x, p) for x in range(1, p)} == {1, p - 1},
      "The bad generator has only two possible outputs")
print("2 DH: public values 8/19; shared result 2; bad group size 2")
```

## What happens if someone replaces the public value?

Alice receives a number and assumes it belongs to Bob.

An attacker sends their own number instead, performs one exchange with Alice and another with Bob, and relays messages between them.

Alice has a shared secret with the attacker. Bob has a different shared secret with the attacker.

The arithmetic is working correctly on both connections.

We therefore need authentication of the exchange. A public value is not a verified identity merely because it is public, long or difficult to generate.

## How do we bind a key to a name?

There are several trust models. A certificate can bind a key to an identity through a trusted issuer.

A pinned key can be distributed through an already trusted channel.

Trust on first use remembers the initial key, but that first contact remains a security assumption.

For TLS, checking that a certificate has a valid signature is not enough. The application must also verify that the certificate identifies the intended service.

RFC 9525 defines service-identity checking; the expected name must come from the client's intended destination, not from the untrusted certificate itself. [7]

For example, a valid certificate for `example.net` does not authenticate a connection intended for `orders.example.com`.

A self-signed certificate proves that somebody controlling a private key signed it. Without an independent trust decision, that tells us nothing about whether they own the name printed in it.

## What else belongs in the binding?

In a real protocol, the authenticated transcript needs to cover the relevant exchange, roles and negotiated choices so that a message cannot change meaning unnoticed.

TLS 1.3's CertificateVerify and Finished messages authenticate different parts of this process. Use the protocol's full verification rules rather than assembling a handshake from separate signature and DH calls. [5]

After key agreement, a KDF derives keys for particular uses.

HKDF's context input can separate roles such as sending and receiving, protocol versions and purposes. It does not authenticate a peer by itself, and it does not turn a guessable input into a high-entropy secret. [8]

For an agent service, keep three records distinct: which key authenticated, which owner enrolled it, and which operations that owner authorized.

A valid request from an enrolled agent may still exceed its trading limit.

**Try it:** A service publishes a key at `/public-key`, over a connection whose certificate is not verified.

The client downloads it and verifies every later signature correctly. Identify the missing trust step.

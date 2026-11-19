---
title: What does a complete review look like?
description: A practice review of a made-up signing service with nine flaws, then what we should find.
order: 11
---

Here is a fictional signing and messaging service.

These statements are deliberately flawed; they describe no particular product.

## What are we reviewing?

1. The service calls a 32-byte hash of a six-digit PIN a “256-bit secret.”
2. Two encryption workers share one AES-GCM key. Each resets its nonce counter to zero on restart.
3. The client downloads a public key over a connection with certificate checking disabled.
4. The DH modulus is large, but the generator is p - 1.
5. Requests use `SHA256(secret || request)` as authentication. Audit records have Merkle proofs against roots returned by the same server without authentication.
6. The RSA endpoint encrypts the integer representation of each command directly. Its compatibility mode allows RC4 and MD5-based signatures.
7. A dashboard advertises 2-of-3 signing, but one process holds the full key and checks two approval rows in its database.
8. The RSA module recombines CRT results without verifying them before return.
9. Debug logs contain private-key material. Valid requests can be executed repeatedly.

Before reading on, write one finding for each numbered item.

Include the violated claim, a concrete observation or test, and what a suitable repair must accomplish.

## What should we find?

| Perspective | Finding | Evidence to request |
| --- | --- | --- |
| Shannon | The output size overstates the PIN's uncertainty | Key-generation path and the PIN candidate space |
| Turing | Restarts and multiple workers reuse stream state | Concurrent and post-restore nonce traces for the same key ID |
| Diffie | A substituted key can pass every later verification | A test with an untrusted certificate or wrong service identity |
| Hellman | The generator confines values to a two-element group | Parameter inspection and enumeration of its powers |
| Merkle | The MAC construction permits extension; roots lack a trust anchor | Parser behavior and authenticated root-distribution design |
| Rivest | Raw deterministic RSA leaks low-entropy commands; legacy choices are unsafe | Exact scheme API, parameters and downgrade behavior |
| Shamir | The process can bypass the approval threshold | Full-key custody and direct signing-path access |
| Adleman | Faulty CRT output may disclose a factor | Fault-injection test and the release-boundary verification |
| Schneier | Logs expose keys; valid requests can replay | Canary-secret searches and concurrent duplicate-request tests |

The suitable repair is often architectural.

Renaming the PIN hash, adding another approval button or changing a log level does not establish the property originally claimed.

For nonce reuse, establish a lifecycle that prevents repeat allocations under a key, including restore and multi-worker cases.

For identity, anchor the key in a verified enrollment or certificate process.

For the threshold, either implement a suitable distributed scheme with independent custody or describe the product honestly as centralized signing with approvals.

## What would a useful final finding look like?

“The documented 2-of-3 property applies to the dashboard approval workflow. In the reviewed configuration, process S holds the full signing key and can produce a signature without either approval service.

This was demonstrated by invoking the local signing path in an isolated test. The receiving verifier accepted the resulting signature.

Therefore the implementation does not establish a cryptographic two-party signing requirement.”

That finding is more useful than “threshold security is weak.”

It names the boundary, the evidence and the limitation without claiming to have tested unrelated deployments.

## How should we make the decision?

Use explicit statuses:

- demonstrated;
- contradicted;
- untested;
- outside scope.

Keep “code exists,” “tests passed” and “deployed behavior verified” as different records.

For this fictional service, accepting all nine claims would be unjustified.

The sensible next step is to stop relying on the failed claims, repair the affected paths, and retest the intended properties. A clean unit-test run cannot turn an untested recovery route into verified security.

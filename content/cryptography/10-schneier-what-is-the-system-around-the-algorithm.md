---
title: Schneier: what is the system around the algorithm?
description: How an attacker reaches a secret without breaking the mathematics, and how to check the parts around it.
order: 10
---

**The question:** How can the attacker reach the asset without solving the mathematical problem?

Schneier's writing on security emphasizes the continuing operational process around protective products.

For this guide, we turn that perspective into a concrete exercise: follow the key, the message and the permission check across the whole application. [30]

## Why is an algorithm name insufficient?

“We use AES-256” leaves several questions unanswered:

- Which mode?
- How are nonces allocated?
- Is the ciphertext authenticated?
- Who has the key?
- Can a caller ask the service to decrypt arbitrary data?
- What becomes visible when authentication fails?

Prefer a complete authenticated-encryption interface for application data.

AEAD takes a key, nonce, plaintext and associated data; authenticated decryption returns plaintext or failure. Associated data is protected against modification but remains visible. [23]

For our order example, the encrypted body might hold order details while associated data binds a protocol version and account identifier.

The receiver must check that the authenticated account is the intended account. Authenticating a field does not make its value authorized.

## What does the mode change?

| Construction | What to understand before use |
| --- | --- |
| AES-ECB | Equal plaintext blocks produce equal ciphertext blocks under one key; it is unsuitable for general message confidentiality |
| AES-CBC without authentication | Encryption alone does not detect malicious modification; IV and padding behavior also matter |
| AES-CTR without authentication | Repeated counter streams expose plaintext relationships; bit changes are malleable |
| AES-GCM | AEAD with strict nonce and usage requirements; nonce reuse can compromise confidentiality and authentication |
| ChaCha20-Poly1305 | AEAD with a 96-bit nonce in the IETF construction; the nonce must not repeat for a key |

The basic confidentiality modes are specified in SP 800-38A. GCM and ChaCha20-Poly1305 have their own bounds and nonce rules.

Follow the selected protocol and library profile rather than treating “AEAD” as permission for unlimited use of a key. [27, 31, 35]

## How should I think about nonce allocation?

A counter gives deterministic uniqueness only if its state and allocation rules are correct.

Multiple workers need separate ranges or an allocation mechanism that prevents overlap. A restored backup must not resume an old counter under a key that has already used those values.

RFC 5116 explicitly discusses multiple devices and state surviving restarts. [23]

Random nonces give a probability of uniqueness. For q independent uniform 96-bit nonces, the small-probability approximation is:

`P(collision) ≈ q(q - 1) / 2^97`

At `q = 2^32`, that is about `2^-33`.

This calculation is not a recommended invocation limit. These also matter:

- message sizes;
- forgery bounds;
- the number of systems sharing a key;
- the protocol profile.

A useful review asks for the nonce allocator's behavior under concurrency and recovery, not a screenshot of two different values from a happy-path test.

## What does constant time mean for a tag?

An early-exit byte comparison can reveal how much of a proposed tag matches through timing.

For a standalone HMAC in Python, use `hmac.compare_digest` on appropriately validated, fixed-format values.

Its purpose is to avoid content-dependent short-circuiting; it does not promise to hide public input lengths or make the surrounding program constant-time. [33]

Here is the lab. Press Run to try it in your browser.

```python run
from hmac import compare_digest, digest
from secrets import token_bytes


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


key = token_bytes(32)
message = b"guide-demo:v1:request=123:account=7:buy=10"
tag = digest(key, message, "sha256")
check(compare_digest(tag, digest(key, message, "sha256")), "HMAC matches")
modified = b"guide-demo:v1:request=123:account=7:buy=100"
check(not compare_digest(tag, digest(key, modified, "sha256")), "Changed message fails")
print("8 HMAC: original verifies; changed message fails")
```

For AEAD, let the cryptographic library verify its tag. Do not manually compare part of the tag or expose plaintext before verification succeeds.

Use the specified tag length; truncation changes the security analysis.

Also inspect the behavior around the check. A constant-time comparison followed by distinguishable error paths can still leak information.

A quick local timing test is useful for finding gross mistakes, but does not prove resistance to side channels.

## Where does the key get printed?

Search the full lifecycle:

- configuration dumps;
- debug logs;
- exception traces;
- command-line arguments;
- support bundles;
- crash dumps;
- telemetry;
- backups.

An encrypted key file offers limited help if its unlocking credential is stored next to it and the same attacker can read both.

For a test environment, use a deliberately generated canary secret and check whether it appears in those outputs.

Do not copy a real production key into a search command or report. Redaction should prevent exposure at the source, not merely hide one field in the dashboard after it has already been collected.

A hardware boundary or remote signer changes which actions are possible; it does not automatically constrain the use of the key.

If an attacker can ask the signer to authorize arbitrary operations, preventing key export has not prevented misuse.

## How do I prevent replay?

An old valid ciphertext still has a valid tag.

Add authenticated request identifiers and an application policy for freshness. Then enforce that policy where the action is committed.

For an order service, the check and execution reservation need to handle concurrent delivery. Two workers can both see “request not used” before either records it.

A durable, atomic reservation or a protocol-specific equivalent is necessary. Time windows also need clock and retry rules.

## Can we try authenticated encryption in Python?

The companion lab:

- generates a fresh AES-GCM key;
- encrypts one message;
- decrypts it;
- changes the ciphertext, nonce and associated data in separate tests.

Each altered input must fail authentication.

It then decrypts the unchanged message again to demonstrate that AEAD alone does not reject replay. The library documents these inputs and its `InvalidTag` behavior. [34]

Here is the lab. Press Run to try it in your browser.

```python run
from secrets import token_bytes

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


key = AESGCM.generate_key(bit_length=256)
cipher = AESGCM(key)
nonce = token_bytes(12)
aad = b"guide-demo:v1:account=7"
message = b"buy 10 units"
# Only one encryption invocation under this fresh key.
ciphertext = cipher.encrypt(nonce, message, aad)
check(cipher.decrypt(nonce, ciphertext, aad) == message, "AEAD round trip")
altered = bytes([ciphertext[0] ^ 1]) + ciphertext[1:]
wrong_nonce = bytes([nonce[0] ^ 1]) + nonce[1:]
for label, candidate_nonce, candidate_ct, candidate_aad in (
    ("ciphertext", nonce, altered, aad),
    ("nonce", wrong_nonce, ciphertext, aad),
    ("associated data", nonce, ciphertext, b"guide-demo:v1:account=8"),
):
    try:
        cipher.decrypt(candidate_nonce, candidate_ct, candidate_aad)
    except InvalidTag:
        pass
    else:
        raise AssertionError(f"Altered {label} should be rejected")
# Repeated DECRYPTION is intentional: AEAD itself has no replay state.
check(cipher.decrypt(nonce, ciphertext, aad) == message, "Replay still decrypts")
print("7 AEAD: 3 alterations rejected; unchanged replay still decrypts")
```

Run all the examples in a fresh virtual environment with Python 3.11 or later:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install cryptography==50.0.0
.venv/bin/python Cryptography_Practical_Labs.py
```

On Windows, use `.venv\Scripts\python` for the last two commands.

Version 50.0.0 is the version used to verify this tutorial; it is a reproducibility pin, not an instruction to keep a deployed service on that version indefinitely.

The final output should be:

```text
8 labs passed
```

The script makes no network calls and uses no account credentials.

It deliberately prints toy mathematical values, but does not print the randomly generated AEAD or HMAC keys.

**Try it:** An encrypted request authenticates correctly twice. What additional state or protocol rule is needed to stop the second execution?

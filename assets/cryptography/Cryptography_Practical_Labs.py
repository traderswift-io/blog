"""Eight local teaching labs for Cryptography A Practical Guide.

Python 3.11+; verified with cryptography 50.0.0.
These are educational demonstrations, not production cryptographic code.
No network calls, account credentials or external services are used.
"""

from hashlib import sha256
from hmac import compare_digest, digest
from itertools import combinations
from math import gcd, lcm
from secrets import token_bytes
from typing import TypeAlias

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

Share: TypeAlias = tuple[int, int]


def check(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def xor_equal(left: bytes, right: bytes) -> bytes:
    if len(left) != len(right):
        raise ValueError("This lab requires equal lengths")
    return bytes(a ^ b for a, b in zip(left, right))


def lab_xor_reuse() -> None:
    # Fixed public toy data. Never use this pad to protect a real secret.
    m1, m2, pad = b"A", b"B", bytes.fromhex("aa")
    c1, c2 = xor_equal(m1, pad), xor_equal(m2, pad)
    recovered = xor_equal(xor_equal(c1, c2), m1)
    check(recovered == m2, "Known plaintext must reveal the reused byte")
    check((c1.hex(), c2.hex()) == ("eb", "e8"), "Guide values")
    print("1 XOR reuse: ciphertexts eb/e8; recovered B")


def lab_diffie_hellman() -> None:
    p, g, a, b = 23, 5, 6, 15
    public_a, public_b = pow(g, a, p), pow(g, b, p)
    secret_a, secret_b = pow(public_b, a, p), pow(public_a, b, p)
    check((public_a, public_b, secret_a, secret_b) == (8, 19, 2, 2),
          "Guide DH values")
    check({pow(p - 1, x, p) for x in range(1, p)} == {1, p - 1},
          "The bad generator has only two possible outputs")
    print("2 DH: public values 8/19; shared result 2; bad group size 2")


def leaf(record: bytes) -> bytes:
    return sha256(b"\x00" + record).digest()


def node(left: bytes, right: bytes) -> bytes:
    if len(left) != 32 or len(right) != 32:
        raise ValueError("SHA-256 children must be 32 bytes")
    return sha256(b"\x01" + left + right).digest()


def lab_merkle() -> None:
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


def lab_raw_rsa() -> None:
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


def lab_shamir() -> None:
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


def lab_crt_fault() -> None:
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


def lab_aead() -> None:
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


def lab_hmac() -> None:
    key = token_bytes(32)
    message = b"guide-demo:v1:request=123:account=7:buy=10"
    tag = digest(key, message, "sha256")
    check(compare_digest(tag, digest(key, message, "sha256")), "HMAC matches")
    modified = b"guide-demo:v1:request=123:account=7:buy=100"
    check(not compare_digest(tag, digest(key, modified, "sha256")), "Changed message fails")
    print("8 HMAC: original verifies; changed message fails")


def main() -> None:
    for lab in (
        lab_xor_reuse, lab_diffie_hellman, lab_merkle, lab_raw_rsa,
        lab_shamir, lab_crt_fault, lab_aead, lab_hmac,
    ):
        lab()
    print("8 labs passed")


if __name__ == "__main__":
    main()

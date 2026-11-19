---
title: Sources
description: The papers, standards and documentation behind every chapter, with links.
order: 15
---

The explanations and small numerical exercises in this guide are original teaching material.

The following papers, specifications and official documentation support the definitions and implementation requirements.

Historical papers explain foundations; they are not current deployment instructions.

1. [Claude Shannon, Communication Theory of Secrecy Systems, 1949](https://pages.cs.wisc.edu/~rist/642-fall-2014/shannon-secrecy.pdf). Perfect secrecy, entropy and unicity; especially the sections on perfect secrecy and equivocation.
2. [Dan Boneh and Victor Shoup, A Graduate Course in Applied Cryptography, version 0.6](https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_6.pdf). Formal security definitions and further exercises.
3. [NIST, FIPS 186-5 Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final). Signature properties and algorithms. See also its errata.
4. [Alan Turing, Treatise on the Enigma, US National Archives copy](https://www.archives.gov/files/press/press-releases/2015/images/turing-enigma-treatise.pdf). Primary historical source for crib and depth analysis.
5. [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html). Sections 4.4 and E.1 cover handshake authentication and security properties, including 0-RTT limitations.
6. [Whitfield Diffie and Martin Hellman, New Directions in Cryptography, 1976](https://web.mit.edu/6.857/OldStuff/Fall03/ref/diffie76new.pdf). Public-key distribution and one-way-function foundations.
7. [RFC 9525, Service Identity in TLS](https://www.rfc-editor.org/rfc/rfc9525.html). Verification of the intended service identity.
8. [RFC 5869, HKDF](https://www.rfc-editor.org/rfc/rfc5869.html). Extract-and-expand derivation and context binding.
9. [NIST SP 800-56A Revision 3](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final). Discrete-logarithm key-establishment schemes and validation. Its publication page notes planned revision.
10. [RFC 7919, Negotiated Finite Field DH Parameters for TLS](https://www.rfc-editor.org/rfc/rfc7919.html). Named groups and peer-public-value validation.
11. [RFC 7748, Elliptic Curves for Security](https://www.rfc-editor.org/rfc/rfc7748.html). X25519 and X448 processing and security considerations.
12. [NIST SP 800-57 Part 1 Revision 5](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-57pt1r5.pdf). Table 2 compares conventional security strengths; key length alone is not a cross-algorithm comparison.
13. [NIST SP 800-107 Revision 1](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=911479). Hash security properties and generic strength distinctions. Used here for those mathematical distinctions, not as a claim about current compliance requirements.
14. [RFC 2104, HMAC](https://www.rfc-editor.org/rfc/rfc2104.html). The MAC construction; read with the later algorithm guidance in RFC 6151.
15. [RFC 8017, PKCS 1 version 2.2](https://www.rfc-editor.org/rfc/rfc8017.html). RSA key conditions, primitives, OAEP and PSS. Historical defaults in a specification are not a recommendation for new profiles.
16. [RFC 9162, Certificate Transparency version 2](https://www.rfc-editor.org/rfc/rfc9162.html). Section 2.1 specifies Merkle trees and proofs.
17. [RFC 9380, Hashing to Elliptic Curves](https://www.rfc-editor.org/rfc/rfc9380.html). Section 2.2.5 explains domain separation and injective encoding.
18. [RFC 6234, US Secure Hash Algorithms](https://www.rfc-editor.org/rfc/rfc6234.html). SHA-256 padding, chaining-state processing and digest output, which explain the length-extension mechanism.
19. [PyCA cryptography, RSA documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/). Scheme-level encryption and signature APIs and parameter guidance.
20. [RFC 7465, Prohibiting RC4 Cipher Suites](https://www.rfc-editor.org/rfc/rfc7465.html). TLS prohibition and supporting rationale.
21. [RFC 6151, MD5 and HMAC-MD5 Security Considerations](https://www.rfc-editor.org/rfc/rfc6151.html). Distinguishes collision failures from other security properties.
22. [Adi Shamir, How to Share a Secret, 1979](https://www.cs.tau.ac.il/research/benny.chor/Shamir.html). Threshold reconstruction and secrecy with insufficient shares.
23. [RFC 5116, An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html). AEAD interfaces and nonce generation across devices and restarts.
24. [RFC 9591, FROST](https://www.rfc-editor.org/rfc/rfc9591.html). Threshold Schnorr signing, nonce requirements, assumptions and trusted-dealer appendix.
25. [NIST FIPS 186-5, publication and errata](https://csrc.nist.gov/pubs/fips/186-5/final). RSA signature key generation and mathematical requirements; same publication as reference 3.
26. [Boneh, DeMillo and Lipton, On the importance of checking cryptographic protocols for faults](https://crypto.stanford.edu/~dabo/pubs/abstracts/faults.html). CRT RSA fault attack.
27. [NIST SP 800-38D, GCM and GMAC](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=51288). Nonce uniqueness, authentication and usage bounds. Consult the publication's revision status before using it as a compliance profile.
28. [NIST FIPS 202, SHA-3 Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf). Sponge-based hash construction and security properties.
29. [NIST FIPS 203, ML-KEM](https://csrc.nist.gov/pubs/fips/203/final). Post-quantum key encapsulation; consult the linked errata.
30. [Bruce Schneier, The Process of Security](https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html). Operational security perspective.
31. [RFC 8439, ChaCha20 and Poly1305](https://www.rfc-editor.org/rfc/rfc8439.html). AEAD construction, nonce requirements and security considerations.
32. [Rivest, Shamir and Adleman, A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://people.csail.mit.edu/rivest/Rsapaper.pdf). Original RSA mathematics.
33. [Python hmac documentation](https://docs.python.org/3/library/hmac.html). `compare_digest` behavior and its limitations.
34. [PyCA cryptography, authenticated encryption documentation](https://cryptography.io/en/latest/hazmat/primitives/aead/). AES-GCM API, nonce requirements and authentication-failure behavior.
35. [NIST SP 800-38A, Block Cipher Modes of Operation](https://csrc.nist.gov/pubs/sp/800/38/a/final). Definitions of ECB, CBC, CTR and other confidentiality modes.

The article structure and explanatory approach were informed by Jignesh Davda's [Binance Python API guide](https://algotrading101.com/learn/binance-python-api-guide/), [Interactive Brokers Python API guide](https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/) and [Backtrader guide](https://algotrading101.com/learn/backtrader-for-backtesting/). They are voice references, not sources for the cryptographic claims.

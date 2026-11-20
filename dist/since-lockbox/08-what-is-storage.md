---
title: What is Storage?
description: Where your files will live, with providers who cannot read them.
order: 8
---

Storage is where your files will live, kept by providers who cannot read them.

Your files are encrypted on your phone, so providers store only scrambled data they cannot open.

Storage is its own subnet chain, `storage-1`. The files stay outside the chain.

## How do we know a provider still has the file?

The chain holds commitments, small fingerprints of each file, and sends challenges. A provider proves it still holds a file by answering those challenges.

Why this helps you: you do not have to trust a provider's word that your data is safe, because the chain keeps asking.

## Where does it stand?

Storage is **Built, not live**.

On Wed 18 Nov 2026 a test chain passed a full round: a real challenge, an accepted proof, and four refusals that left the state untouched.

It is not a public network yet. It waits on the founding providers and on an outside review of the encryption.

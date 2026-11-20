---
title: How do I keep learning?
description: Five steps, from explaining the ideas without notes to writing a review someone else can repeat.
order: 14
---

Use milestones rather than a promise to become an expert in a fixed number of days.

**First, explain the properties without notes.** You should be able to distinguish:

- secrecy from computational cost;
- authentication from authorization;
- inclusion from truth;
- secret sharing from threshold signing.

If a term is doing too much work in your explanation, break it into separate claims.

**Next, reproduce the examples.** Change the toy messages and parameters.

Predict the output before running the code.

In the Shamir example, show why two points fit every possible secret. In the RSA example, derive the modified plaintext before decrypting it.

**Then, read a specification alongside an implementation.** Pick one narrow operation, such as AES-GCM decryption or RSA-PSS verification.

Map its input requirements, failure cases and parameter rules to the code path.

Use official test vectors as well as tests with invalid inputs. Record the exact versions you reviewed.

**After that, examine the operational boundary.** Trace keys and counters across:

- startup;
- backup;
- recovery;
- revocation.

Check who can alter the software or policy. Ask whether supposedly independent parties share one deployment account or recovery credential.

**Finally, write a review another person can reproduce.** Give them:

- the claim;
- assumptions;
- test inputs;
- expected result.

Let them challenge your conclusion.

Being able to find a flaw is useful; being able to explain the precise conditions under which it exists is the skill to keep developing.

For deeper study, work through the relevant exercises in Boneh and Shoup's *A Graduate Course in Applied Cryptography*, then return to the original papers and applicable standards.

Implementing a new primitive or distributed signing protocol calls for deeper cryptographic training and specialist review than using an existing, well-specified library interface.

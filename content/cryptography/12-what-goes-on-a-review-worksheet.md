---
title: What goes on a review worksheet?
description: A table to copy and fill in for each operation you review, with the tests to run against it.
order: 12
---

Copy this into a review document and fill it in for one operation at a time.

| Field | What to record |
| --- | --- |
| Operation | Exact action, caller, recipient and acceptance boundary |
| Asset and claim | What is protected, from whom, and for how long |
| Attacker access | Network, database, host, administrator, signer or physical access |
| Scheme and version | Complete construction, parameters, library version and profile |
| Identity | Enrollment, certificate or pin; rotation and revocation rules |
| Key custody | Generation, holders, copies, backups, recovery and deletion |
| Encoding | Exact authenticated bytes and parsing rules |
| State | Nonces, signing nonces, counters, request IDs and epochs |
| Threshold | Every sufficient set of authorities, including recovery |
| Failure behavior | Rejection boundary and whether partial output escapes |
| Evidence | Commit, configuration, command, input and observed output |
| Status | Demonstrated, contradicted, untested or outside scope |
| Next action | Specific change or test, with an owner |

For a negative test, describe what must fail.

Examples include:

- a wrong identity;
- repeated participant;
- malformed group element;
- altered associated data;
- replayed request;
- an injected CRT error.

For an operational test, include at least one state transition:

- restart;
- recovery;
- rotation;
- revocation;
- concurrent processing.

These transitions often expose assumptions that normal-operation tests leave untouched.

Keep the strength of the conclusion proportional to the evidence.

A passing test supports the tested behavior in that configuration. A proof supports a model under stated assumptions.

Neither automatically describes:

- a different build;
- hidden backup;
- changed policy;
- live deployment.

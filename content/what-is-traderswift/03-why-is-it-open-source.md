---
title: Why is TraderSwift open source?
description: If someone else's code manages your keys and your money, reading that code is the bare minimum.
order: 3
---

If a machine and code you don't control is managing your keys, your trading and your money, you should be able to read that code.

For me, open source is the bare minimum for that kind of trust.

## Why does it matter more now?

In the past, it mattered less, because not everybody could read code.

Today, anybody can point their own AI agent at a repository and ask it to check the code for anything malicious.

So open code is no longer only for programmers. It is for anyone with an agent.

## Can I check it myself?

Yes. Give this prompt to your own AI agent:

::: prompt
Read the repository at https://github.com/traderswift-io/signer. Tell me, in plain words, what the code does with a trading key. Check whether any code path could send a key, a key share or funds anywhere other than where the documentation says. List anything that looks unsafe, with the file and line. Do not run any of the code.
:::

## Am I tied to you?

No.

You can take part in the TraderSwift network, or fork the code and run it on your own, as a private network.

Both are open to you. The guides show how.

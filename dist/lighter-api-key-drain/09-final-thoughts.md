---
title: Final thoughts
description: Written limits around every trading key.
order: 9
---

The leaked key did nothing it wasn't allowed to do.

That is the point: everything it could do, it was allowed to do. And when it went wrong, the only control left was an exchange-wide halt that landed on everyone.

With Signer, the market maker writes down what its key may do, on chain, from how it actually trades.

A maker key that cannot cross the spread. A taker key that can, but only a little, only in liquid markets.

Trading carries on as normal for everyone else.

In our replay, the fields live today still let the attacker take almost everything they went for. With Policy v2 added, the most they moved was 0.3% to 0.9%.

That is a limit, not a wall: the attacker can still trade at the edge of the band until the owner revokes.

That is what we are building: not protection for one venue, but a defined policy around every trading key.

---
title: What would the attacker try next?
description: With only a trading key, the attacker has to move value by trading.
order: 4
---

With only a trading key, the attacker has to move value by trading.

The plausible route is to trade the victim's account against the attacker's own:

- **Pick a thin market.** An instrument with little depth, where the attacker can rest orders at bad prices.
- **Cross the spread from the victim's account.** Either one large market order into the attacker's resting orders, or many small ones to stay under any single-order limit.
- **Repeat until stopped.** Each fill moves a little value from the victim to the attacker.

This is the attack a policy has to stop. A market maker's own trading history says a lot about what that policy should be.

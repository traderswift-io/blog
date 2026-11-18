---
title: How did the money leave?
description: Five steps, with nothing but a trading key.
order: 3
---

A Lighter API key can trade.

It can also create pools, move funds between accounts with the same owner, and withdraw to the owner's own wallet.

Lighter's public account data shows the attacker used exactly that, with nothing but the victims' trading key:

1. **Close the positions.** Reduce-only orders closed both accounts' open positions, about $12.5 million and $8.9 million in notional.
2. **Open a pool in the victim's name.** A pool with a 0% fee and no minimum operator share, created inside each victim account.
3. **Buy the pool.** From their own account, the attacker bought 99.99% of each pool's shares, for about 9,999 USDC.
4. **Fill it from the victim.** Same-owner transfers moved 10.38 million and 5.09 million USDC into the pools. No wallet signature is needed between accounts with the same owner.
5. **Cash out.** The attacker burned the shares and withdrew 10,393,056.79 and 5,096,588.02 USDC to their own wallet.

The share burn is the step that crosses owners. A key that "can only withdraw to its owner" still moved about $15.5 million to someone else, without a single wallet signature.

Under Signer, the key could only ever be used to trade. A delegate may send trading requests only (orders, cancels and the timed cancel-all), and nothing else, so pool creation, transfers and share operations (steps 2 and 4) are refused by request type, before any policy field is read.

Step 1 is a trading request, and it is the one place the policy has to do the work: reduce-only orders close risk, so they are not size-capped, but they are limited to the markets the policy allows.

Signer never signs a transfer or a withdrawal. Moving funds stays with the owner's own wallet.

So the pool route closes. A real attacker would not stop there.

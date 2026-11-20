---
title: How did the money leave?
description: Five steps, with nothing but a trading key.
order: 3
---

A Lighter API key can trade.

It can also create pools, move funds between accounts with the same owner, and withdraw to the owner's own wallet ([Lighter docs](https://docs.lighter.xyz/developers/integration-guides/api-keys)).

Lighter's public account data and an on-chain analyst's breakdown show the attacker used exactly that, with nothing but the victims' trading key ([0xTria](https://x.com/0xTria/status/2122280548047671629)).

In step 1, a reduce-only order, also called close-only, is one that can only shrink a position, never grow it.

1. **Close the positions.** Reduce-only orders closed both accounts' open positions.
2. **Open a pool in the victim's name.** A pool with a 0% fee and no minimum operator share, created inside each victim account.
3. **Buy the pool.** From their own account, the attacker bought 99.99% of each pool's shares, for about 9,999 USDC.
4. **Fill it from the victim.** Same-owner transfers moved 10.38 million and 5.09 million USDC into the pools, with no wallet signature needed between same-owner accounts at the time ([Lighter docs](https://docs.lighter.xyz/developers/integration-guides/deposits-transfers-and-withdrawals)).
5. **Cash out.** The attacker burned the shares, handing them back to the pool for its cash, and requested withdrawals of 10,393,056.79 and 5,096,588.02 USDC to their own wallet; the first was paid out.

The share burn is the step that crosses owners.

A key that "can only withdraw to its owner" still moved about $10.4 million to someone else, and tried for $5.1 million more, without a single wallet signature.

## What would Signer have refused?

Signer is our signing network. Its signers are machines that each hold a part of a trading key, and they sign only what a written set of limits, the policy, allows.

The policy sits on Signer's chain, a shared record that every signer reads and anyone can check. When we say "on chain", we mean on that record.

Under Signer, the key could only ever be used to trade.

The trading key the owner hands out is called a delegate. A delegate may send three kinds of request: orders, cancels and the timed cancel-all.

Anything else is refused by its request type, before any policy field is read. So pool creation, transfers and share operations (steps 2 and 4) are never signed.

Step 1 is a trading request, and it is the one place the policy has to do the work.

Close-only orders reduce risk, so they are not size-capped. They are still limited to the markets the policy allows.

Signer never signs a transfer or a withdrawal. Moving funds stays with the owner's own wallet.

Lighter has since closed this route on its side: transfers into public pools now need a wallet signature ([CoinMarketCap](https://coinmarketcap.com/academy/article/lighter-withdrawals-resume-leaked-api-keys)).

So the pool route closes. A real attacker would not stop there.

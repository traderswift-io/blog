---
title: What Would Written Limits on One Key Have Stopped at Lighter?
description: A leaked trading key took about $10.4 million from a market maker's account on Lighter. What written limits on that key would have stopped.
kind: case-study
order: 1
---

On 16 November 2026, a leaked API key let an attacker take about $10.4 million in USDC out of a trader's account on Lighter, a perpetuals exchange.

Outlets and on-chain analysts describe the accounts as a market maker's ([crypto.news](https://crypto.news/lighter-suspends-withdrawals-after-suspected-15-5-million-exploit/), [0xTria](https://x.com/0xTria/status/2122280548047671629)). Lighter said its contracts were not affected ([Lighter](https://x.com/Lighter_xyz/status/2122311006604984497)).

::: notice
The facts here are as of 16 November 2026, checked again on 18 November.

Since then, Lighter has resumed withdrawals and returned about $5 million to the trader ([Crypto Briefing](https://cryptobriefing.com/lighter-api-key-security-exploit/), [CoinMarketCap](https://coinmarketcap.com/academy/article/lighter-withdrawals-resume-leaked-api-keys)).

Its post-mortem says the key was exposed by signing code outside Lighter's official SDKs that reused nonces, the one-time numbers each signature needs ([Lighter](https://x.com/Lighter_xyz/status/2122394446343946717)).
:::

The key did exactly what it was allowed to do.

The problem was not Lighter. It was one trading key, held whole, with every permission and no defined limits.

Any venue that hands out keys like that has the same exposure.

This case study uses the Lighter drain as the example. It asks what a defined trading policy would have done: against the route the attacker used, against the route they would have tried next, and for every other trader on the exchange.

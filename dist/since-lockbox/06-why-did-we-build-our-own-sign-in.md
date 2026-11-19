---
title: Why did we build our own sign-in?
description: Passkey and wallet sign-in, and a gate we own.
order: 6
---

It started with a chart that would not load.

Our charts sat behind a third-party sign-in page that could not show inside a phone frame. We fixed that chart directly, and then took the bigger step: our own sign-in for all of TraderSwift.

Sign-in is a passkey or a wallet. Apps will move onto it one at a time, each only after it works on a phone.

The gate will sit in front of our apps. It checks each signed session, and each app still checks every request on its own.

New sign-ups pay a small proof of work: a short puzzle the device solves, cheap for one person but costly for a bot making thousands of accounts.

Limits are per identity. The network protection in front of it stays where it is.

Owning the gate means owning who gets in, not leaving our network provider. The gate is **Built, not live**: its code is merged, and it is not deployed yet.

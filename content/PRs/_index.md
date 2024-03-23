---
title: ""
date: 2020-06-01T16:16:24+02:00
draft: false
menu:
  main:
    name: "OSS"
    weight: 1
---

# Open Source Work 

Some are WIP, will probably add in context after completing. Since I am on a time-crunch right now (looking for work within the next 60 days), I'm a bit behind on schedule :(

  
1. Port POSIX APIs to Zephyr RTOS
2. Improve incompatible solidity versions error formatting
3. Extract tests in test/libsolidity/ViewPureChecker.cpp to syntaxTests/viewPureChecker
4. Implement dbeug_traceCallMany (nethermind)
5. Store fallback peers in TransactionFetcher as a (PeerId, usize) tuple (RETH)
6. Track unique tx hashes in valid announcement data (RETH)
7. Support suggested priority fee sampling. (Foundry)
8. Mutiny Node BIP39 fix
9. Improve Mapping::find_match to return error when multiple replacements are possible. (Sway)
10. Added missing malloc check in libpayload in Coreboot
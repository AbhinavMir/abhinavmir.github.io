---
title: First principles of Ethereum Rollups
tags: ethereum, crypto
---

Layer 2 solutions have become an integral part of the Ethereum roadmap, especially short term. Today we will be talking about Ethereum L2s.

Question #1 - What are Layer 2 (L2s)

L2 are technologies that help scale a Blockchain network. Layer 1 is what you refer to as the base technology: Bitcoin, Ethereum etc. Layer 2 usually help scale by taking transactions off the L1 network.

Question #2 - Why do we need these L2s

As network traffic increases, so does the load on the network - thus increasing transaction fees, transaction time and such. This makes user experience of the apps built on the network poor. Even using the network becomes unappealing. As Vitalik puts it well: To scale, we can either change how the Layer 1 handles the transaction (bigger blocks, sharding etc) or change the way the user uses the network - L2s do the latter. There are many different approaches to this scalability problem - almost all include Off Chain transactions and they all use the Ethereum Virtual Machine to maintain the security aspect. The first approach to this is Rollups. You might’ve been hearing about Optimism, Arbitrium and Polygon Hermez this last month - All these are examples of Rollups. Rollups perform the transaction off-chain, but some of the data is kept on chain. This, as you will see, is different from some other L2s that move data and transactions, both off chain. Rollups replace on-chain data with processed data - Usually batches with proof on them. A Smart Contract on L1 maintains the Rollup State Root (A merkle root of balance,code etc). The state root switches to the new state root if the previous state root matches current state root.

At this point, we need to check the post-state root so that we know that the batches are correct - Optimistic Rollups (Such as Optimism and Arbitrium) use fraud proofs (all state root published, upon detecting fraud, can submit proof on-chain) and ZK rollups use ZK-SNARK proof. This is where the math and the logic gets hairy too, so I leave you with this bird’s eye view of rollups - a lot of which was inspired from the article below.Layer 2 solutions have become an integral part of the Ethereum roadmap, especially short term. Today we will be talking about Ethereum L2s.

Question #1 - What are Layer 2 (L2s)

L2 are technologies that help scale a Blockchain network. Layer 1 is what you refer to as the base technology: Bitcoin, Ethereum etc. Layer 2 usually help scale by taking transactions off the L1 network.

Question #2 - Why do we need these L2s

As network traffic increases, so does the load on the network - thus increasing transaction fees, transaction time and such. This makes user experience of the apps built on the network poor. Even using the network becomes unappealing. As Vitalik puts it well: To scale, we can either change how the Layer 1 handles the transaction (bigger blocks, sharding etc) or change the way the user uses the network - L2s do the latter. There are many different approaches to this scalability problem - almost all include Off Chain transactions and they all use the Ethereum Virtual Machine to maintain the security aspect. The first approach to this is Rollups. You might’ve been hearing about Optimism, Arbitrium and Polygon Hermez this last month - All these are examples of Rollups. Rollups perform the transaction off-chain, but some of the data is kept on chain. This, as you will see, is different from some other L2s that move data and transactions, both off chain. Rollups replace on-chain data with processed data - Usually batches with proof on them. A Smart Contract on L1 maintains the Rollup State Root (A merkle root of balance,code etc). The state root switches to the new state root if the previous state root matches current state root.

At this point, we need to check the post-state root so that we know that the batches are correct - Optimistic Rollups (Such as Optimism and Arbitrium) use fraud proofs (all state root published, upon detecting fraud, can submit proof on-chain) and ZK rollups use ZK-SNARK proof. This is where the math and the logic gets hairy too, so I leave you with this bird’s eye view of rollups - a lot of which was inspired from the article below.

<a href ="https://vitalik.ca/general/2021/01/05/rollup.html"><div 
style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 3px; padding: 10px; margin-bottom: 20px;">
Vitalik’s Rollup-centric article
</div></a>

State Channels work differently. They allow user to commit however number of transactions they want off-chain, publishing only 2 transactions on chain. An example would be two users playing Rock Paper Scissors - 3 rounds on the Ethereum mainnet - winner takes home 1 ETH (wild, I know). The game would open up a State Channel, making all the fundamental game transactions happen off-chain in a “Channel” - this will mainly be the shape the player chooses - displayed when both the players choose the shape and then deciding the winner.

Once both the users sign using multisig,the final state transaction is published to the L1. As you can image, calling the smart contract for 3 rounds and having such computation occur would be expensive on mainnet. So we do it using EVM running off-chain systems. Plasma L2s are interesting. On these systems, you can create smaller copies of the mainnet, these will be the Child chains - on top of which you can spawn other child chains. These child chains are stacked on top of each other in the Merkle Tree. Each child chain serve a purpose and can operate independently. If you remember fraud proofs from optimistic rollups, it’ll come in handy. The fraud proof technique is used to save the user from malicious nodes and exit from a corrupt transaction. You can read further about it in the link below.

<a href ="https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/plasma/">
<div style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 3px; padding: 10px; margin-bottom: 20px;">
Ethhub’s Plasma article
</div></a>

Sidechains aren’t truly layer 2 since they run an EVM-compatible chain parallel to the mainnet, usually with a bridge. But they have their own set of rules, and don’t use native Ethereum main net security. In this case, Rollups are closest to using EVM security natively. And that’s it for the thread about L2s. It's too late in the night now.
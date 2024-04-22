---
title: How does an Ethereum Transaction work?
---

A Blockchain is essentially a public database in which the data is shared and synchronized across multiple nodes connected in a network. A Blockchain is built up of Block Data structures arranged in a Chain like cryptographic sequence.

Ethereum is no different, when you commit any transaction on the chain, the data must be added to the network for it to be successful. The verification process is similar to Bitcoin, which uses Proof of Work.

A single Ethereum transaction includes the recipient, signature (An indentity generated using the sender’s private key), the amount of $ETH to be transferred, data, gasLimit (Maximum amount of gas that can be allowed on the transaction based on the computation required) and the gasPrice (the fees that sender pays per unit of gas).

With the idea of Blockchain, Transactions and Nodes in place, let’s have a look at the lifecycle of a transaction with the examples of Elon and Indra. Let’s assume Indra wants to buy a bunch of Tesla Electric Trucks to make her new supply chain more eco-friendly, and she decides to pay Elon with Ethereum.

1. Once Indra hits send from her wallet, a transaction hash is generated.
2. The transaction is then broadcasted to the network via a gossip protocol [(Ethereum Wire Protocol)](https://github.com/ethereum/devp2p/blob/master/caps/eth.md).
3. The transaction is then added to a “Pending Transaction Pool” called the txPool with other pending transactions. You can see a list of active pending transactions on the Ethereum Network [here](https://etherscan.io/txsPending).
4. A miner will now pick your transaction and include it in a block that has other transactions. You might have to wait your turn since Miners priotise the transactions with higher gas price since they get to pocket it. If you’ve studied Bitcoin, you might remember that a miner picks 1 MB worth of transactions. This is not true in Ethereum, here a miner picks transactions till they reach the gasLimit or till they run out of the transactions in the *TxPool*. Following is a very complicated image of the structure of a Block in a Blockchain.

![https://i.stack.imgur.com/7eiCt.jpg](Picture of the steps for an Ethereum transaction)
Citation: [https://ethereum.stackexchange.com/a/31869/57651](https://ethereum.stackexchange.com/a/31869/57651)

1. Once your block is confirmed, you will get a Block confirmation number. This is indicative of “Block Height”, as in chronologically how many other blocks have been mined before this particular transaction. The higher this number, the more number of Blocks before you, thus more immutability.

Now that your Block has been added to the network, it is added to the Network, using a “cryptographic chain”, and with that Indra has sent Elon the required number of Ether. However note that this piece skips over important information, and they are

1. How are Transactions stored in a Block
2. How an Ethereum Node works
3. What is this “cryptographic chain” I am talking about

### References

https://ethereum.stackexchange.com/a/31869/57651

https://github.com/ethereum/devp2p/blob/master/caps/eth.md

https://ethereum.org/en/developers/docs/transactions/
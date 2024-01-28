---
title: Stolen notes on the EVM
tags: ethereum
---

What is the EVM? How does it work?
At a high level, Ethereum Virtual Machine is a deterministic function that outputs a certain value for a certain input. The EVM is much like any other computer, but it specializes in running smart contracts. EVM is like JVM - but instead of using any other process virtual machine, on Ethereum we use EVM because we need things like finite determinism and gas-implementations.

The compiler design behind EVM
Solidity is a high-level language choice that compiles into bytecodes (machine readable set). Solidity is one of the more popular choices, otherwise Vyper, Flint, even C via ceagle can be your choices.

Opcodes are low-level human-readable instruction sets that are representative of the deployed/creation bytecode. This creation bytecode is used to generate the runtime bytecode. The following contract is an example.

```
pragma solidity ^0.8.10;
contract MyContract {
    uint i = (10 + 2) * 2;
}
```

For this, this is generated-

```
"object": "60806040526018600055348015601457600080fd5b50603f8060226000396000f3fe6080604052600080fdfea264697066735822122068ed984f1f49a5710584afd544f61110f039d04d2791e66a88e1d8914ffdff1464736f6c634300080b0033",
```

```
"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x18 PUSH1 0x0 SSTORE CALLVALUE DUP1 ISZERO PUSH1 0x14 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x3F DUP1 PUSH1 0x22 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x0 DUP1 REVERT INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 PUSH9 0xED984F1F49A5710584 0xAF 0xD5 DIFFICULTY 0xF6 GT LT CREATE CODECOPY 0xD0 0x4D 0x27 SWAP2 0xE6 PUSH11 0x88E1D8914FFDFF1464736F PUSH13 0x634300080B0033000000000000"
```

### EVM Architecture
There are two types of accounts in Ethereum: EOA (Externally owned accounts) and Smart Contracts. Both are treated similarly by the EVM, have balances and storage. Here's one of my favourite graphics for this.

Focus on the lower two blocks. When a transaction caller sends a transactiom, a module to recieve input transaction recieves the input and updates storage, while storing the arguments in the stack with the program counter. The Smart Contract bytecode, with the stack is then fed to the EVM for gas estimation via opcodes. The gas fee is deducted, and the opcode is executed. THe memory is then updated. If the transaction fails, the memory is updated.

EVM is stack-designed, so stack operations such as pop, push apply to it. The overall architecture is similar to any other FSM and instructions are implemented how they're implemented in other stack-based machines, with obvious differences.

Different implementations of the Ethereum protocol are implemented in different ways/languages such as Geth, Parity, Mist - with different add-on features, but same core structure of EVM + State + Consensus.

Memory, Storage, State and such
The Ethereum Virtual Machine has three areas where it can store data- storage, memory and the stack, which are explained in the following paragraphs.

Each account has a data area called storage, which is persistent between function calls and transactions. Storage is a key-value store that maps 256-bit words to 256-bit words. It is not possible to enumerate storage from within a contract, it is comparatively costly to read, and even more to initialise and modify storage. Because of this cost, you should minimize what you store in persistent storage to what the contract needs to run. Store data like derived calculations, caching, and aggregates outside of the contract. A contract can neither read nor write to any storage apart from its own.

The second data area is called memory, of which a contract obtains a freshly cleared instance for each message call. Memory is linear and can be addressed at byte level, but reads are limited to a width of 256 bits, while writes can be either 8 bits or 256 bits wide. Memory is expanded by a word (256-bit), when accessing (either reading or writing) a previously untouched memory word (i.e. any offset within a word). At the time of expansion, the cost in gas must be paid. Memory is more costly the larger it grows (it scales quadratically).

The data in the Blockchain itself is stored via a Merkle Patricia-Trie tree Data Structure. A Patricia Trie or prefix Tree or radix Tree is an ordered structured tree, which takes the applications of usually the data it stores. A node’s position in the tree defines the key with which that node is associated, which makes tries different in comparison to binary search Trees, in which a node stores a key that corresponds only to that node.

In different implementations, the state is maintained in different ways. For example in Go-Ethereum, it is done via stateDB.go.

Is the EVM Turing-complete, why?
Turing complete machines are machines that despite any complexity of problem, will solve a problem given enough time. This is of course, an abstract idea developed using an infinite tape. EVM is quasi-Turing complete system, because the machine executes as far as the gas is provided. Gas is the fundamental fuel for the infrastructure and this solves the halting problem in a way - in that you cannot generally determine whether an arbitrary problem provided will keep running forever or not, but the gas will not allow any problem to run forever. The gas is calculated on an opcode-basis. For example, to calculate one Keccak256 cryptographic hash it will take 30 gas each time a hash is calculated, plus a cost of 6 more gas for every 256 bits of data being hashed.

What is Gas and why is it important for operations in the EVM?
Ethereum gas is unique from Bitcoin due to how pieces of code are treated on the platform. On Bitcoin, gas/fee is charged per size unit basis, but since Ethereum allows for complex, decisive code to be run on the platform, it charges gas per operation unit basis. Gas isn't a token, but rather a unit of measurement of work, like joule. Now USD <> Joule value is decided by market rate, but unit of work done is decisive and lawful (one by nature, one by code). If I set a gas fee too low with my transaction (although post update, I must set a baseFee to my txn), no node will choose to pick my transaction and add it to a Block, thus resulting in no change in the Blockchain state - which is the end goal.

Gas is important because it allows for monetization of operation. Monetization of operation means - 1. Nodes are rewarded for maintaining integrity of node, 2. There is a punishment for malicious code to cause a DOS-like attack. As disccused earlier, the gas feature of the EVM allows for the quasi-Turing complete state of the machine. Sure, you don't have an infinite tape, but gas allows for the scope of usage of tape to be reduced - if that makes sense.

What are Jump Tables and why are they relevant for gas consumption?
The entry point to the actual code execution is the run method of the EVM interpreter. This method is essentially going through the bytecode step by step and, for each opcode, looking up the opcode in a data structure known as jump table– Among other things, this table contains a reference to a Go function that is to be executed to process the instruction. More specifically, an entry in the jump table contains the following fields, which partially refer to other tables in other source code files.

In a jump table, each entry has a couple of fields, we need to have a look at constant gas and dynamic gas.


```
abc
```

```go
type operation struct {
	// execute is the operation function
	execute     executionFunc
	constantGas uint64
	dynamicGas  gasFunc
	// minStack tells how many stack items are required
	minStack int
	// maxStack specifies the max length the stack can have for this operation
	// to not overflow the stack.
	maxStack int

	// memorySize returns the memory size required for the operation
	memorySize memorySizeFunc

	halts   bool // indicates whether the operation should halt further execution
	jumps   bool // indicates whether the program counter should not increment
	writes  bool // determines whether this a state modifying operation
	reverts bool // determines whether the operation reverts state (implicitly halts)
	returns bool // determines whether the operations sets the return data content
}
```

Constant gas is the constant gas value of the operation, and dynamic gas is the gas value of the operation as a function of the parameters.

Since gas is computed from opcode, the library gas usage isn’t considered - since it is computed via jump tables from opcodes. But bytecode undergoes the same linking process as the linking process of libraries in C.

What are Precompiled Contracts?
> These are four so-called ‘precompiled’ contracts, meant as a preliminary piece of architecture that may later become native extensions. The four contracts in addresses 1, 2, 3 and 4 execute the elliptic curve public key recovery function, the SHA2 256-bit hash scheme, the RIPEMD 160-bit hash scheme and the identity function respectively.

Full, updated list-
- Recovery of ECDSA signature
- Hash function SHA256
- Hash function RIPEMD160
- Identity
- Modular exponentiation (EIP 198)
- Addition on elliptic curve alt_bn128 (EIP 196)
- Scalar multiplication on elliptic curve alt_bn128 (EIP 196)
- Checking a pairing equation on curve alt_bn128 (EIP 197)
- BLAKE2b hash function (EIP 152)


Implemented in geth as such

```go
var PrecompiledContractsByzantium = map[common.Address]PrecompiledContract{
    common.BytesToAddress([]byte{1}): &ecrecover{},
    common.BytesToAddress([]byte{2}): &sha256hash{},
    common.BytesToAddress([]byte{3}): &ripemd160hash{},
    common.BytesToAddress([]byte{4}): &dataCopy{},
    common.BytesToAddress([]byte{5}): &bigModExp{},
    common.BytesToAddress([]byte{6}): &bn256Add{},
    common.BytesToAddress([]byte{7}): &bn256ScalarMul{},
    common.BytesToAddress([]byte{8}): &bn256Pairing{},
}
```

Precompiled contracts are not native opcodes, but are calculations that are implemented in the EVM codebase for efficient calucaltions without EVM overheads. Ref: https://ethereum.stackexchange.com/questions/440/whats-a-precompiled-contract-and-how-are-they-different-from-native-opcodes/28469

What are the pros and cons of the EVM compared to other VMs?
JVM is another popular process VM - it has it's advantages, of course, but EVM allows for finality and gas-implementation, two important factors of the Ethereum ecosystem.
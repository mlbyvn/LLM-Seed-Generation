---

## Abstract

---

## Сlarification

"Mutation-based" refers to a term from traditional software fuzzing: 

Echidna belongs to a specific family of fuzzers: property-based fuzzing, which is heavily inspired by QuickCheck. In contrast to a classic fuzzer that tries to find crashes, Echidna aims to break user-defined invariants.

---

## Properties & Vulnerabilities

1. Properties of Ethereum Request for Comments standards (ERC20, ERC721, ERC4626)
2. Usage of "wierd" ERC20 tokens
   - Tokens with weird decimals (like USDC)
3. Protocol invariants

---

## Dataset of contracts

One common issue with existing datasets is that they feature contracts with outdated Solidity versions (ranging from 0.4.24 to 0.7). Despite Solidity 0.8.0 being introduced in late 2020, there remains a lack of large datasets containing vulnerable contracts utilizing pragma versions above 0.8.0. To address this problem, several approaches were considered:

1. **Refactor existing datasets**  
   - **Approach:** Use contracts from current datasets and rewrite them to support newer pragma versions.  
   - **Drawbacks:** This is highly labor-intensive and introduces a risk of unintentionally adding new bugs during the refactoring process.  

2. **Generate contracts with bug synthesizers**  
   - **Approach:** Use automated tools to create vulnerable contracts.  
   - **Drawbacks:** The generated contracts tend to be overly simplistic, lacking the use of libraries, ERC standards, or real-world complexity.  

3. **Leverage real-world vulnerabilities and known exploits**  
   - **Approach:** Extract real-world vulnerabilities from audit reports on platforms like [Solodit](https://solodit.cyfrin.io/) and supplement them with "textbook" bugs from Capture The Flag (CTF) challenges. These exploits can then be manually injected into sample contracts.  
   - **Advantages:** This method ensures the inclusion of realistic vulnerabilities while keeping the dataset concise and practical.

---

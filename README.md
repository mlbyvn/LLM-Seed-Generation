# Leveraging LLM-generated Seeds for Mutation-based Fuzzing in Solidity Smart Contracts

Welcome to **"Leveraging LLM-generated seeds for mutation-based fuzzing in Solidity smart contracts"** repository. This project explores how Large Language Models (LLMs) can be utilized to generate high-quality initial inputs (seeds) for mutation-based fuzzing, improving the detection of vulnerabilities in Ethereum smart contracts.

## Table of Contents

1. [Overview](#overview)
2. [Clarification](#clarification)
3. [Dataset of contracts](#dataset-of-contracts)
4. [Features](#features)
5. [Repository Structure](#repository-structure)
6. [Setup](#setup)
7. [Usage](#usage)
8. [Results](#results)
9. [Contributing](#contributing)
10. [License](#license)

---

## Clarification



---

## Overview

Smart contracts written in Solidity often have complex behaviors, making them susceptible to subtle vulnerabilities that can result in severe financial losses. Mutation-based fuzzing is a prominent technique for identifying such issues, but its effectiveness heavily depends on the quality of the input seeds.

This thesis investigates the use of LLMs (e.g., OpenAI GPT models) to generate high-quality input seeds tailored to Solidity smart contracts. By combining these seeds with traditional mutation-based fuzzing techniques, we aim to:

- Enhance the coverage of fuzzing.
- Identify more intricate vulnerabilities.
- Automate parts of the seed generation process, reducing manual intervention.

---

## Dataset of contracts

One common issue with existing datasets is that they feature contracts with outdated Solidity versions (ranging from 0.4.24 to 0.7). Despite Solidity 0.8.0 being introduced in late 2020, there remains a lack of large datasets containing vulnerable contracts utilizing pragma versions above 0.8.0. To address this problem, several approaches were considered:

1. Use contracts from exisiting datasets, re-writing them for newer pragma versions. Cons: Too much labor, refactoring can introduce new uninteded bugs.
2. Generate vulnerable contracts with bug synthesizers. Cons: contracts are too generic, do not use any libraries or ERCs.
3. Get detected real-world vulnerabilities from audit reports on [Solodit](https://solodit.cyfrin.io/) and "textbook" bugs from different CTFs, then inject them in sample contracts manually. This way real-world exploits can be introduced, keeping the codebase compact and neat.


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

## Features

- **LLM-Driven Seed Generation:** Use of advanced LLMs to generate seed inputs.
- **Vulnerability Detection:**
- **Metrics and Analytics:** 

---

## Repository Structure

```
├── src
│   ├── llm_seed_generator.py  # Module for interacting with LLMs to generate seeds
│   ├── mutator.py             # Implements mutation strategies
│   ├── fuzzer.py              # Core fuzzing engine
│   ├── solidity_analyzer.py   # Analyzes and parses Solidity contracts
├── contracts
│   ├── examples               # Sample Solidity smart contracts for testing
│   └── vulnerabilities        # Known vulnerable contracts
├── results
│   ├── coverage_reports       # Reports on fuzzing coverage
│   └── vulnerabilities_found  # Logs of detected vulnerabilities
├── tests
│   ├── test_llm_seeds.py      # Unit tests for seed generation
│   ├── test_mutator.py        # Unit tests for mutation engine
│   ├── test_fuzzer.py         # Unit tests for fuzzing engine
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # License file
```

---

## Setup

### Prerequisites

- Python 3.8+
- Node.js (for Solidity tools like `solc`)
- API access to an LLM service (e.g., OpenAI API key)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/llm-fuzzing-thesis.git
   cd llm-fuzzing-thesis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory with your LLM API credentials:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Install Solidity compiler tools:
   ```bash
   npm install -g solc
   ```

---

## Usage

### 1. Generate Seeds
Run the LLM seed generator to create initial seeds for fuzzing:
```bash
python src/llm_seed_generator.py --contract contracts/examples/sample.sol
```

### 2. Start Fuzzing
Run the fuzzer with generated seeds:
```bash
python src/fuzzer.py --seeds results/seeds.json --contract contracts/examples/sample.sol
```

### 3. Analyze Results
After fuzzing completes, view the coverage and vulnerability reports:
```bash
cat results/coverage_reports/report.json
cat results/vulnerabilities_found/log.txt
```

---

## Results

The results of this research include:

- **Improved Coverage:** Demonstrating increased code coverage compared to traditional seed generation methods.
- **Vulnerability Detection:** Identified new vulnerabilities in open-source Solidity contracts.
- **Performance Analysis:** Quantitative analysis of LLM-based seed generation's impact on fuzzing effectiveness.

For detailed findings, refer to the `results/` directory.

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.



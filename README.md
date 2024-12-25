# Leveraging LLM-generated Seeds for Mutation-based Fuzzing in Solidity Smart Contracts

Welcome to the repository for my thesis, **"Leveraging LLM-generated seeds for mutation-based fuzzing in Solidity smart contracts."** This project explores how Large Language Models (LLMs) can be utilized to generate high-quality initial inputs (seeds) for mutation-based fuzzing, improving the detection of vulnerabilities in Ethereum smart contracts.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Repository Structure](#repository-structure)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

Smart contracts written in Solidity often have complex behaviors, making them susceptible to subtle vulnerabilities that can result in severe financial losses. Mutation-based fuzzing is a prominent technique for identifying such issues, but its effectiveness heavily depends on the quality of the input seeds.

This thesis investigates the use of LLMs (e.g., OpenAI GPT models) to generate high-quality input seeds tailored to Solidity smart contracts. By combining these seeds with traditional mutation-based fuzzing techniques, we aim to:

- Enhance the coverage of fuzzing.
- Identify more intricate vulnerabilities.
- Automate parts of the seed generation process, reducing manual intervention.

---

## Features

- **LLM-Driven Seed Generation:** Use of advanced LLMs to generate seed inputs.
- **Custom Mutation Engine:** Implements mutation strategies optimized for Solidity.
- **Vulnerability Detection:** Focused on common issues like reentrancy, overflow/underflow, and unchecked external calls.
- **Metrics and Analytics:** Detailed reports on fuzzing coverage and detected vulnerabilities.

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



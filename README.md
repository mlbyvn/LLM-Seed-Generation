<h3 align="center">Leveraging LLM-generated Seeds for Mutation-based Fuzzing in Solidity Smart Contracts</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Solidity-e6e6e6?style=for-the-badge&logo=solidity&logoColor=black" alt="Solidity"/>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
  <img src="https://camo.githubusercontent.com/8c47fd6bf4ac8eec4be8caefd7d56b8cdbff9de4985b76e3ff3ab1497d7363e8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466f756e6472792d677265793f7374796c653d666c6174266c6f676f3d646174613a696d6167652f706e673b6261736536342c6956424f5277304b47676f414141414e53556845556741414142514141414155434159414141434e6952304e414141456c456c45515652346e483156555568556152673939383459647a42706b7152305a3231307249455349585361624562634867796472704e52526a30306b57617a746a3055314d4f57304d4f49624433303049764c4d7142704d54475978646f71796f524e4455455342445777557550756743535373544d3775304f6a312f2b656664694d636d6e50322f66446437374434662f4f4236784361327572515a626c6c56494359477471616e4b31744c53344164674179414167797a4a615731734e712f756c543474774f4777346650697741474470374f77385656316437625661725257785743772f6b386d67736245786d30776d5a2b4c782b4d2f5872312f2f4363417353566d534a4830314d634c68734145416e45356e782b546b35422f78654a784f70354e39665832737171716978574c686e5474333648413447497646474931475533563164663550652f394431743765486b676b45757a6f3647425054343957576c6f713748613766756a5149546f6344753761745573336d38336936745772326f6b544a2f6a6978517565506e3236357a5053634468736b47555a652f6675625876382b44467633727970626469775161786274343652534954373975336a304e415162393236525656564f54342b5471765679767a38664430594443354e546b3679736248786c43524a2f354b536c41415552794b5254464e546b7741673774363953352f507837362b50713747794d6749392b2f667a394852555149514f336273454b4f6a6f333844734a43554a4144772b2f3042565657376f74486f387073336234797658723343784d514554435954544359544e453044414f546c3553475879304652464f7a5a7377646d73786b564652584c4e545531786d67302b6b4e76622b2f3341474163474269493739363957776367367572712b4f544a4539363764343962746d7a68395054305233574a52494b4251494442594a425455314e73614767674147477a32665465337435664165515a415777754c69347550336e79704f5431656d457747464265586f3761326c6f734c4379676f6145422f6633394d4a6c4d434956436b43514a42773865684e56716863666a51584e7a7331525355694b7458372b2b4445415a71717171334b465169414259554644414d32664f6b4351584678644a6b766676333264685953473958692b765862764732646e5a6a346f446751434c696f716f4b417148686f626f6444712f4d63374e7a556b6c4a535549426f4f7732577a59746d30626c7065587357624e476b784d544f44703036646f61327644344f41674e6d37634349764641704c516452336e7a7033447a70303738664c6c537851564665486475336341674970486a7836392f7a425558356b2b4d4442417439764e5938654f736275376d366c556967634f484b444c3557496d6b79484a7a39544759724563414c734d49506e363965735a54644d49674d2b6550554e58567864753337364e73724979754e3175584c70304357617a476350447733433558464256465766506e6b564e5451313850702b657a5759354d7a507a4f344466414142486a687a704a736c554b71566476486952342b506a624739765a79365849306b754c5330786d55785343454753395076394c4330747064466f5a47566c705361456f4d2f6e757749414b782f37713547526b6239436f5a42515656576350332b657a35382f4a306d6d30326b4f44673779776f554c6a4d5669544b6654744e7674584c74324c5464743271546e63726e6c736247784c49437653557166726c35484a424c68314e54556b6842434a386d4668515832392f6454565655574642547777594d48314857646c7939667071496f65694b52574a71666e3264316458576e4c4d7566377a4d41484431367447642b666e37465a7932627a59724b796b6f644141465156565639635846526b4e5465766e334c75626b357472533058506e6678484534484e384f44772b6e562f79616e70366d782b4f68782b503561494d51676d4e6a59332f5731745a2b74357273537747372b666a78342f37362b76726d3764753332776f4c433030416b45366e3338666a385a6d4844782f2b637550476a5238424a4c3859734374596451494d414c5971696c4b764b456f394150754874792b656748384133476646444a586d786d4d41414141415355564f524b3543594949253344266c696e6b3d6874747073253341253246253246626f6f6b2e676574666f756e6472792e7368253246" alt="Foundry"/>
  <img src="https://img.shields.io/badge/chatGPT-74aa9c?logo=openai&logoColor=white" alt="GPT"/>
</p>

# About The Project

## Project Description

Welcome to **"Leveraging LLM-generated seeds for mutation-based fuzzing in Solidity smart contracts"** repository.
This project highlights the research results of my bachelor thesis *"Leveraging LLM-Generated Seeds
for Mutation-Based Fuzzing in Solidity"*, in which I've tested the integration of different OpenAI models with [Echidna](https://github.com/crytic/echidna?tab=readme-ov-file) smart contract fuzzer and it's influence on the fuzzing outcome.

Recent research shows that LLMs can be used to enhance the fuzzing process without being directly integrated into the fuzzing engine. In 2023, [Asmita et al.](https://www.usenix.org/conference/usenixsecurity24/presentation/asmita) used LLM to generate a set of initial seeds, called
the seed corpus, for mutation-based fuzzing of embedded Linux firmware. Asmita
et al. claim that the proposed technique significantly improved the fuzzing outcome
by enhancing the number of identified unique crashes. 

The idea was to use the approach proposed in the paper
to generate high-quality initial seeds that accurately reflect the smart contract code,
rather than relying solely on Echidna internal seed generation. The initial assumption was that LLM's ability to understand context can help in generating seeds not only for structural peculiarities of the contract, but also tailored to an exact specific function implementation and protocol logic. 

## Test setup

For the test benchmark I've modified two protocols designed by Cyfrin:
1. A fixed point math library for WAD numbers [MathMasters](https://github.com/Cyfrin/2024-01-math-master/tree/main)
2. An AMM protocol [Tswap](https://github.com/Cyfrin/5-t-swap-audit)

Both contracs have intentionally injected vulnerabilities which I modified and also introduced new ones. It is obvious that smart contract property based testing differs from traditional software fuzzing and the bug can only be uncovered if the test suite and harness are designed properly, so the challenge was to introduce such bugs that can be potentially missed by Echidna even with correct test suites. 


With test limit equal to 100,000 runs Echidna has following bug detection rates for introduced vulnerabilities:

* *AlmostPreciseMath*
    1. mulWadUp - multipliestwoWADnumbersi.e., numberswith
    18 decimal places, rounding up. If the result of dividing y by x is exactly
    one, the output value is rounded incorrectly. Adopted from MathMasters without change
    2. sqrt - computes the square root of xx using Heron’s method.
    One of initial estimate thresholds is slightly inaccurate, leading
    to imprecise calculations for values within a narrow range. Adopted with a threshold change
* *SwapPool*
    1. swapExactOutput - determines the amount of input tokens
    required to obtain a specified amount of output tokens and then executes
    the swap. If the requested output amount approaches the total token
    reserves in the pool, the user may receive slightly fewer tokens due to an
    improperly implemented slippage protection mechanism. Was engineered and injected in TSwap protocol,
    the original TSwap vulnerability that breaks the protocol invariant is fixed 

For each of the two protocols from the benchmark, 250 separate fuzzing campaigns
were executed using seeds automatically generated by Echidna. These campaigns
were conducted to estimate the fuzzing failure rate, allowing a comparison between
the results of the proposed approach and these values. The odds that a bug is
detected by Echidna using default seeds, with a 95% confidence level, are as fol-
lows
* *mulWadUp* - 82 ± 5%
* *sqrt* - 25 ± 5%
* *swapExactOutput* - 90 ± 5%

After that, 50 separate fuzzing campaigns were executed for each generated seed corpus, leading to
a total of 1,000 fuzzing campaigns.

Running 250 campaigns for each generated corpus would be too time-consuming, so
the number of runs was reduced to 50 per corpus. Since the confidence intervals for
fuzzing with default Echidna seeds were determined based on 250 campaigns, directly
comparing the results of fuzzing with LLM-generated seed corpora to these intervals
would be inaccurate. To address this issue, Fisher’s exact test was applied. It
determines whether the difference in fuzzing rates is statistically significant, meaning
whether fuzzing with LLM-generated seeds leads to a different outcome. Compared
to methods like the chi-square test, Fisher’s exact test is more suitable for small
sample sizes and is particularly effective for comparing proportions of success and
failure.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Tested approach

I've chosen [Echidna](https://github.com/crytic/echidna) as a property-based coverage guided fuzzer for this project, as it is has comprehencive documentation, supports *corpus replay* and is currently used by most of the top notch auditing companies. The seed generation is implemented as follows:
1. Seeds are generated using python `seed_generator.py` script, which makes requests to OpenAI models using API. The response is saved in a .txt file 
2. Contract ABI is extracted using another python script named `get_abi`
3. Using `wrapper.py` script and contract ABI alongside with generated seed values, the seeds are wrapped in an Echidna compatible format and then added into the corpus directory manually 
4. Fuzzing campaigns are ran with following parameters in config.yaml file:
```
testMode: assertion
corpusDir: "corpusDir"
seqLen: 25
testLimit: 100000
```
 
## Research outcome

Two OpenAI models were tested: [gpt-4o](https://openai.com/index/hello-gpt-4o/) and [o3-mini](https://openai.com/index/openai-o3-mini/). 

Using the proposed prompt *gpt-4o* model doesn to seem to deliver any results that would be statistically different from fuzzing with deafult Echidna seeds. This indicates that the fuzzing process was not affected by the use of
generated seeds. 

![results](img/fisherexact.png)

However, two seed corpora produced different results. In particular, Corpus 3 con-
tained a seed that directly triggered a bug in the mulWadUp function, causing the
property to be violated in every fuzzing campaign. Upon closer examination, this
seed was found to have been randomly generated as an overflow test case. Despite
its classification, the bug it triggered was unrelated to overflows and could be consid-
ered a coincidental discovery. Corpus 2 has a borderline p-value for the sqrt function,
which could be considered almost significant. However, the average odds of finding
the bug were lower. This suggests that using this corpus of initial seeds may lead to
less effective fuzzing results.
The o3 model, which is more capable in reasoning tasks, demonstrated better results
on the AlmostPreciseMath contract. It identified bug in the mulWadUp function
across all five attempts, provided a correct justification for the nature of the bug,
and generated values that violate the property directly. Although the bug in the
sqrt function was not detected and the difference between rates was not statistically
significant, the suggested values were actually tailored to the specific function imple-
mentation. For example, they targeted an edge case unique to Heron’s method for
computing square roots.
ThebranchintheswapExactOutputfunctionthatviolatedtheprotocolpropertywas
also detected. Unlike GPT-4o, which generated numeric values for that function, o3-
miniwasabletounderstandthatthevaluetriggeringthebugdependsonpoolreserve
parametersdefinedinanexternalcontract, whichcouldbealsoalteredwithinthecall
sequence during the fuzzing process. The model suggested a formula to calculate the
value using the current pool reserves, which produces results that trigger the bug.
After manually calculating the value for the defined pool reserves, wrapping it as
a seed, and adding it to the seed corpus, the property is violated in each distinct
fuzzing campaign.

Moreover, after identifying a call sequence that triggers the bug, Echidna attempts to minimize
the sequence, making it as short and simple as possible. However, for complex pro-
tocols, such as a decentralized exchange, this may result in significant time overhead.
The use of the generated seed corpus helps save time on minimization, as the bug is
always triggered within a single function call:

![overhead](img/overhead.png)



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Repository structure

```
├── 1-magic
│   ├── config.yaml                 # Echidna configuration file
│   ├── magic.sol                   # Contract for initial tests
├── 2-math
│   ├── AlmostPreciseMath.sol       # Fixed point math contract
│   └── config.yaml                 # Echidna configuration file
├── 3-amm
│   ├── src
|   |    ├── PoolFactory            # Creates a pool for a token pair
│   |    └── SwapPool.sol           # Main AMM protocol engine
|   ├── test
|   |     └── mocks
|   |           └── ERC20Moc.sol    # Mock ERC20 contract that mimics token behavior
|   ├── config.yaml                 # Echidna configuration file
|   ├── Setup.sol                   # Sets up the test environment
|   └── EchidnaTestAMM.sol          # Test contract where all properties are defined      
├── python-scripts
│   ├── plots
|   |     ├── confintervals.py      # Plots confidence intervals 
|   |     ├── fisherstest.py        # Calculates p-values and odd ratios for fisher's test
|   |     ├── fisherstestplot.py    # Plots the results of fisher's test
|   |     └── timeoverhead.py       # Plots the time series of fuzzing duration
│   ├── get_abi.py                  # Extracts contract's ABI
│   ├── seed_generator.py           # Calls listed model
|   └── wrapper.sol                 # Wraps values into the right seed format
├── requirements.txt                # Dependencies
└──README.md                        # Project documentation
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
# Getting Started

## Prerequisites

- Python 3.8+
- Node.js (for Solidity tools like `solc`)
- API access to an LLM service (e.g., OpenAI API key)
- [Foundry](https://book.getfoundry.sh)
- [Echidna](https://github.com/crytic/echidna)


## Setup

1. Clone the repo
2. Run following commands:
```bash
 cd 3-amm
 forge install foundry-rs/forge-std --no-commit
 forge install openzeppelin/openzeppelin-contracts --no-commit
```
```bash
 pip install openai
 pip install matplotlib
 pip install numpy
 pip install scipy
```
3. [Create an API key](https://platform.openai.com/docs/overview) for OpenAI
4. Add your OpenAI API key to the seed_generator.py:
     ```py
     client = OpenAI(
        api_key="API_KEY_HERE"
     )
     ```

## Usage 

### 1. Generate values
1. Add seed_generator.py into the project folder
2. cd into the folder
3. Run:
```bash
python seed_generator.py '<input_files>' <output_file>
```

### 2. Wrap the values into the seed format
1. cd into the project folder
2. Important: this must be a foundry project, as the script uses `forge inspect` command. If the foundry project is not set up, run `forge init` and add contracts in scope into the /src folder
3. Copy get_abi.py and wrapper.py into the folder
4. Run get_abi.py to extract the ABI
5. Using the extracted ABI and generated values, run wrapper.py
6. wrapper.py usage example:
```bash
python wrapper.py --abi AlmostPreciseMath.abi.json --functions '["solmateSqrt", "test_fuzzDivWadUp"]' --values '[
[123456], [10,20]]' --outfile seeds.txt
```

### 2. Start Fuzzing
Run Echidna:
```bash
echidna CONTRACT_NAME --config config.yaml
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Known Issues

1. `get_abi.py` uses `forge inspect` command, thus works only in the foundry projects
2. `wrapper.py` must be modified in order to work with payable functions or adjustable delay and gas price
3. Test protocols set up within the allotted time demonstrated the benefits of using LLM-generated initial seed corpora. However, due to the small size of
thebenchmark,theseresultsshouldbeinterpretedwithcaution.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

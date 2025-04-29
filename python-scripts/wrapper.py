import json
import argparse
import os

'''
Usage example: python wrapper.py --abi AlmostPreciseMath.abi.json --functions '["solmateSqrt", "test_fuzzDivWadUp"]' --values '[
[123456], [10,20]]' --outfile seeds.txt
'''

def load_abi(file_path):
    """Loads and returns the ABI from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def construct_echidna_seeds(functions, values, abi):
    """
    Constructs echidna seeds based on the given function names, their parameter values,
    and the ABI to determine the expected parameter count.

    :param functions: List of function names (e.g., ["solmateSqrt", "test_fuzzDivWadUp"]).
    :param values: List of lists. Each inner list contains parameter values for the function.
                   For example: [[123456], [10, 20]]
    :param abi: ABI loaded from the file (list of dicts).
    :return: List of echidna seed objects.
    :raises: ValueError if the provided values do not match the ABI's expected parameter count.
    """
    # Build a mapping from function names to their ABI entries (ignoring non-function types).
    FUNCTION_ABI = {
        item["name"]: item
        for item in abi
        if item.get("type") == "function"
    }

    if len(functions) != len(values):
        raise ValueError("The functions and values arrays must have the same length.")

    seeds = []
    for func_name, params in zip(functions, values):
        # Ensure the function exists in the ABI.
        if func_name not in FUNCTION_ABI:
            raise ValueError(f"Function '{func_name}' not found in ABI.")
        
        func_abi = FUNCTION_ABI[func_name]
        expected_param_count = len(func_abi.get("inputs", []))
        
        if len(params) != expected_param_count:
            raise ValueError(f"Function '{func_name}' expects {expected_param_count} parameters, but got {len(params)}.")
        
        # Build argument objects.
        # This example assumes each parameter is a uint256 and tags it as "AbiUInt".
        args_objs = [{"contents": [256, str(arg)], "tag": "AbiUInt"} for arg in params]
        
        # Construct the echidna seed using the provided format.
        seed = {
            "call": {
                "contents": [func_name, args_objs],
                "tag": "SolCall"
            },
            "delay": [
                "0x000000000000000000000000000000000000000000000000000000000005ae99",
                "0x000000000000000000000000000000000000000000000000000000000000e3f7"
            ],
            "dst": "0x00a329c0648769A73afAc7F9381E08FB43dBEA72",
            "gas": 12500000,
            "gasprice": "0x0000000000000000000000000000000000000000000000000000000000000000",
            "src": "0x0000000000000000000000000000000000020000",
            "value": "0x0000000000000000000000000000000000000000000000000000000000000000"
        }
        seeds.append(seed)
    return seeds

def main():
    parser = argparse.ArgumentParser(
        description="Generate valid Echidna seeds using the contract ABI to determine parameter counts."
    )
    parser.add_argument(
        "--abi",
        type=str,
        required=True,
        help="Path to the ABI JSON file."
    )
    parser.add_argument(
        "--functions",
        type=str,
        required=True,
        help='JSON array of function names. Example: \'["solmateSqrt", "test_fuzzDivWadUp"]\''
    )
    parser.add_argument(
        "--values",
        type=str,
        required=True,
        help='JSON array of parameter arrays. Example: \'[[123456], [10,20]]\''
    )
    parser.add_argument(
        "--outfile",
        type=str,
        required=True,
        help="Output file name (e.g., seeds.txt)."
    )
    args = parser.parse_args()

    try:
        abi = load_abi(args.abi)
    except Exception as e:
        print("Error loading ABI file:", e)
        return

    try:
        functions = json.loads(args.functions)
        values = json.loads(args.values)
    except Exception as e:
        print("Error parsing JSON input:", e)
        return

    try:
        seeds = construct_echidna_seeds(functions, values, abi)
        # Minify the JSON output (no extra whitespace)
        seed_str = json.dumps(seeds, separators=(',', ':'))
    except Exception as e:
        print("Error constructing echidna seeds:", e)
        return

    # Define the output directory and ensure it exists.
    output_dir = os.path.join("corpusDir", "coverage")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, args.outfile)

    try:
        with open(output_path, 'w') as f:
            f.write(seed_str)
        print(f"Seeds written to {output_path}")
    except Exception as e:
        print("Error writing to output file:", e)

if __name__ == "__main__":
    main()

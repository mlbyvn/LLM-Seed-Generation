# -*- coding:utf-8 -*-
# @Script: seed_generator.py
# @Author: mlbyvn
# @Email: Aleksandr.Rybin@ruhr-uni-bochum.de
# @Create At: 2025-01-19 03:34:50
# @Last Modified By: mlbyvn
# @Last Modified At: 2025-03-09 21:06:38
# @Description: Following script generates values for a seed corpus for echidna fuzzer for solidity contracts in scope.

from openai import OpenAI
import os
import sys

'''
Insert your openai API key (https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)
'''
client = OpenAI(
  api_key="API_KEY_HERE"
)

def merge_solidity_files(input_files: str) -> str:
    """Merges the contents of multiple Solidity files into a single string.

    Parameters:
        input_files (str): A string containing Solidity file paths separated by whitespace.

    Returns:
        str: The merged content of the Solidity files as a single string.
    """
    file_list = input_files.split()
    merged_content = []

    try:
        for file_path in file_list:
            if not os.path.isfile(file_path):
                print(f"Warning: {file_path} does not exist or is not a file.")
                continue

            with open(file_path, 'r') as infile:
                content = infile.read()
                merged_content.append(content)
                merged_content.append("\n\n")  # Add some spacing between files

        return "".join(merged_content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def analyze_smart_contract_and_generate_seeds(solidity_code, output_file):
    '''Generate values for echidna seeds based on solidity contracts
    in scope.

    Parameters:
        solidity_code (str): Merged contracts in scope
        output_file (str): Path to the output file where the values will be stored.
    '''
    try:

        prompt = (
            "You are an AI specialized in smart contract analysis and fuzz testing. "
            "Analyze the following Solidity smart contract and generate input values "
            "That could potentially violate the user-defined Echidna properties."
            "Ensure the values are not random but derived from the contract's "
            "logic, covering edge cases and potential vulnerabilities."
            "Smart Contracts in scope and defined propreties:\n\n"
            f"{solidity_code}\n\n"
        )

        completion = client.chat.completions.create(
            model="o3-mini-2025-01-31",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        seeds = completion.choices[0].message.content
        with open(output_file, "x") as f:
            f.write(seeds)
        print(f"Seed values successfully generated and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python seed_generator.py '<input_files>' <output_file>")
        print("Example: python seed_generator.py 'file1.sol file2.sol' output.txt")
    else:
        input_files = sys.argv[1]
        merged_result = merge_solidity_files(input_files)
        if merged_result:   
            analyze_smart_contract_and_generate_seeds(merged_result, sys.argv[2])

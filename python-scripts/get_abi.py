import subprocess
import json
import sys
import os

def get_contract_abi(contract_name):
    try:
        # Run 'forge inspect' to get the ABI
        result = subprocess.run(
            ["forge", "inspect", contract_name, "abi"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse and format ABI
        abi = json.loads(result.stdout)
        return abi

    except subprocess.CalledProcessError as e:
        print(f"Error running forge inspect: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Failed to parse ABI JSON.")
        sys.exit(1)

def save_abi(contract_name, abi):
    # Ensure the output directory exists
    output_dir = "abi"
    os.makedirs(output_dir, exist_ok=True)

    # Save the ABI as a JSON file
    file_path = os.path.join(output_dir, f"{contract_name}.abi.json")
    with open(file_path, "w") as f:
        json.dump(abi, f, indent=4)

    print(f"ABI saved to {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_abi.py <ContractName>")
        sys.exit(1)

    contract_name = sys.argv[1]
    abi = get_contract_abi(contract_name)
    save_abi(contract_name, abi)

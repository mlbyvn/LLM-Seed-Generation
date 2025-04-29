// SPDX-License-Identifier: AGPL-3.0

// @author Trail of Bits (https://github.com/crytic/building-secure-contracts/blob/master/program-analysis/echidna/advanced/collecting-a-corpus.md)
pragma solidity ^0.8.0;

contract C {
    bool value_found = false;

    function magic(uint256 magic_1, uint256 magic_2, uint256 magic_3, uint256 magic_4) public {
        require(magic_1 == 42);
        require(magic_2 == 129);
        require(magic_3 == magic_4 + 333);
        value_found = true;
        return;
    }

    // @dev Echidna property is broken if magic() is called with correct magic values.
    // That means Echidna must guess those
    function echidna_magic_values() public view returns (bool) {
        return !value_found;
    }
}

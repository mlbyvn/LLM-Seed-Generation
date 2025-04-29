// SPDX-License-Identifier: MIT

// @dev Needed to set up all the contracts, balances and approvals to run tests

pragma solidity 0.8.20;

import { SwapPool } from "./src/SwapPool.sol";
import { ERC20Mock } from "./test/mocks/ERC20Mock.sol";
import { PoolFactory } from "./src/PoolFactory.sol";

contract Users {
    function proxy(address target, bytes memory _calldata) public returns (bool success, bytes memory returnData) {
        (success, returnData) = address(target).call(_calldata);
    }
}

contract SetUp {
    SwapPool pool;
    ERC20Mock weth;
    ERC20Mock poolToken;
    PoolFactory factory;
    Users liquidityPlovider;
    Users swapper;

    int256 constant STARTING_X = 10e18;
    int256 constant STARTING_Y = 10e18;

    constructor() {
        // Set up the contracts
        weth = new ERC20Mock();
        poolToken = new ERC20Mock();
        factory = new PoolFactory(address(weth));
        pool = SwapPool(factory.createPool(address(poolToken)));
        liquidityPlovider = new Users();
        swapper = new Users();

        // Mint tokens
        poolToken.mint(address(this), uint256(STARTING_X));
        weth.mint(address(this), uint256(STARTING_Y));

        // Approve transactions
        poolToken.approve(address(pool), type(uint256).max);
        weth.approve(address(pool), type(uint256).max);

        // Deposit into the pool, give the starting X and Y balances
        pool.deposit(uint256(STARTING_Y), uint256(STARTING_Y), uint256(STARTING_X), uint64(block.timestamp));
    }

    /*//////////////////////////////////////////////////////////////
                            HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function _between(uint256 val, uint256 lower, uint256 upper) internal pure returns (uint256) {
        return lower + (val % (upper - lower + 1));
    }

    function _init(address _user, uint256 _wethAmount, uint256 _poolTokenAmount) internal {
        weth.mint(_user, _wethAmount);
        poolToken.mint(_user, _poolTokenAmount);
    }

    function _doApprovals() internal {
        liquidityPlovider.proxy(
            address(weth), abi.encodeWithSelector(weth.approve.selector, address(pool), type(uint256).max)
        );
        liquidityPlovider.proxy(
            address(poolToken), abi.encodeWithSelector(poolToken.approve.selector, address(pool), type(uint256).max)
        );
    }
}

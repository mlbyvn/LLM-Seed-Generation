// SPDX-License-Identifier: MIT

pragma solidity 0.8.20;

import "./Setup.sol";

contract EchidnaTestAMM is SetUp {
    event logUints(int256 expected, int256 actual);

    int256 public startingY;
    int256 public startingX;
    int256 public expectedDeltaY;
    int256 public expectedDeltaX;
    int256 public endingY;
    int256 public endingX;
    int256 public actualDeltaX;
    int256 public actualDeltaY;

    uint256 constant POOL_BOUND = 1e22;

    function test_deposit(uint256 wethAmount) public {
        // let's make sure it's a reasonable amount avoiding weird overflows
        uint256 minWeth = pool.getMinimumWethDepositAmount();
        wethAmount = _between(wethAmount, minWeth, type(uint64).max);

        startingY = int256(weth.balanceOf(address(pool)));
        startingX = int256(poolToken.balanceOf(address(pool)));
        expectedDeltaY = int256(wethAmount);
        expectedDeltaX = int256(pool.getPoolTokensToDepositBasedOnWeth(wethAmount));

        //deposit for LP
        _init(address(liquidityPlovider), wethAmount, uint256(expectedDeltaX));
        _doApprovals();

        // Call
        (bool success,) = liquidityPlovider.proxy(
            address(pool),
            abi.encodeWithSelector(
                pool.deposit.selector, wethAmount, 0, uint256(expectedDeltaX), uint64(block.timestamp)
            )
        );

        if (!success) {
            return;
        }

        endingY = int256(weth.balanceOf(address(pool)));
        endingX = int256(poolToken.balanceOf(address(pool)));

        actualDeltaY = int256(endingY) - int256(startingY);
        actualDeltaX = int256(endingX) - int256(startingX);

        assert(actualDeltaX == expectedDeltaX);
        assert(actualDeltaY == expectedDeltaY);
    }

    function test_swapPoolTokenForTheWethBasedOnOutputWeth(uint256 outputWeth) public {
        outputWeth = _between(outputWeth, pool.getMinimumWethDepositAmount(), weth.balanceOf(address(pool)));

        if (outputWeth == 0) {
            return;
        }
        // delta X
        // ∆x = (β/(1-β)) * x
        uint256 poolTokenAmount = pool.getInputAmountBasedOnOutput(
            outputWeth, poolToken.balanceOf(address(pool)), weth.balanceOf(address(pool))
        );

        if (poolTokenAmount >= POOL_BOUND) {
            return;
        }

        startingY = int256(weth.balanceOf(address(pool)));
        startingX = int256(poolToken.balanceOf(address(pool)));
        expectedDeltaY = int256(-1) * int256(outputWeth);
        expectedDeltaX = int256(poolTokenAmount);

        poolToken.mint(address(swapper), 1e30);

        if (poolToken.balanceOf(address(swapper)) < poolTokenAmount) {
            poolToken.mint(address(swapper), poolTokenAmount - poolToken.balanceOf(address(swapper)) + 1);
        }

        swapper.proxy(
            address(poolToken), abi.encodeWithSelector(poolToken.approve.selector, address(pool), type(uint256).max)
        );

        // Call
        (bool success,) = swapper.proxy(
            address(pool),
            abi.encodeWithSelector(pool.swapExactOutput.selector, poolToken, weth, outputWeth, uint64(block.timestamp))
        );

        if (!success) {
            return;
        }

        endingY = int256(weth.balanceOf(address(pool)));
        endingX = int256(poolToken.balanceOf(address(pool)));

        actualDeltaY = int256(endingY) - int256(startingY);
        actualDeltaX = int256(endingX) - int256(startingX);

        emit logUints(expectedDeltaX, actualDeltaX);
        emit logUints(expectedDeltaY, actualDeltaY);

        assert(actualDeltaX == expectedDeltaX);
        assert(actualDeltaY == expectedDeltaY);
    }

    function test_getExactInputFromOutputDoesNotRevert(uint256 output) public view {
        output = _between(output, 1, 100e18 - 1);
        try pool.getInputAmountBasedOnOutput(output, 100e18, 100e18) { }
        catch {
            assert(false);
        }
    }
}

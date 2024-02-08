Problem description of "Perfect Squares" can be found [here](https://leetcode.com/problems/perfect-squares/) and its solution [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Python%20Solutions/Perfect%20Squares/perfect.py).

## Implementation

The Python solution initializes a dynamic programming array `dp` where `dp[i]` represents the minimum number of perfect square numbers that sum to `i`. It iteratively fills this array by considering all square numbers less than the current number `i` and finding the minimum count. The solution leverages the dynamic programming approach to efficiently compute the answer by building from smaller subproblems to the larger problem.
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)  # Initialize DP array with 0's

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - j])  # Find max in the last j elements
                dp[i] = max(dp[i], dp[i - j] + max_val * j)  # Update dp[i]

        return dp[n]  # Return the maximum sum after partitioning

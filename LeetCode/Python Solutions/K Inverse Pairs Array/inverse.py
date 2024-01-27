class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7  # Modulus for large numbers

        # Initialize DP table with zeros
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: 1 way to form an empty array

        # Iterate over array sizes from 1 to n
        for i in range(1, n + 1):
            cum_sum = 0  # Initialize cumulative sum for the current row
            # Iterate over the number of inverse pairs from 0 to k
            for j in range(k + 1):
                cum_sum += dp[i - 1][j]  # Add the number of ways from the previous row
                if j >= i:
                    cum_sum -= dp[i - 1][j - i]  # Subtract the number of ways exceeding the inverse pair limit
                dp[i][j] = cum_sum % MOD  # Update the DP table and apply modulus

        return dp[n][k]  # Return the number of ways for n elements and k inverse pairs

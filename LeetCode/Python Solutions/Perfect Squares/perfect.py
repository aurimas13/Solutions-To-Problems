class Solution:
    def numSquares(self, n: int) -> int:
        # DP array initialized with infinity for all indexes
        dp = [float('inf')] * (n + 1)
        
        # Base case: 0 can be represented by 0 squares
        dp[0] = 0
        
        # Iterate through all numbers from 1 to n to fill the dp array
        for i in range(1, n + 1):
            # Try all square numbers less than i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]

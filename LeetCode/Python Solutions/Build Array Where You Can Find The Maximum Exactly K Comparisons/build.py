class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize the dp array
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case
        for j in range(1, m + 1):
            dp[1][j][1] = 1
            
        # Fill the dp array using the transition
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for l in range(1, k + 1):
                    dp[i][j][l] = (dp[i][j][l] + j * dp[i-1][j][l]) % MOD
                    for p in range(1, j):  # Updated transition
                        dp[i][j][l] = (dp[i][j][l] + dp[i-1][p][l-1]) % MOD
        
        # Calculate the answer
        ans = 0
        for j in range(1, m + 1):
            ans = (ans + dp[n][j][k]) % MOD
        
        return ans

# Test the failed testcase
solution = Solution()
solution.numOfArrays(50, 100, 25)

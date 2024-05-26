class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k] where i is the length, j is the number of 'A's, k is the consecutive 'L's
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P'
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    # Add 'A'
                    if j > 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-1][j-1][k]) % MOD
                    # Add 'L'
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
        
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
                
        return result

# Example usage:
sol = Solution()
print(sol.checkRecord(2))  # Output: 8

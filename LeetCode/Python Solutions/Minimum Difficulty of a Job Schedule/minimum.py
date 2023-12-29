class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        # Initialize the dp array with infinity
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                max_difficulty = 0
                for k in range(i - 1, j - 2, -1):
                    # Update the max difficulty for the current day
                    max_difficulty = max(max_difficulty, jobDifficulty[k])
                    # Update the dp value considering the difficulty of the last job on the jth day
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max_difficulty)

        return dp[n][d] if dp[n][d] != float('inf') else -1
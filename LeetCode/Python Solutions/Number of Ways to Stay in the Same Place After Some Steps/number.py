class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        maxPoint = min(arrLen - 1, steps)  # The farthest point you can reach

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if j == 0:
                return 1 if i == 0 else 0
            if i < 0 or i > maxPoint:
                return 0  # invalid, outside the boundary
            # Current state is the sum of the three possible moves
            return (dp(i - 1, j - 1) + dp(i + 1, j - 1) + dp(i, j - 1)) % mod

        return dp(0, steps)


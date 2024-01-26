class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(move, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if move == 0:
                return 0
            return (dp(move - 1, i + 1, j) + dp(move - 1, i - 1, j) +
                    dp(move - 1, i, j + 1) + dp(move - 1, i, j - 1)) % MOD

        return dp(maxMove, startRow, startColumn)

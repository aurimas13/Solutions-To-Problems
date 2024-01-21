from typing import List


class Solution:
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        # base case
        if not obstacleGrid:
            return 0

        # if destination is blocked
        if obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # number of ways to reach last box, if only last box was present
        dp[-1][-1] = 1

        # all cells in last column to reach destination
        for i in reversed(range(m - 1)):
            if not obstacleGrid[i][-1] and dp[i + 1][-1]:
                dp[i][-1] = 1

        # all cells in last row to reach destination
        for j in reversed(range(n - 1)):
            if not obstacleGrid[-1][j] and dp[-1][j + 1]:
                dp[-1][j] = 1

        # number of ways to reach any intermediate block depends on i+1, j and i, j+1
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.uniquePathsWithObstacles(obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] -> 2
    # obstacleGrid = [[0, 1], [0, 0]] -> 1
    print(Solve)

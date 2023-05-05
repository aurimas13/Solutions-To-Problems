from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]


# Tests:
if __name__ == '__main__':
    def test_solution():
        s = Solution()
        
        assert s.uniquePaths(3, 2) == 3
        assert s.uniquePaths(3, 7) == 28
        assert s.uniquePaths(7, 3) == 28
        assert s.uniquePaths(1, 1) == 1
        assert s.uniquePaths(5, 5) == 70
        assert s.uniquePaths(5, 1) == 1
        assert s.uniquePaths(1, 5) == 1

    test_solution()
    print('All tests passed')
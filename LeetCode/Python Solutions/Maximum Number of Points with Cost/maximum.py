class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]
        
        for i in range(1, m):
            new_dp = [0] * n
            left_max = 0
            
            # Left to right
            for j in range(n):
                left_max = max(left_max - 1, dp[j])
                new_dp[j] = left_max + points[i][j]
            
            right_max = 0
            # Right to left
            for j in range(n - 1, -1, -1):
                right_max = max(right_max - 1, dp[j])
                new_dp[j] = max(new_dp[j], right_max + points[i][j])
            
            dp = new_dp
        
        return max(dp)
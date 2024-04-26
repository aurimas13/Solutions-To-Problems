from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        prev = grid[0]
        
        for i in range(1, n):
            # Initialize left and right cumulative minimum arrays
            leftMin = [0] * n
            rightMin = [0] * n
            leftMin[0] = prev[0]
            rightMin[-1] = prev[-1]
            
            for j in range(1, n):
                leftMin[j] = min(leftMin[j-1], prev[j])
            for j in range(n-2, -1, -1):
                rightMin[j] = min(rightMin[j+1], prev[j])
            
            # Calculate the current row's dp values
            curr = [0] * n
            for j in range(n):
                min_except_current = float('inf')
                if j > 0:
                    min_except_current = min(min_except_current, leftMin[j-1])
                if j < n - 1:
                    min_except_current = min(min_except_current, rightMin[j+1])
                
                curr[j] = grid[i][j] + min_except_current
            
            # Update prev to the current dp row for the next iteration
            prev = curr
        
        return min(prev)

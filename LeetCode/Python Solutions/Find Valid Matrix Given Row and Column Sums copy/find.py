from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                min_val = min(rowSum[i], colSum[j])
                matrix[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        
        return matrix

# Example usage:
sol = Solution()
print(sol.restoreMatrix([3, 8], [4, 7]))  # Output: [[3, 0], [1, 7]]
print(sol.restoreMatrix([5, 7, 10], [8, 6, 8]))  # Output: [[0, 5, 0], [6, 1, 0], [2, 0, 8]]

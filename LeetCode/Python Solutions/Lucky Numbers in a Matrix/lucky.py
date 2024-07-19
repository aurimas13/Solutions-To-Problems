from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_row = {min(row) for row in matrix}
        max_col = {max(col) for col in zip(*matrix)}
        
        return list(min_row & max_col)

# Example usage:
sol = Solution()
print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))  # Output: [15]
print(sol.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))  # Output: [12]
print(sol.luckyNumbers([[7,8],[1,2]]))  # Output: [7]

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0

        # Preprocess the matrix
        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Find the largest area for each row
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                max_area = max(max_area, row[j] * (j + 1))

        return max_area

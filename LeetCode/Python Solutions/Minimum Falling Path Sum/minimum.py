class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Starting from the second row, update each element
        for i in range(1, n):
            for j in range(n):
                # Check left diagonal, directly above and right diagonal
                left_diagonal = matrix[i - 1][j - 1] if j > 0 else float('inf')
                right_diagonal = matrix[i - 1][j + 1] if j < n - 1 else float('inf')
                directly_above = matrix[i - 1][j]

                # Update the matrix with the minimum sum of the falling path to this element
                matrix[i][j] += min(left_diagonal, directly_above, right_diagonal)

        # The answer is the minimum value in the last row
        return min(matrix[-1])

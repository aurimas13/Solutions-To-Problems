class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Number of rows and columns in the original matrix
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the transposed matrix with swapped dimensions
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]

        # Iterate through the matrix and transpose
        for r in range(rows):
            for c in range(cols):
                transposed[c][r] = matrix[r][c]

        return transposed

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0

        # Calculate prefix sums for each row
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i - 1]

        # Iterate over all pairs of columns
        for i in range(n):
            for j in range(i, n):
                submatrix_sums = {0: 1}
                curr_sum = 0

                # Calculate the sum of submatrices for the current column pair
                for k in range(m):
                    curr_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += submatrix_sums.get(curr_sum - target, 0)
                    submatrix_sums[curr_sum] = submatrix_sums.get(curr_sum, 0) + 1

        return count

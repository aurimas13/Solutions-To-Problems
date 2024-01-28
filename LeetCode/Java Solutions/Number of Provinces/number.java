import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int count = 0;

        // Calculate prefix sums for each row
        for (int[] row : matrix) {
            for (int i = 1; i < n; i++) {
                row[i] += row[i - 1];
            }
        }

        // Iterate over all pairs of columns
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                Map<Integer, Integer> submatrixSums = new HashMap<>();
                submatrixSums.put(0, 1);
                int currSum = 0;

                // Calculate the sum of submatrices for the current column pair
                for (int k = 0; k < m; k++) {
                    currSum += matrix[k][j] - (i > 0 ? matrix[k][i - 1] : 0);
                    count += submatrixSums.getOrDefault(currSum - target, 0);
                    submatrixSums.put(currSum, submatrixSums.getOrDefault(currSum, 0) + 1);
                }
            }
        }

        return count;
    }
}

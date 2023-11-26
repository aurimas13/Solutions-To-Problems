public class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int maxArea = 0;

        // Preprocess the matrix
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < m; i++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }

        // Find the largest area for each row
        for (int i = 0; i < m; i++) {
            // Sort the row
            Arrays.sort(matrix[i]);

            // Calculate the area that can be formed with each cell as the height of the submatrix
            for (int j = n - 1; j >= 0; j--) {
                int height = matrix[i][j];
                int width = n - j;
                maxArea = Math.max(maxArea, height * width);
            }
        }

        return maxArea;
    }
}

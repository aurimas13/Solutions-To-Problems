class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;

        // Start from the second row and update each element
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Check left diagonal, directly above, and right diagonal
                int leftDiagonal = j > 0 ? matrix[i - 1][j - 1] : Integer.MAX_VALUE;
                int rightDiagonal = j < n - 1 ? matrix[i - 1][j + 1] : Integer.MAX_VALUE;
                int directlyAbove = matrix[i - 1][j];

                // Update the matrix with the minimum sum of the falling path to this element
                matrix[i][j] += Math.min(Math.min(leftDiagonal, directlyAbove), rightDiagonal);
            }
        }

        // Find the minimum value in the last row
        int minSum = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            minSum = Math.min(minSum, matrix[n - 1][j]);
        }
        return minSum;
    }
}

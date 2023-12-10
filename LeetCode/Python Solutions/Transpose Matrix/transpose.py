class Solution {
    public int[][] transpose(int[][] matrix) {
        // Number of rows and columns in the original matrix
        int rows = matrix.length, cols = matrix[0].length;

        // Initialize the transposed matrix with swapped dimensions
        int[][] transposed = new int[cols][rows];

        // Iterate through the matrix and transpose
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                transposed[c][r] = matrix[r][c];
            }
        }

        return transposed;
    }
}

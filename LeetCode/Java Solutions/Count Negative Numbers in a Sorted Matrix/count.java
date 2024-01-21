class Solution {
    /**
     * Counts the number of negative numbers in a matrix sorted in non-increasing order.
     *
     * @param grid The input matrix.
     * @return The number of negative numbers.
     */
    public int countNegatives(int[][] grid) {
        // Corner case: if the grid is null or empty, return 0
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int rowCount = grid.length;
        int colCount = grid[0].length;

        // Start from the top-right corner of the matrix
        int row = 0;
        int col = colCount - 1;

        // Counter for negative numbers
        int negativeCount = 0;

        // Traverse the matrix
        while (row < rowCount && col >= 0) {
            // If the current element is negative
            if (grid[row][col] < 0) {
                // All elements below this element in the current column are negative
                // (as columns are sorted in non-increasing order).
                // So, add the number of elements below it to the negative count.
                negativeCount += rowCount - row;
                
                // Move to the left in the same row.
                col--;
            } else {
                // If the current element is non-negative,
                // move down to the next row.
                row++;
            }
        }

        return negativeCount;
    }

    // Example usage:
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] grid = {
            {4, 3, 2, -1},
            {3, 2, 1, -1},
            {1, 1, -1, -2},
            {-1, -1, -2, -3}
        };
        System.out.println(solution.countNegatives(grid));  // Output: 8
    }
}

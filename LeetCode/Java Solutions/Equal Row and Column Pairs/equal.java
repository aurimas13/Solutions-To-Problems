import java.util.HashMap;

class Solution {
    /**
     * Calculates the number of pairs of rows and columns in a 2D grid where each element in the row is equal
     * to some element in the column.
     *
     * @param  grid  a 2D array of integers representing the input grid
     * @return       the number of pairs of rows and columns where each element in the row is equal to some
     *               element in the column
     */
    public int equalPairs(int[][] grid) {
        int numberOfPairs = 0;
        int numberOfRows = grid.length;
        
        // Iterate through each row
        for (int rowIndex = 0; rowIndex < numberOfRows; rowIndex++) {
            
            // Create a map with key as column index and value as the element
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int colIndex = 0; colIndex < numberOfRows; colIndex++) {
                map.put(colIndex, grid[rowIndex][colIndex]);
            }
            
            // For each column, check if elements of the current row are equal to elements in the column
            for (int colIndex = 0; colIndex < numberOfRows; colIndex++) {
                if (isRowEqualToColumn(map, grid, colIndex)) {
                    numberOfPairs++;
                }
            }
        }
        return numberOfPairs;
    }
    
    // Method to check if elements of a row are equal to elements in a column
    private boolean isRowEqualToColumn(HashMap<Integer, Integer> rowElements, int[][] grid, int columnIndex) {
        for (int rowIndex = 0; rowIndex < grid.length; rowIndex++) {
            if (!rowElements.get(rowIndex).equals(grid[rowIndex][columnIndex])) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] grid1 = {{3, 2, 1}, {1, 7, 6}, {2, 7, 7}};
        System.out.println(solution.equalPairs(grid1)); // Output should be 1

        int[][] grid2 = {{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}};
        System.out.println(solution.equalPairs(grid2)); // Output should be 3
    }
}

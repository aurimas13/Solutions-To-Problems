class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length - 2; i++) {
            for (int j = 0; j < grid[0].length - 2; j++) {
                if (isMagicSquare(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isMagicSquare(int[][] grid, int i, int j) {
        // Check if all numbers are from 1 to 9
        boolean[] used = new boolean[10];
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                int num = grid[x][y];
                if (num < 1 || num > 9 || used[num]) {
                    return false;
                }
                used[num] = true;
            }
        }

        // Check rows, columns, and diagonals
        int target = grid[i][j] + grid[i][j+1] + grid[i][j+2];
        for (int x = 0; x < 3; x++) {
            if (grid[i+x][j] + grid[i+x][j+1] + grid[i+x][j+2] != target) return false;
            if (grid[i][j+x] + grid[i+1][j+x] + grid[i+2][j+x] != target) return false;
        }
        return grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == target &&
               grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == target;
    }
}
public class Solution {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] maxLocal = new int[n - 2][n - 2];
        
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                int maxVal = 0;
                // Iterate through the 3x3 sub-matrix
                for (int r = i; r < i + 3; r++) {
                    for (int c = j; c < j + 3; c++) {
                        maxVal = Math.max(maxVal, grid[r][c]);
                    }
                }
                maxLocal[i][j] = maxVal;
            }
        }
        
        return maxLocal;
    }
}


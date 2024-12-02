class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Using boolean array to track reachable cells
        boolean[][] dp = new boolean[m][n];
        
        // First column cells are reachable
        for (int i = 0; i < m; i++) {
            dp[i][0] = true;
        }
        
        int maxMoves = 0;
        
        // Process column by column
        for (int j = 0; j < n - 1; j++) {
            boolean hasMoves = false;
            
            for (int i = 0; i < m; i++) {
                // If current cell is reachable
                if (dp[i][j]) {
                    // Try all three possible moves
                    for (int k = Math.max(0, i - 1); k <= Math.min(m - 1, i + 1); k++) {
                        if (grid[k][j + 1] > grid[i][j]) {
                            if (!dp[k][j + 1]) {  // If not already marked reachable
                                dp[k][j + 1] = true;
                                hasMoves = true;
                                maxMoves = Math.max(maxMoves, j + 1);
                            }
                        }
                    }
                }
            }
            
            // If no moves possible from this column, break
            if (!hasMoves) {
                break;
            }
        }
        
        return maxMoves;
    }
}
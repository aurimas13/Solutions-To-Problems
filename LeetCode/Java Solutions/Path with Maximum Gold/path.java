public class Solution {
    public int getMaximumGold(int[][] grid) {
        int maxGold = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > 0) {
                    maxGold = Math.max(maxGold, dfs(grid, i, j));
                }
            }
        }
        
        return maxGold;
    }
    
    private int dfs(int[][] grid, int x, int y) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == 0) {
            return 0;
        }
        
        int gold = grid[x][y];
        grid[x][y] = 0; // Mark as visited
        
        int maxGold = 0;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            maxGold = Math.max(maxGold, dfs(grid, x + dx[i], y + dy[i]));
        }
        
        grid[x][y] = gold; // Backtrack
        
        return gold + maxGold;
    }
}

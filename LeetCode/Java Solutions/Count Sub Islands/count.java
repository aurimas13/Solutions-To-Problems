class Solution {
    private int m, n;
    private int[][] grid1, grid2;
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        this.m = grid1.length;
        this.n = grid1[0].length;
        this.grid1 = grid1;
        this.grid2 = grid2;

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid2[i][j] == 1 && dfs(i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean dfs(int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid2[i][j] == 0) {
            return true;
        }

        grid2[i][j] = 0;  // Mark as visited
        boolean isSubIsland = grid1[i][j] == 1;

        for (int[] dir : directions) {
            isSubIsland &= dfs(i + dir[0], j + dir[1]);
        }

        return isSubIsland;
    }
}
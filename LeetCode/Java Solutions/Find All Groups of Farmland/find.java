public class Solution {
    /**
     * Given a 2D integer array representing a map of land, where 1 represents
     * farmland and 0 represents water, returns an array of integers where
     * each element represents the bounding coordinates of a group of adjacent
     * farmland.
     *
     * @param grid the 2D integer array representing the map of land
     * @return an array of integer arrays, where each subarray represents the
     *         bounding coordinates of a group of adjacent farmland
     */
        public int[][] findFarmland(int[][] grid) {
            int rows = grid.length;    // number of rows in the grid
            int cols = grid[0].length;// number of columns in the grid
            boolean[][] visited = new boolean[rows][cols];// whether each cell has been visited
            List<int[]> farmland = new ArrayList<>();// final result
            // iterate through each cell in the grid
            for (int r = 0; r < rows; ++r) {
                for (int c = 0; c < cols; ++c) {
                    // if the current cell is farmland and has not been visited
                    if (grid[r][c] == 1 && !visited[r][c]) {
                        int[] bounds = {r, c, r, c};// [top, left, bottom, right]
                        dfs(grid, visited, r, c, bounds);
                        farmland.add(new int[] {bounds[0], bounds[1], bounds[2], bounds[3]});
                    }
                }
            }
            return farmland.toArray(new int[farmland.size()][4]);
        }
        private void dfs(int[][] land, boolean[][] visited, int r, int c, int[] bounds) {
            if (r < 0 || r >= land.length || c < 0 || c >= land[0].length || visited[r][c] || land[r][c] == 0)
                return;
            visited[r][c] = true;
            bounds[0] = Math.min(bounds[0], r);
            bounds[1] = Math.min(bounds[1], c);
            bounds[2] = Math.max(bounds[2], r);
            bounds[3] = Math.max(bounds[3], c);
            dfs(land, visited, r + 1, c, bounds);
            dfs(land, visited, r - 1, c, bounds);
            dfs(land, visited, r, c + 1, bounds);
            dfs(land, visited, r, c - 1, bounds);
        }
    }
    
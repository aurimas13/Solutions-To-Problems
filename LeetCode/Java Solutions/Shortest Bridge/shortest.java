import java.util.*;

public class Solution {
    private int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private Queue<int[]> queue = new LinkedList<>();

    public int shortestBridge(int[][] grid) {
        int n = grid.length;

        // Start DFS to find the first island and color it with 2.
        boolean found = false;
        for (int i = 0; i < n; i++) {
            if (found) break;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dfs(grid, i, j);
                    found = true;
                    break;
                }
            }
        }

        // BFS to expand the first island until it reach the second one.
        int level = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] cur = queue.poll();
                for (int[] dir : dirs) {
                    int nx = cur[0] + dir[0];
                    int ny = cur[1] + dir[1];
                    if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                        if (grid[nx][ny] == 1) {
                            return level;
                        }
                        if (grid[nx][ny] == 0) {
                            grid[nx][ny] = 2;
                            queue.offer(new int[]{nx, ny});
                        }
                    }
                }
            }
            level++;
        }
        return -1;
    }

    private void dfs(int[][] grid, int x, int y) {
        // If out of bounds or not island, return.
        if (x < 0 || y < 0 || x >= grid.length || y >= grid.length || grid[x][y] != 1) {
            return;
        }
        // Color the island with 2 and add it into the queue.
        grid[x][y] = 2;
        queue.offer(new int[]{x, y});
        for (int[] dir : dirs) {
            dfs(grid, x + dir[0], y + dir[1]);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] grid = {{0, 1, 0}, {0, 0, 0}, {0, 0, 1}};
        System.out.println(solution.shortestBridge(grid));
    }
}




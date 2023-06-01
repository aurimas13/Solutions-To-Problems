import java.util.*;

public class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }

        int[][] directions = new int[][] {
            {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}
        };

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 1});  // x, y, path_length

        grid[0][0] = 1;  // mark as visited

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1], path_length = cell[2];

            if (x == n - 1 && y == n - 1) {
                return path_length;
            }

            for (int[] direction : directions) {
                int new_x = x + direction[0];
                int new_y = y + direction[1];

                if (new_x >= 0 && new_x < n && new_y >= 0 && new_y < n && grid[new_x][new_y] == 0) {
                    grid[new_x][new_y] = 1;  // mark as visited
                    queue.offer(new int[]{new_x, new_y, path_length + 1});
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        // Test case 1
        int[][] grid1 = new int[][]{{0, 1}, {1, 0}};
        assert solution.shortestPathBinaryMatrix(grid1) == 2;

        // Test case 2
        int[][] grid2 = new int[][]{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}};
        assert solution.shortestPathBinaryMatrix(grid2) == -1;

        System.out.println("All test cases passed!");
    }
}

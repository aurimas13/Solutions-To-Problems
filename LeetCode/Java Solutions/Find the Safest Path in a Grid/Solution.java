import java.util.*;

public class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] intGrid = new int[n][n];
        
        // Convert List<List<Integer>> to int[][]
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                intGrid[i][j] = grid.get(i).get(j);
            }
        }

        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        Queue<int[]> queue = new LinkedList<>();

        // Step 1: BFS to calculate distances from thieves
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (intGrid[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                    dist[i][j] = 0;
                }
            }
        }

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];
            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] == Integer.MAX_VALUE) {
                    dist[nx][ny] = dist[x][y] + 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        // Step 2: Binary search to find maximum safeness factor
        int low = 0, high = Arrays.stream(dist).flatMapToInt(Arrays::stream).max().orElse(0);
        while (low < high) {
            int mid = (low + high + 1) / 2;
            if (canReachWithSafeness(dist, mid, n)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        return low;
    }

    private boolean canReachWithSafeness(int[][] dist, int safeness, int n) {
        if (dist[0][0] < safeness || dist[n-1][n-1] < safeness) return false;

        boolean[][] visited = new boolean[n][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];
            if (x == n - 1 && y == n - 1) return true;
            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] && dist[nx][ny] >= safeness) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {
        List<List<Integer>> grid = Arrays.asList(
            Arrays.asList(1, 0, 0),
            Arrays.asList(0, 0, 0),
            Arrays.asList(0, 0, 1)
        );

        Solution sol = new Solution();
        System.out.println(sol.maximumSafenessFactor(grid));  // Output should be 0
    }
}

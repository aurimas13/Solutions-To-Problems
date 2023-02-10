import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        if (n == 0) return -1;

        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    q.offer(new int[] {i, j});
                }
            }
        }
        if (q.isEmpty() || q.size() == n * n) return -1;

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int res = -1;
        while (!q.isEmpty()) {
            res++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cur = q.poll();
                for (int[] dir : dirs) {
                    int x = cur[0] + dir[0];
                    int y = cur[1] + dir[1];
                    if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 0) {
                        q.offer(new int[] {x, y});
                        grid[x][y] = 1;
                    }
                }
            }
        }
        return res;
    }
}
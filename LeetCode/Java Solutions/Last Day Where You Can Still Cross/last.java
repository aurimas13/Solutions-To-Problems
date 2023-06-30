import java.util.*;

class Solution {
    private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    
    public int latestDayToCross(int row, int col, int[][] cells) {
        // Convert the cell positions from 1-based to 0-based
        for (int i = 0; i < cells.length; i++) {
            cells[i][0]--;
            cells[i][1]--;
        }

        // Binary search the maximum day
        int lo = 1, hi = cells.length;
        while (lo <= hi) {
            int mi = lo + (hi - lo) / 2;  // Calculate the mid day
            
            // Initialize the matrix as all land
            int[][] matrix = new int[row][col];
            
            // Flood the cells according to the cells list
            for (int i = 0; i < mi; i++) {
                matrix[cells[i][0]][cells[i][1]] = 1;
            }

            // Apply BFS to check if it's possible to walk from the top to the bottom on the mid day
            Queue<int[]> queue = new LinkedList<>();
            for (int i = 0; i < col; i++) {
                if (matrix[0][i] == 0) {
                    queue.offer(new int[] {i, 0});
                }
            }
            boolean[][] visited = new boolean[row][col];
            boolean reachedBottom = false;
            while (!queue.isEmpty()) {
                int[] cell = queue.poll();
                int x = cell[0], y = cell[1];
                visited[y][x] = true;
                if (y == row - 1) {  // If we can reach the bottom row
                    reachedBottom = true;
                    break;
                }
                for (int[] direction : DIRECTIONS) {
                    int nx = x + direction[0], ny = y + direction[1];
                    if (nx >= 0 && nx < col && ny >= 0 && ny < row && matrix[ny][nx] == 0 && !visited[ny][nx]) {
                        queue.offer(new int[] {nx, ny});
                    }
                }
            }
            if (reachedBottom) {  // If we can reach the bottom row
                lo = mi + 1;  // Try to find a larger day
            } else {  // If we cannot reach the bottom row
                hi = mi - 1;  // Try to find a smaller day
            }
        }

        return hi;  // Return the maximum day when it's still possible to walk from the top to the bottom
    }
}

import java.util.*;

class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        // Define the four cardinal directions: left, right, up, and down
        int[][] directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        
        // Convert the cell positions from 1-based to 0-based
        for (int i = 0; i < cells.length; i++) {
            cells[i][0] -= 1;
            cells[i][1] -= 1;
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
                    queue.add(new int[]{i, 0});
                }
            }
            boolean[][] visited = new boolean[row][col];
            for (int[] point : queue) {
                visited[point[1]][point[0]] = true;
            }
            boolean canReach = false;
            while (!queue.isEmpty()) {
                int[] point = queue.poll();
                if (point[1] == row - 1) {  // If we can reach the bottom row
                    canReach = true;
                    lo = mi + 1;  // Try to find a larger day
                    break;
                }
                for (int[] direction : directions) {
                    int nx = point[0] + direction[0];
                    int ny = point[1] + direction[1];
                    if (0 <= nx && nx < col && 0 <= ny && ny < row && matrix[ny][nx] == 0 && !visited[ny][nx]) {
                        queue.add(new int[]{nx, ny});
                        visited[ny][nx] = true;
                    }
                }
            }
            if (!canReach) {  // If we cannot reach the bottom row
                hi = mi - 1;  // Try to find a smaller day
            }
        }

        return hi;  // Return the maximum day when it's still possible to walk from the top to the bottom
    }
}

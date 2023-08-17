import java.util.Queue;
import java.util.LinkedList;

public class Solution {
    public int[][] updateMatrix(int[][] mat) {
        // Initialize a queue to store the cells to be processed
        Queue<int[]> queue = new LinkedList<>();

        int m = mat.length;
        int n = mat[0].length;

        // Initialize the distance matrix with maximum integer values
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        // Add all the 0s in the matrix to the queue and set their distance to 0
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    queue.add(new int[] {i, j});
                    dist[i][j] = 0;
                }
            }
        }

        // Define directions for the BFS (Up, Down, Left, Right)
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // Perform breadth-first search
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int i = current[0], j = current[1];

            for (int[] dir : directions) {
                int x = i + dir[0], y = j + dir[1];
                // If the neighboring cell is within the matrix and has not been updated
                if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == Integer.MAX_VALUE) {
                    dist[x][y] = dist[i][j] + 1;
                    queue.add(new int[] {x, y});
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] mat = {{0,0,0},{0,1,0},{0,0,0}};
        int[][] result = sol.updateMatrix(mat);

        // Print the result
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[0].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}

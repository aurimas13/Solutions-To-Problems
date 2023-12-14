class Solution {

    // Define possible movement directions - up, down, left, right.
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int minimumEffortPath(int[][] heights) {

        // Initialize the search range for our binary search.
        int left = 0, right = 1000000;

        // Binary search: Continue until the range narrows down to a single value.
        while (left < right) {

            // Calculate the middle effort.
            int mid = (left + right) / 2;

            // Check if it's possible to reach the destination with the current effort.
            if (canReachDestination(heights, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        // The minimum effort required.
        return left;
    }

    // Helper function to check if we can reach the destination with the given effort.
    private boolean canReachDestination(int[][] heights, int maxEffort) {

        // Mark cells as visited or not.
        boolean[][] visited = new boolean[heights.length][heights[0].length];

        // Start DFS from the top-left corner.
        return dfs(heights, 0, 0, maxEffort, visited);
    }

    // Depth-First Search to explore the grid.
    private boolean dfs(int[][] heights, int i, int j, int maxEffort, boolean[][] visited) {

        // If we have reached the destination, return true.
        if (i == heights.length - 1 && j == heights[0].length - 1) return true;

        // Mark the current cell as visited.
        visited[i][j] = true;

        // Explore each direction.
        for (int[] dir : directions) {
            int x = i + dir[0], y = j + dir[1];

            // If the new cell is within bounds, not visited, and the absolute difference in 
            // heights is within the allowed effort, explore it.
            if (x >= 0 && x < heights.length && y >= 0 && y < heights[0].length && 
                !visited[x][y] && Math.abs(heights[i][j] - heights[x][y]) <= maxEffort) {
                if (dfs(heights, x, y, maxEffort, visited)) return true;
            }
        }

        // Return false if we cannot reach the destination.
        return false;
    }
}

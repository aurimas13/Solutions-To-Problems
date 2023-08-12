import java.util.Arrays;

public class Solution {
    
    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // Check if obstacleGrid is empty
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0) {
            return 0;
        }
        
        // Check if the destination is blocked
        if (obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1] == 1) {
            return 0;
        }

        // Dimensions of the matrix
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        // Create a 2D DP array to store results of subproblems
        int[][] dp = new int[m][n];
        for (int[] row : dp) {
            Arrays.fill(row, 0);
        }

        // If only the last cell was present, there's only one way to reach it
        dp[m - 1][n - 1] = 1;

        // Initialize paths for the last column
        for (int i = m - 2; i >= 0; i--) {
            if (obstacleGrid[i][n - 1] == 0 && dp[i + 1][n - 1] == 1) {
                dp[i][n - 1] = 1;
            }
        }

        // Initialize paths for the last row
        for (int j = n - 2; j >= 0; j--) {
            if (obstacleGrid[m - 1][j] == 0 && dp[m - 1][j + 1] == 1) {
                dp[m - 1][j] = 1;
            }
        }

        // Calculate number of ways to reach each intermediate cell
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                if (obstacleGrid[i][j] == 0) {
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1];
                }
            }
        }

        return dp[0][0];
    }

    public static void main(String[] args) {
        int[][] obstacleGrid = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
        System.out.println(uniquePathsWithObstacles(obstacleGrid)); // Expected output: 2
    }
}

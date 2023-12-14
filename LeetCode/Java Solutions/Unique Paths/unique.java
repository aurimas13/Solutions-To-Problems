public class Solution {
    // Function to calculate the number of unique paths
    public int uniquePaths(int m, int n) {
        // Create a 2D array 'dp' to store the number of unique paths at each cell
        int[][] dp = new int[m][n];
        
        // Initialize the first row and first column with 1, 
        // as there's only one way to reach any cell in the first row or first column
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Calculate the number of unique paths for each cell
        // by adding the number of paths from the cell above and the cell to the left
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // Return the number of unique paths to reach the bottom-right corner
        return dp[m-1][n-1];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        
        // Test cases
        assert s.uniquePaths(3, 2) == 3;
        assert s.uniquePaths(3, 7) == 28;
        assert s.uniquePaths(7, 3) == 28;
        assert s.uniquePaths(1, 1) == 1;
        assert s.uniquePaths(5, 5) == 70;
        assert s.uniquePaths(5, 1) == 1;
        assert s.uniquePaths(1, 5) == 1;
        
        System.out.println("All tests passed");
    }
}


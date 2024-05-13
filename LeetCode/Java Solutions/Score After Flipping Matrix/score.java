public class Solution {
    public int matrixScore(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        // Step 1: Ensure the first column has all 1s
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                for (int j = 0; j < n; j++) {
                    grid[i][j] ^= 1;
                }
            }
        }

        // Step 2: Maximize the 1s in each column from the second column onwards
        for (int j = 1; j < n; j++) {
            int countOnes = 0;
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1) {
                    countOnes++;
                }
            }
            if (countOnes < m - countOnes) {
                for (int i = 0; i < m; i++) {
                    grid[i][j] ^= 1;
                }
            }
        }

        // Calculate the final score
        int score = 0;
        for (int i = 0; i < m; i++) {
            int num = 0;
            for (int j = 0; j < n; j++) {
                num = (num << 1) | grid[i][j];
            }
            score += num;
        }

        return score;
    }
}

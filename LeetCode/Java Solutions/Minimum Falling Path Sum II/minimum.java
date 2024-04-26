class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        if (n == 1) return grid[0][0];

        int[] prev = grid[0];

        for (int i = 1; i < n; i++) {
            int[] leftMin = new int[n];
            int[] rightMin = new int[n];
            leftMin[0] = prev[0];
            rightMin[n-1] = prev[n-1];
            for (int j = 1; j < n; j++) {
                leftMin[j] = Math.min(leftMin[j-1], prev[j]);
            }
            for (int j = n-2; j >= 0; j--) {
                rightMin[j] = Math.min(rightMin[j+1], prev[j]);
            }
            
            int[] curr = new int[n];
            for (int j = 0; j < n; j++) {
                int minExceptCurrent = Integer.MAX_VALUE;
                if (j > 0) minExceptCurrent = Math.min(minExceptCurrent, leftMin[j-1]);
                if (j < n - 1) minExceptCurrent = Math.min(minExceptCurrent, rightMin[j+1]);
                
                curr[j] = grid[i][j] + minExceptCurrent;
            }
            
            prev = curr;
        }
        
        int minPathSum = Integer.MAX_VALUE;
        for (int value : prev) {
            minPathSum = Math.min(minPathSum, value);
        }
        return minPathSum;
    }
}

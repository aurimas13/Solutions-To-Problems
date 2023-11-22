import java.util.Arrays;

class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffixSum = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }

        int[][] memo = new int[n][n];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return dp(piles, 0, 1, memo, suffixSum);
    }

    private int dp(int[] piles, int i, int m, int[][] memo, int[] suffixSum) {
        if (i + 2 * m >= piles.length) {
            return suffixSum[i];
        }

        if (memo[i][m] != -1) {
            return memo[i][m];
        }

        int maxStones = Integer.MIN_VALUE;
        for (int x = 1; x <= 2 * m; x++) {
            int nextM = Math.max(m, x);
            maxStones = Math.max(maxStones, suffixSum[i] - dp(piles, i + x, nextM, memo, suffixSum));
        }

        memo[i][m] = maxStones;
        return maxStones;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example test cases
        int[] piles1 = {2, 7, 9, 4};
        System.out.println(solution.stoneGameII(piles1));  // Output: 10
        
        int[] piles2 = {1, 2, 3, 4, 5, 100};
        System.out.println(solution.stoneGameII(piles2));  // Output: 104
    }
}

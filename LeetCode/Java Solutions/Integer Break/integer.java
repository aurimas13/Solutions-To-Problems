public class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[i], Math.max(j, dp[j]) * Math.max(i - j, dp[i - j]));
            }
        }
        return dp[n];
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.integerBreak(10);
        System.out.println(result);  // Expected output: 36
    }
}

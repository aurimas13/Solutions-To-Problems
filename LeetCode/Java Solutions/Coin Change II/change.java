public class Solution {
    public int change(int amount, int[] coins) {
        // Create a DP array initialized with zeros, with size amount+1
        int[] dp = new int[amount + 1];
        
        // There's one way to make the amount 0 - by not using any coin.
        dp[0] = 1;
        
        // Loop through each coin
        for (int coin : coins) {
            // For each coin, iterate through amounts from the coin value up to the target amount
            for (int i = coin; i <= amount; i++) {
                // For each amount, add the number of ways it can be formed without the current coin
                dp[i] += dp[i - coin];
            }
        }
        
        // The target amount's index contains the total number of ways the amount can be formed using the given coins
        return dp[amount];
    }
}

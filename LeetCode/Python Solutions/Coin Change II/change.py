from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Create a DP array initialized with zeros, with size amount+1
        dp = [0] * (amount + 1)
        
        # There's one way to make the amount 0 - by not using any coin.
        dp[0] = 1
        
        # Loop through each coin
        for coin in coins:
            # For each coin, iterate through amounts from the coin value up to the target amount
            for i in range(coin, amount + 1):
                # For each amount, add the number of ways it can be formed without the current coin
                dp[i] += dp[i - coin]
                
        # The target amount's index contains the total number of ways the amount can be formed using the given coins
        return dp[amount]

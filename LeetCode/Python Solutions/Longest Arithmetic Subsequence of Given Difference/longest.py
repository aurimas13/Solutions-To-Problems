from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Initialize a dictionary to keep track of the longest sequence ending at each number
        dp = {}

        for num in arr:  # Iterate over the input list
            # If num - difference is not in dp, set dp[num] to 1
            # Else set dp[num] to dp[num - difference] + 1
            dp[num] = dp.get(num - difference, 0) + 1

        # Return the maximum value in dp
        return max(dp.values())

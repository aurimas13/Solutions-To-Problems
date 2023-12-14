from typing import List
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        This function takes a list of integers as input and returns the length of the longest arithmetic subsequence.
        The function accepts one parameter:
            1. nums (List[int]): A list of integers for which the longest arithmetic subsequence needs to be found.
        The function returns an integer representing the length of the longest arithmetic subsequence.
        """
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_length = 2  # Minimum length of arithmetic subsequence is 2

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_length = max(max_length, dp[i][diff])

        return max_length

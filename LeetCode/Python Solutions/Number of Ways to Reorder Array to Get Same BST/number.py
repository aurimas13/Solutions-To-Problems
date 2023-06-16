from math import comb
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def ways(nums: List[int]) -> int:
            if len(nums) <= 2: return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return comb(len(left) + len(right), len(left)) * ways(left) * ways(right) % (10**9 + 7)
        return ways(nums) - 1


from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)  # Use a set for fast lookup
        max_k = -1
        
        for num in nums:
            if num > 0 and -num in num_set:
                max_k = max(max_k, num)
                
        return max_k

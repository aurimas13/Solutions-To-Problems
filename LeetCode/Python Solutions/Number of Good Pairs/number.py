# O(n):
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Use a dictionary to count occurrences of each number
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Calculate number of good pairs
        count = 0
        for val in num_count.values():
            count += (val * (val - 1)) // 2
        
        return count


# or

# # O(n^2):
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] == nums[j] and i < j:
#                     count += 1
#         return count
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Initial candidates and counts
        candidate1, candidate2, count1, count2 = nums[0], None, 1, 0
        for num in nums[1:]:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        # Re-check the candidates in the array
        return [num for num in (candidate1, candidate2) 
                if nums.count(num) > len(nums) // 3]

# or

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         count = Counter(nums)
#         return [num for num, freq in count.items() if freq > len(nums) // 3]
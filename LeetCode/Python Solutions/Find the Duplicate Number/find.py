from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detecting the loop using Floyd's Cycle Detection
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Finding the starting point of the cycle
        hare = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return hare


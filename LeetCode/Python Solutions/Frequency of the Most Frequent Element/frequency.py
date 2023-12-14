from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        left, total, maxFreq = 0, 0, 0

        for right in range(len(nums)):
            total += nums[right]

            # Check if the total increments needed is more than k
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            maxFreq = max(maxFreq, right - left + 1)

        return maxFreq

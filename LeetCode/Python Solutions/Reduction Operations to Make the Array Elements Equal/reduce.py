from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()  # Sort in non-decreasing order
        operations = 0
        distinct_counts = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                distinct_counts += 1
            operations += distinct_counts

        return operations

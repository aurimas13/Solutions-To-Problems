from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Compare the maximum amount robbed considering two subproblems, excluding the first and the last element, respectively
        return max(self.rob_simple(nums, 0, len(nums) - 1), self.rob_simple(nums, 1, len(nums)))

    def rob_simple(self, nums, start, end):
        prevTwo, prevOne, Max = 0, 0, 0

        # Iterate through the given range and update the max robbed amount
        for i in range(start, end):
            Max = max(prevTwo + nums[i], prevOne)
            prevTwo = prevOne
            prevOne = Max

        return Max


# Checking in terminal/console:
if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 3, 2], 3),
        ([2, 7, 9, 3, 1], 11),
        ([0], 0),
        ([], 0),
    ]
    for nums, expected in test_cases:
        result = sol.rob(nums)
        print(f"Input: {nums}, Output: {result}, Expected: {expected}, Result: {result == expected}")

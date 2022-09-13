from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
       return max(self.rob_simple(nums, 0, len(nums) - 1), self.rob_simple(nums, 1, len(nums)))

    def rob_simple(self, nums, start, end):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prevTwo, prevOne, Max = 0, 0, 0

        for i in range(start, end):
            Max = max(prevTwo + nums[i], prevOne)
            prevTwo = prevOne
            prevOne = Max

        return Max


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.rob([1,2,3,1])  # nums = [1,2,3,1] -> 4 | [nums = [2,3,2] -> 3
    print(Solve)

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = [0 for i in range(len(nums))]
        n[0] = nums[0]
        for i in range(1, len(nums)):
            n[i] = max(n[i - 1] + nums[i], nums[i])
        return max(n)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])  # nums = [-2,1,-3,4,-1,2,1,-5,4] -> 6 | [5,4,-1,7,8] -> 23
    print(Solve)

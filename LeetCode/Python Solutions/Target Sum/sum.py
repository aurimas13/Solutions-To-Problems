from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def comb(idx, running_sum):
            if idx + 1 == len(nums):
                if running_sum == target:
                    return 1
                return 0
            if (idx, running_sum) not in dp:
                dp[(idx, running_sum)] = comb(idx + 1, running_sum + nums[idx +1]) + comb(idx + 1, running_sum - nums[idx + 1])
            return dp[(idx, running_sum)]
        return comb(-1, 0)


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findTargetSumWays(nums = [1,1,1,1,1], target = 3) # nums = [1,1,1,1,1], target = 3 -> 5
    print(Solve)

from typing import List


class Solution:
    @staticmethod
    def combinationSum4(nums: List[int], target: int) -> int:
        nums.sort()

        # Notice that we cap the size of our circular dp array by max(nums)+1
        dp = [0 for i in range(min(target, max(nums)) + 1)]
        dp[0] = 1

        # We need to skip comb_sum == 0 since that's a special seed value and
        # we don't want to clear it in the next line
        for comb_sum in range(1, target + 1):
            # We need to clear entries to prevent carry-over of old values
            dp[comb_sum % len(dp)] = 0

            for num in nums:
                if comb_sum - num >= 0:
                    # We use modular arithmetic for indexing since our dp array is circular
                    dp[comb_sum % len(dp)] += dp[(comb_sum - num) % len(dp)]

                else:
                    break

        return dp[target % len(dp)]


# Checking in PyCharm/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.combinationSum4(nums = [1,2,3], target = 4)
    # nums = [1,2,3], target = 4 -> 7 | nums = [9], target = 3 -> 0
    print(Solve)

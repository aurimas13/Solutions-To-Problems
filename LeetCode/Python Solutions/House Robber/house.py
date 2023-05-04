from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max_total = 0
        t1 = t2 = t3 = 0
        for i in range(len(nums)):
            n = nums[i]
            cur_total = max(n + t2, n + t3)
            max_total = max(max_total, cur_total)
            temp1 = t1
            temp2 = t2
            t1 = cur_total
            t2 = temp1
            t3 = temp2

        return max_total


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.rob([1,2,3,1])  # nums = [1,2,3,1] -> 4 | [2,7,9,3,1] -> 12
    print(Solve)

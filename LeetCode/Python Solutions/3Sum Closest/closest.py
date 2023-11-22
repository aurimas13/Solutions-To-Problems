from cmath import inf
from typing import List


class Solution:
    @staticmethod
    def threeSumClosest(nums: List[int], target: int) -> int:
        nums.sort()
        diff = float(inf)
        lens = len(nums)
        ans = None

        for i in range(lens - 2):

            l = i + 1
            r = lens - 1

            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if diff == 0:
                    return target
                if abs(target - temp) < diff:
                    diff = abs(target - temp)
                    ans = temp
                if temp < target:
                    l += 1
                else:
                    r -= 1

        return ans


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.threeSumClosest(nums=[-1, 2, 1, -4], target=1)  # nums = [-1,2,1,-4], target = 1 -> 2
    print(Solve)
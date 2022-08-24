from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 1:
            return True

        i = N - 2
        possible = True
        while i >= 0:
            if nums[i] == 0:
                possible = False
                val = 1
                i -= 1
                while i >= 0:
                    if nums[i] > val:
                        possible = True
                        break
                    val += 1
                    i -= 1
            i -= 1

        return possible


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.canJump([2,3,1,1,4])  # [2,3,1,1,4] -> true
    print(Solve)
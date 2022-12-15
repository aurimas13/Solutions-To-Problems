from typing import List


class Solution:
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.pivotIndex(nums = [1,7,3,6,5,6])
    # nums = [1,7,3,6,5,6] -> 3
    # nums = [1,2,3] -> -1
    print(Solve)

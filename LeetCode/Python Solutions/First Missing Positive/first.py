from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # so far, all the integers that could find their own correct place
        # have been put to the correct place, next thing is to find out the
        # place that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.firstMissingPositive(nums=[7, 8, 9, 11, 12])  # nums = [7,8,9,11,12] -> 1 | nums = [3,4,-1,1] -> 2 | nums = [1,2,0] -> 3
    print(Solve)

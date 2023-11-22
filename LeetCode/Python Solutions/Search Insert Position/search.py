from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        while index <= len(nums):
            if index == len(nums):
                return index
            else:
                if nums[index] < target:
                    index += 1
                else:
                    return index


# Checking in PyCharm/Console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.searchInsert([1,3,5,6], 5)  # [1,3,5,6], 5 -> 2
    print(Solve)
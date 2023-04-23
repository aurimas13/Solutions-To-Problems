from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            middle  = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return nums[left]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findMin([11,13,15,17])  # [11,13,15,17] -> 11| nums = [3,4,5,1,2] -> 1 | nums = [4,5,6,7,0,1,2] -> 0
    print(Solve)


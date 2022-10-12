from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        pivot = len(nums) - k % len(nums)
        nums[:] = nums[pivot:] + nums[:pivot]
        return nums[:]  # Delete this when running in Leetcode 


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.rotate(nums = [-1,-100,3,99], k = 2)  # nums = [-1,-100,3,99], k = 2 -> [3,99,-1,-100] 
    print(Solve)

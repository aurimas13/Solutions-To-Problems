from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        return min(nums[n-1]-nums[0], nums[n-2]-nums[0], nums[n-3]-nums[0], 
        nums[n-4]-nums[0], nums[n-1]-nums[1], nums[n-2]-nums[1], nums[n-3]-nums[1], 
        nums[n-1]-nums[2], nums[n-2]-nums[2], nums[n-1]-nums[3])

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minDifference(nums = [1,5,0,10,14]) 
    # nums = [5,3,2,4] -> 0
    # nums = [1,5,0,10,14] -> 1
    print(Solve)

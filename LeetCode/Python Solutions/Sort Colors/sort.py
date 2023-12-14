from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_lst, white_lst, blue_lst = [], [], []
        for num in nums:
            if num == 0:
                red_lst.append(num)
            elif num == 1:
                white_lst.append(num)
            elif num == 2:
                blue_lst.append(num)
        nums[:] = (red_lst + white_lst + blue_lst)
        return nums # for LeetCode this can be ommited


# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.sortColors(nums = [2,0,2,1,1,0])  # nums = [2,0,2,1,1,0] -> [0,0,1,1,2,2] | nums = [2,0,1] -> [0,1,2]
    print(Solve)

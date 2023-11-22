from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.append(nums.pop(nums.index(i)))


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.moveZeroes([0,1,0,3,12])  #  [0,1,0,3,12] -> [1,3,12,0,0]
    print(Solve)

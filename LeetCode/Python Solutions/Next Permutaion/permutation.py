from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1;
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        while (i < j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.nextPermutation([1, 2, 3])  # [1, 2, 3] = [1, 3, 2], [1, 1, 5] -> [1, 5, 1]
    print(Solve)

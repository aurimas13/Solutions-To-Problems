from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
            j+=1
        return i+1


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeDuplicates([1,1,2])  #  [1,1,2] -> 2
    print(Solve)
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeElement([3,2,2,3], 3)  # [3,2,2,3], 3 -> 2
    print(Solve)

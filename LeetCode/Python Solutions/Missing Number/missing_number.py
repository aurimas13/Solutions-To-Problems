from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.missingNumber([3,0,1])  #  [3,0,1] -> 2 | [9,6,4,2,3,5,7,0,1] -> 8 | [0,1] -> 2
    print(Solve)

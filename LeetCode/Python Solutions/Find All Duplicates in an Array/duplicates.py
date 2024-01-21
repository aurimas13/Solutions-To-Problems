from typing import List


class Solution:
    @staticmethod
    def findDuplicates(nums: List[int]) -> List[int]:
        prev = 0
        dups = []
        for i in sorted(nums):
            if i == prev:
               dups.append(i)
            prev = i
        return dups


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findDuplicates(nums = [4,3,2,7,8,2,3,1])
    # nums = [4,3,2,7,8,2,3,1] -> [2,3]
    # nums = [1,1,2] -> [1]
    print(Solve)

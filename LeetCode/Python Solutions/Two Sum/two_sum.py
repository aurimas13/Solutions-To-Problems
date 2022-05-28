#Solution
from typing import List
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int): #-> List[int]:
        all = list(combinations(nums, 2))
        for i in all:
            if i[0] + i[1] == target:
                return i[0], i[1]
            else:
                pass
# Instantiation
if __name__ == '__main__':
    Solve = Solution.twoSum(12, [2,7,11,15], 9)  # 1234 gives False
    print(Solve)



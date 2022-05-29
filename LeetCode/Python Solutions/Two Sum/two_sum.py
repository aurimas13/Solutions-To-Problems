#Solution
from typing import List
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (i, value_1), (j, value_2) in combinations(enumerate(nums), 2):
            if value_1 + value_2 == target:
                return [i, j]

# Instantiation to check values
if __name__ == '__main__':
    Solve = Solution.twoSum(13, [2,7,11,15], 9)  # [0,1]
    Solve_1 = Solution.twoSum(16, [3,2,3], 6)  # [0,2]
    Solve_2 = Solution.twoSum(23, [3,2,4], 6)  # [1,2]
    print(Solve)
    print(Solve_1)
    print(Solve_2)



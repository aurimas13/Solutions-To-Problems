#Solution
from typing import List
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int): #-> List[int]:
        all = combinations(nums, 2)
        for i, v in enumerate(all):
            print(v[0]+v[1])
            if v[i] + v[i+1] == target:
                return [i, i+1]
            else:
                pass

# Instantiation
if __name__ == '__main__':
    Solve = Solution.twoSum(12, [2,7,11,15], 9)  # 1234 gives False
    Solve_1 = Solution.twoSum(12, [3,2,3], 6)  # 1234 gives False
    Solve_2 = Solution.twoSum(12, [3,2,4], 7)  # 1234 gives False
    print(Solve, Solve_1, Solve_2)



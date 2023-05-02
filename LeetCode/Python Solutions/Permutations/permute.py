from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


# Checking test cases:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.permute([1, 2, 3])  # [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Solve_2 = Instant.permute([0, 1])  # [0,1] -> [[0,1],[1,0]]
    Solve_3 = Instant.permute([1])  # [1] -> [[1]]
    print(Solve)
    print(Solve_2)
    print(Solve_3)

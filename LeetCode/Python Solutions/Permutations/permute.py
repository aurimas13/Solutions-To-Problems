from typing import List
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.permute([1, 2, 3])  # [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(Solve)


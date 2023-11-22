from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal_map[i + j].append(nums[i][j])

        result = []
        for k in sorted(diagonal_map.keys()):
            result.extend(diagonal_map[k][::-1])  # Reverse each diagonal

        return result

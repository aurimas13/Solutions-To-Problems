from functools import reduce
from typing import List


class Solution:
    @staticmethod
    def minCost(costs: List[List[int]]) -> int:
        return min(reduce(lambda a, b: [min(a[j] + b[i] for j in range(len(a)) if i != j) for i in range(len(b))], costs))


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.minCost(costs = [[7,6,2]])
    # costs = [[17,2,17],[16,16,5],[14,3,19]] -> 10
    # costs = [[7,6,2]] -> 2
    print(Solve)


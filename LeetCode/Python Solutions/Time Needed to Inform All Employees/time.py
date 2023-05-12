from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            graph[m].append(i)

        def dfs(node, time):
            max_time = time
            for child in graph[node]:
                max_time = max(max_time, dfs(child, time + informTime[node]))
            return max_time

        return dfs(headID, 0)


# Tests:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0])
    # n = 1, headID = 0, manager = [-1], informTime = [0] -> 0
    # n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] _> 1
    print(Solve)

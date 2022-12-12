from typing import List
from collections import deque


class Solution:
    @staticmethod
    def shortestBridge(grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i, j, land):
           for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
               if 0<=x<n and 0<=y<n and grid[x][y] == 1 and (x,y) not in land:
                   land.add((x,y))
                   dfs(x, y, land)
        # dfs get two island
        land1 = set()
        land2 = set()
        flag = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i,j) not in land1:
                        if not flag:
                            land1.add((i,j))
                            dfs(i, j, land1)
                            flag = 1
                        else:
                            land2.add((i,j))
                            dfs(i, j, land2)
        # bfs get the shortest distance
        Q = deque(list(land1))
        level = 0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                if (i,j) in land2: return level - 1
                for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < n and 0 <= y < n and (x,y) not in land1:
                        land1.add((x,y))
                        Q.append((x,y))
            level += 1


# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]])
    # grid = [[0,1],[1,0]] -> 1
    # grid = [[0,1,0],[0,0,0],[0,0,1]] -> 2
    print(Solve)

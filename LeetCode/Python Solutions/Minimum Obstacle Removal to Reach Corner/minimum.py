from collections import deque
from typing import List

class Solution:
    @staticmethod
    def minimumObstacles(grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 0:
                        if dist[i][j] > dist[x][y]:
                            dist[i][j] = dist[x][y]
                            q.append((i, j))
                    else:
                        if dist[i][j] > dist[x][y] + 1:
                            dist[i][j] = dist[x][y] + 1
                            q.append((i, j))
        return dist[m-1][n-1]

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
    # grid = [[0,1,1],[1,1,0],[1,1,0]] -> 2
    # grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]] -> 0
    print(Solve)

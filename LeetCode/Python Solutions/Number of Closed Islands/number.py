from typing import List
from collections import deque


class Solution:
    @staticmethod
    def closedIsland(grid: List[List[int]]) -> int:
        # Initialize variables
        count = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]

        # Check all cells in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    closed = True
                    q.append((i, j))
                    visited[i][j] = True

                    # BFS to check if the island is closed
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                closed = False
                            elif grid[nx][ny] == 0 and not visited[nx][ny]:
                                q.append((nx, ny))
                                visited[nx][ny] = True

                    # Increase count if the island is closed
                    if closed:
                        count += 1

        return count


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.closedIsland(grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])
    # grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0],
    # [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]] -> 2
    # grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]] -> 1
    print(Solve)

from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        # DFS function to traverse and mark the first island
        def dfs(i, j):
            # Ignore if the current cell is out of bounds or is water or has been visited
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] not in (0, -1)):
                return
            # Mark the current cell as visited
            grid[i][j] = -1
            # Add the current cell to the queue for BFS
            self.queue.append((i, j))
            # Visit all adjacent cells
            list(map(dfs, (i-1, i+1, i, i), (j, j, j-1, j+1)))

        # BFS function to find the shortest bridge to the second island
        def bfs():
            dist = 0
            while self.queue:
                for _ in range(len(self.queue)):
                    i, j = self.queue.popleft()
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            # If we've reached the second island, return the current distance
                            if grid[x][y] == 1:
                                return dist
                            # If the current cell is water, mark it as visited and add it to the queue
                            elif not grid[x][y]:
                                grid[x][y] = -1
                                self.queue.append((x, y))
                # Increase the distance for each level we move away from the first island
                dist += 1

        self.queue = deque()
        break_flag = False
        # Find and mark the first island
        for i in range(len(grid)):
            if break_flag:
                break
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i, j)
                    break_flag = True
                    break
        # Find the shortest bridge to the second island
        return bfs()


# Test case:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]])
    print(Solve)


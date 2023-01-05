from typing import List
from collections import deque


class Solution:
    @staticmethod
    def islandPerimeter(grid: List[List[int]]) -> int:
        search_queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    search_queue.append((i,j))
        perimeter = 0

        while search_queue:
            k, l = search_queue.popleft()
            count = 4
            if (k+1, l) in visited:
                count-=1
            if (k-1, l) in visited:
                count-=1
            if (k, l+1) in visited:
                count-=1
            if (k, l-1) in visited:
                count-=1
            perimeter+=count
        return perimeter


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] -> 16
    # grid = [[1]] -> 4
    # grid = [[1,0]] -> 4
    print(Solve)

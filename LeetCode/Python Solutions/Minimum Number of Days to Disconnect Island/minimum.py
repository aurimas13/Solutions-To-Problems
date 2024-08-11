class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
                return
            visited.add((i, j))
            for di, dj in directions:
                dfs(i + di, j + dj, visited)

        def count_islands():
            visited = set()
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count

        # Check if already disconnected
        if count_islands() != 1:
            return 0

        # Check if removing any single land cell disconnects the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        # Otherwise, it takes 2 days
        return 2
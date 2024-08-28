class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            
            grid2[i][j] = 0  # Mark as visited
            is_sub_island = grid1[i][j] == 1

            for di, dj in directions:
                is_sub_island &= dfs(i + di, j + dj)

            return is_sub_island

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1

        return count
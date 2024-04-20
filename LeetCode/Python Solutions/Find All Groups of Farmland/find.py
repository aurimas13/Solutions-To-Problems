from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = [[False] * n for _ in range(m)]
        results = []
        
        def dfs(r, c, bounds):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or land[r][c] == 0:
                return
            visited[r][c] = True
            # Update bounds with current cell
            bounds[0] = min(bounds[0], r)  # Top row
            bounds[1] = min(bounds[1], c)  # Left column
            bounds[2] = max(bounds[2], r)  # Bottom row
            bounds[3] = max(bounds[3], c)  # Right column
            # Explore all four directions
            dfs(r + 1, c, bounds)
            dfs(r - 1, c, bounds)
            dfs(r, c + 1, bounds)
            dfs(r, c - 1, bounds)

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not visited[i][j]:
                    bounds = [i, j, i, j]  # Initialize bounds as [top, left, bottom, right]
                    dfs(i, j, bounds)
                    results.append(bounds)
        
        return results

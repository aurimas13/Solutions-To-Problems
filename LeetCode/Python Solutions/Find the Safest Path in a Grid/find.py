from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Calculate distance from each cell to the nearest thief using BFS
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    dist[i][j] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        
        # Step 2: Binary search for the maximum safeness factor
        def canReachWithSafeness(safeness: int) -> bool:
            if dist[0][0] < safeness or dist[n-1][n-1] < safeness:
                return False
            
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            while queue:
                x, y = queue.popleft()
                if x == n-1 and y == n-1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= safeness:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        
        low, high = 0, max(max(row) for row in dist)
        while low < high:
            mid = (low + high + 1) // 2
            if canReachWithSafeness(mid):
                low = mid
            else:
                high = mid - 1
        
        return low

import collections
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Initialize starting position and bitmask for all keys
        start = None
        all_keys = 0
        
        # Find the starting position '@' and set the bitmask for all keys
        for i in range(m):
            for j in range(n):
                # If it is the starting position, store it in 'start'
                if grid[i][j] == '@':
                    start = (i, j)
                # If it is a key, add its bit representation to 'all_keys'
                elif grid[i][j] in 'abcdef':
                    all_keys |= 1 << (ord(grid[i][j]) - ord('a'))
        
        # Initialize a queue for BFS with initial position, keys bitmask and steps
        q = collections.deque([(start[0], start[1], 0, 0)])
        # Set to store visited positions with keys bitmask
        visited = set([(start[0], start[1], 0)])
        
        # Perform BFS
        while q:
            # Dequeue the current position, keys bitmask and steps
            x, y, keys, steps = q.popleft()
            
            # If we have collected all keys, return the steps
            if keys == all_keys:
                return steps
            
            # Explore all 4 neighboring cells
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                # Continue if next position is in grid and not a wall
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    # If it is a locked door and we don't have the key, skip
                    if grid[nx][ny] in 'ABCDEF' and not (keys & (1 << (ord(grid[nx][ny]) - ord('A')))):
                        continue
                    
                    # If it is a key, add its bit representation to 'keys'
                    if grid[nx][ny] in 'abcdef':
                        nkeys = keys | (1 << (ord(grid[nx][ny]) - ord('a')))
                    else:
                        nkeys = keys
                    
                    # If this state hasn't been visited, add it to the queue and visited set
                    if (nx, ny, nkeys) not in visited:
                        visited.add((nx, ny, nkeys))
                        q.append((nx, ny, nkeys, steps + 1))
                        
        # If we reach here, it means it is not possible to collect all keys
        return -1

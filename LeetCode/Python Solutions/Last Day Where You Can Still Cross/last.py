from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Define the four cardinal directions: left, right, up, and down
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        # Convert the cell positions from 1-based to 0-based
        for i in range(len(cells)):
            cells[i][0] -= 1
            cells[i][1] -= 1

        # Binary search the maximum day
        lo, hi = 1, len(cells)
        while lo <= hi:
            mi = lo + (hi - lo) // 2  # Calculate the mid day
            
            # Initialize the matrix as all land
            matrix = [[0] * col for _ in range(row)]
            
            # Flood the cells according to the cells list
            for i in range(mi):
                matrix[cells[i][0]][cells[i][1]] = 1

            # Apply BFS to check if it's possible to walk from the top to the bottom on the mid day
            queue = deque([(i, 0) for i in range(col) if matrix[0][i] == 0])
            visited = set(queue)
            while queue:
                x, y = queue.popleft()
                if y == row - 1:  # If we can reach the bottom row
                    lo = mi + 1  # Try to find a larger day
                    break
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < col and 0 <= ny < row and matrix[ny][nx] == 0 and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            else:  # If we cannot reach the bottom row
                hi = mi - 1  # Try to find a smaller day

        return hi  # Return the maximum day when it's still possible to walk from the top to the bottom

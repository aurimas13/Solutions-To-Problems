from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If the starting or ending point is not reachable, return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # Define directions for moving in the grid
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        # Define the size of the grid
        n = len(grid)

        # Initialize the queue with the starting point (0, 0) and the initial path length 1
        queue = deque([((0, 0), 1)])

        # Mark the starting point as visited
        grid[0][0] = 1

        # Perform BFS traversal to find the shortest path
        while queue:
            (x, y), path_length = queue.popleft()

            # Check if the current cell is the bottom-right cell (destination)
            if x == n - 1 and y == n - 1:
                return path_length

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # Check if the new cell is within the grid and unvisited
                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    # Mark the new cell as visited
                    grid[new_x][new_y] = 1
                    # Add the new cell to the queue with updated path length
                    queue.append(((new_x, new_y), path_length + 1))

        return -1

# Test cases
if __name__ == '__main__':
    solution = Solution()
    
    # Test case 1
    grid1 = [[0, 1], [1, 0]]
    assert solution.shortestPathBinaryMatrix(grid1) == 2

    # Test case 2
    grid2 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert solution.shortestPathBinaryMatrix(grid2) == -1

    print("All test cases passed!")

from typing import List
from collections import deque


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # Helper function to get neighbors of a cell
        def get_neighbors(x, y):
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y)]

        # Helper function to convert 2D matrix to 1D tuple
        def mat_to_tuple(mat):
            return tuple(cell for row in mat for cell in row)

        # Initialize variables
        rows, cols = len(mat), len(mat[0])
        start = mat_to_tuple(mat)
        visited = {start}
        queue = deque([(start, 0)])

        # Breadth-First Search
        while queue:
            state, steps = queue.popleft()

            # If the matrix is all zeros, return the number of steps
            if all(cell == 0 for cell in state):
                return steps

            state_mat = [state[i * cols: (i + 1) * cols] for i in range(rows)]

            # Iterate through each cell in the matrix
            for x in range(rows):
                for y in range(cols):
                    # Flip the cell and its neighbors
                    new_state = [list(row) for row in state_mat]
                    for nx, ny in get_neighbors(x, y):
                        if 0 <= nx < rows and 0 <= ny < cols:
                            new_state[nx][ny] ^= 1

                    new_tuple = mat_to_tuple(new_state)

                    # If the new state hasn't been visited, add it to the queue and mark it visited
                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        queue.append((new_tuple, steps + 1))

        # If there's no solution, return -1
        return -1


# Test cases to try in the terminal/console
if __name__ == "__main__":
    solution = Solution()

    test1 = [[0, 0], [0, 1]]
    test2 = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    test3 = [[1, 0, 0], [1, 0, 0]]

    print(solution.minFlips(test1))  # Expected output: 3
    print(solution.minFlips(test2))  # Expected output: 6
    print(solution.minFlips(test3))  # Expected output: -1

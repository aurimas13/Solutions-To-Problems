class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Initialize the starting point and the set of visited points.
        x, y = 0, 0
        visited = {(x, y)}

        # Map the directions to their corresponding coordinate changes.
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for move in path:
            # Update the coordinates based on the direction.
            dx, dy = directions[move]
            x, y = x + dx, y + dy

            # Check if the new position has already been visited.
            if (x, y) in visited:
                return True

            # Mark the new position as visited.
            visited.add((x, y))

        # The path does not cross itself.
        return False

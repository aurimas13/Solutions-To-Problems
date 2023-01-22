from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque()
        visited = set()
        q.append((0, 0, 0))
        visited.add((0, 0))

        # perform BFS
        while q:
            x_curr, y_curr, steps = q.popleft()
            if x_curr == x and y_curr == y:
                return steps
            for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                new_x, new_y = x_curr + dx, y_curr + dy
                if (new_x, new_y) not in visited:
                    q.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minKnightMoves(x = 2, y = 1)
    # x = 2, y = 1 -> 1
    # x = 5, y = 5 -> 4
    print(Solve)
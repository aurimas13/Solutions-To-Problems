from typing import List


class Solution:
    @staticmethod
    def numEnclaves(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        stack = list()
        visited = set()
        for y in [0, m - 1]:
            for x in range(n):
                if grid[y][x] == 1:
                    stack.append((y, x))
                    grid[y][x] = 0
                visited.add((y, x))

        for y in range(1, m - 1):
            for x in [0, n - 1]:
                if grid[y][x] == 1:
                    stack.append((y, x))
                    grid[y][x] = 0
                visited.add((y, x))

        move_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(stack) > 0:
            item = stack.pop()
            y, x = item
            for move_dir in move_dirs:
                cord_y, cord_x = move_dir
                dy = y + cord_y
                dx = x + cord_x
                if 0 < dy < m - 1 and 0 < dx < n - 1 \
                        and grid[dy][dx] == 1 and \
                        (dy, dx) not in visited:
                    stack.append((dy, dx))
                    grid[dy][dx] = 0
                    visited.add((y, x))
        res = 0
        for y in range(m):
            res += sum(grid[y])
        return res


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numEnclaves(
        grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        )
    # grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]] -> 3
    # grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]] -> 0
    print(Solve)

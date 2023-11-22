from typing import List
from collections import deque


class Solution:
    @staticmethod
    def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        row = len(image)
        col = len(image[0])
        image_queue = deque()
        visited = set()

        if oldcolor == color:
            return image

        image_queue.append((sr, sc))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while image_queue:
            (x, y) = image_queue.popleft()
            image[x][y] = color
            for i in directions:
                dx, dy = x + i[0], y + i[1]
                if 0 <= dx < row and 0 <= dy < col and image[dx][dy] == oldcolor and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    image_queue.append((dx, dy))
        return image


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
    # image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2 -> [[2,2,2],[2,2,0],[2,0,1]]
    print(Solve)

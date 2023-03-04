from typing import List


class Solution:
    @staticmethod
    def generateMatrix(n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for i in range(n)]
        values = [i for i in range(n ** 2, 0, -1)]
        turn_left = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        c = (n // 2, n // 2 - 1) if n % 2 == 0 else (n // 2, n // 2)

        x, y = c
        orient = (1, 0) if n % 2 == 0 else (-1, 0)
        for i in range(n ** 2):
            val = values[i]
            matrix[x][y] = val

            turn_dx, turn_dy = turn_left.get(orient)

            if x + turn_dx in range(0, n) and y + turn_dy in range(0, n) and matrix[x + turn_dx][y + turn_dy] is None:
                orient = (turn_dx, turn_dy)

            x, y = x + orient[0], y + orient[1]  # continue path
        return matrix


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.generateMatrix(n=3)
    # n=3 -> [[1,2,3],[8,9,4],[7,6,5]] | n=1 -> [[1]]
    print(Solve)

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findMaxLength(x, y):
            if x >= len(matrix) or y >= len(matrix[0]):
                return 0

            if pathMap[x][y] != 0:
                return pathMap[x][y]

            length = 0
            curr = matrix[x][y]
            maxPath = []

            if x - 1 >= 0 and matrix[x - 1][y] > curr:
                maxPath.append(1 + findMaxLength(x - 1, y))
            if x + 1 < len(matrix) and matrix[x + 1][y] > curr:
                maxPath.append(1 + findMaxLength(x + 1, y))
            if y - 1 >= 0 and matrix[x][y - 1] > curr:
                maxPath.append(1 + findMaxLength(x, y - 1))
            if y + 1 < len(matrix[0]) and matrix[x][y + 1] > curr:
                maxPath.append(1 + findMaxLength(x, y + 1))

            if len(maxPath) == 0:
                pathMap[x][y] = 1
                return 1
            else:
                pathMap[x][y] = max(maxPath)
                return max(maxPath)

        maxLength = 0
        pathMap = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(0, len(matrix) + 1):  # +1 for 1-D array
            for j in range(0, len(matrix[0]) + 1):  # +1 for 1-D array
                maxLength = max(maxLength, findMaxLength(i, j))

        return maxLength


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])  # matrix = [[9,9,4],[6,6,8],[2,1,1]] -> 4 |  matrix = [[3,4,5],[3,2,6],[2,2,1]] -> 4
    print(Solve)

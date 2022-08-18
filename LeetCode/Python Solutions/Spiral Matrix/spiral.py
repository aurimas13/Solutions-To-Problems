from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = 0
        currDir = 0
        result = []
        visited = {}

        while len(result) < rows * columns:
            while 0 <= r < rows and 0 <= c < columns and (r, c) not in visited:
                result.append(matrix[r][c])
                visited[(r, c)] = True
                r += dirs[currDir][0]
                c += dirs[currDir][1]

            # reset
            r -= dirs[currDir][0]
            c -= dirs[currDir][1]
            # change direction.
            currDir = (currDir + 1) % 4
            # set new r, c in the next loop.
            r += dirs[currDir][0]
            c += dirs[currDir][1]

        return result


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])  # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] -> [1,2,3,4,8,12,11,10,9,5,6,7] | [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
    print(Solve)
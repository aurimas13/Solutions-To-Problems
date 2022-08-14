from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        scol = set()
        for j in range(rows):
            ret = False
            for i in range(cols):
                if matrix[j][i] == 0:
                    scol.add(i)
                    ret = True
            if ret:
                matrix[j] = [0] * cols

        for i in scol:
            for j in range(rows):
                matrix[j][i] = 0


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]) # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]-> None
    print(Solve)

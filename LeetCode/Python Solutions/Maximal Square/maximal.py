from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)  # no. of rows in matrix[][]
        column = len(matrix[0])  # no. of columns in matrix[][]
        matrix_int = []

        # Converting a list of strings to a list of integers
        for i in range(row):
            full_row = list(map(int, matrix[i]))
            matrix_int.append(full_row)

        S = []
        # Here we have set the first row and first column of S same as input matrix, other entries are set to 0
        for i in range(row):
            temp = []
            for j in range(column):
                if i == 0 or j == 0:
                    temp += matrix_int[i][j],
                else:
                    temp += 0,
            S += temp,

        # Update other entries
        for i in range(1, row):
            for j in range(1, column):
                if matrix_int[i][j] == 1:
                    S[i][j] = min(S[i][j - 1], S[i - 1][j],
                                  S[i - 1][j - 1]) + 1
                else:
                    S[i][j] = 0

        # Find the maximum entry and
        # indices of maximum entry in S[][]
        max_of_S = S[0][0]
        max_i = 0
        max_j = 0
        for i in range(row):
            for j in range(column):
                if max_of_S < S[i][j]:
                    max_of_S = S[i][j]
                    max_i = i
                    max_j = j

        result = 0
        for i in range(max_i, max_i - max_of_S, -1):
            for j in range(max_j, max_j - max_of_S, -1):
                matrix_int[i][j]
                result+=1
        return result



# Tests:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])  
    # [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] -> 4  
    # matrix = [["0"]] -> 0 
    # matrix = [["0","1"],["1","0"]] -> 1
    print(Solve)
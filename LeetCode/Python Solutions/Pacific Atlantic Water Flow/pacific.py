from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        row = len(matrix)
        col = len(matrix[0])
        pacific = [["0" for _ in range(col)] for _ in range(row)]
        atlantic = [["0" for _ in range(col)] for _ in range(row)]

        def function(r, c, sea, val, M):
            if 0 <= r < row and 0 <= c < col and M[r][c] == "0":
                if matrix[r][c] >= val:
                    # print(r,c)
                    M[r][c] = sea
                    function(r - 1, c, sea, matrix[r][c], M)
                    function(r + 1, c, sea, matrix[r][c], M)
                    function(r, c - 1, sea, matrix[r][c], M)
                    function(r, c + 1, sea, matrix[r][c], M)

        for i in range(col):
            function(0, i, "P", -1, pacific)
        for i in range(row):
            function(i, 0, "P", -1, pacific)
        for i in range(col - 1, -1, -1):
            function(row - 1, i, "A", -1, atlantic)
        for i in range(row - 1, -1, -1):
            function(i, col - 1, "A", -1, atlantic)
        answer = []

        for i in range(row):
            for j in range(col):
                if atlantic[i][j] == "A" and pacific[i][j] == "P":
                    answer.append([i, j])

        return answer

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.pacificAtlantic(matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) # matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    print(Solve)

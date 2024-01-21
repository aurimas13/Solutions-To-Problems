class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowCount = [sum(row) for row in mat]
        colCount = [sum(col) for col in zip(*mat)]
        
        specialCount = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    specialCount += 1
        return specialCount

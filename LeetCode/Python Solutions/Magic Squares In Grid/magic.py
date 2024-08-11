class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(i, j):
            # Check if all numbers are from 1 to 9
            s = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if grid[x][y] < 1 or grid[x][y] > 9 or grid[x][y] in s:
                        return False
                    s.add(grid[x][y])
            
            # Check rows, columns, and diagonals
            target = sum(grid[i][j:j+3])
            return all(sum(grid[i+x][j:j+3]) == target for x in range(3)) and \
                   all(sum(grid[i+x][j+y] for x in range(3)) == target for y in range(3)) and \
                   sum(grid[i+x][j+x] for x in range(3)) == target and \
                   sum(grid[i+x][j+2-x] for x in range(3)) == target

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, self.explore(grid, i, j))
        return max_gold
    
    def explore(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        gold = grid[i][j]
        grid[i][j] = 0  # mark as visited
        max_gold = 0
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            max_gold = max(max_gold, self.explore(grid, i+x, j+y))
        grid[i][j] = gold  # backtrack
        return max_gold + gold



# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])  
    # grid = [[0,6,0],[5,8,7],[0,9,0]] -> 24
    # grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]] -> 28
    print(Solve)

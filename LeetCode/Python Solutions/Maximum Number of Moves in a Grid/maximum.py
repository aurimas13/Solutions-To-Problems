class Solution:
   def maxMoves(self, grid: List[List[int]]) -> int:
       m, n = len(grid), len(grid[0])
       
       # Initialize dp array to keep track of reachable cells
       dp = [[False] * n for _ in range(m)]
       
       # First column cells are reachable
       for i in range(m):
           dp[i][0] = True
           
       max_moves = 0
       
       # Process column by column
       for j in range(n-1):
           has_move = False
           
           for i in range(m):
               # If current cell is reachable
               if dp[i][j]:
                   # Try all three possible moves
                   for ni in [i-1, i, i+1]:
                       if 0 <= ni < m and grid[ni][j+1] > grid[i][j]:
                           if not dp[ni][j+1]:  # If not already marked reachable
                               dp[ni][j+1] = True
                               has_move = True
                               max_moves = max(max_moves, j+1)
           
           # If no moves possible from this column, break
           if not has_move:
               break
               
       return max_moves
class Solution:
   def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
       m, n = len(box), len(box[0])
       
       # Move stones in each row first
       for i in range(m):
           # Process each row from right to left
           empty = n - 1
           for j in range(n - 1, -1, -1):
               if box[i][j] == '#':
                   box[i][j] = '.'
                   box[i][empty] = '#'
                   empty -= 1
               elif box[i][j] == '*':
                   empty = j - 1
       
       # Rotate the box 90 degrees clockwise
       rotated = [['.'] * m for _ in range(n)]
       for i in range(m):
           for j in range(n):
               rotated[j][m - 1 - i] = box[i][j]
       
       return rotated
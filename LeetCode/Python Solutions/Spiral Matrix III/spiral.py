class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
        result = [[rStart, cStart]]
        if rows * cols == 1:
            return result
        
        steps = 0
        d = 0  # Start facing East
        
        while len(result) < rows * cols:
            if d % 2 == 0:
                steps += 1
            
            for _ in range(steps):
                rStart += directions[d][0]
                cStart += directions[d][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                if len(result) == rows * cols:
                    return result
            
            d = (d + 1) % 4  # Change direction
        
        return result
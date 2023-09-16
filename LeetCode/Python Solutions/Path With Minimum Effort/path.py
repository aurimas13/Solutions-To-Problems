class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def canReachDestination(maxEffort):
            visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
            stack = [(0, 0)]
            visited[0][0] = True
            while stack:
                i, j = stack.pop()
                if i == len(heights) - 1 and j == len(heights[0]) - 1:
                    return True
                for x, y in dirs:
                    ni, nj = i + x, j + y
                    if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and not visited[ni][nj]:
                        if abs(heights[i][j] - heights[ni][nj]) <= maxEffort:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
            return False
        
        left, right = 0, 1000000
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1
        return left

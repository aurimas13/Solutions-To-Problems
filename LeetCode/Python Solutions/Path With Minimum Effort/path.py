class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Define movement directions.
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Check if we can reach the destination with a given effort.
        def canReachDestination(maxEffort):
            # Initialize visited cells.
            visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
            
            # Start DFS using a stack from the top-left corner.
            stack = [(0, 0)]
            visited[0][0] = True
            
            # While there are cells to explore:
            while stack:
                i, j = stack.pop()
                
                # If we're at the destination, return True.
                if i == len(heights) - 1 and j == len(heights[0]) - 1:
                    return True

                # Explore all possible directions.
                for x, y in dirs:
                    ni, nj = i + x, j + y
                    
                    # If the new cell is valid, mark it as visited and add to the stack.
                    if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and not visited[ni][nj]:
                        if abs(heights[i][j] - heights[ni][nj]) <= maxEffort:
                            visited[ni][nj] = True
                            stack.append((ni, nj))

            # Return False if we cannot reach the destination.
            return False

        # Initialize binary search range.
        left, right = 0, 1000000
        
        # Binary search logic.
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1

        # Return the minimum effort.
        return left

from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        # Number of boys and girls
        m, n = len(grid), len(grid[0])
        
        # Function to find augmenting paths using DFS
        def dfs(u, seen, match):
            for v in range(n):
                if grid[u][v] and v not in seen:
                    seen.add(v)
                    if match[v] is None or dfs(match[v], seen, match):
                        match[v] = u
                        return True
            return False
        
        # Maximum bipartite matching using augmenting paths
        match = [None] * n
        count = 0
        for u in range(m):
            seen = set()
            if dfs(u, seen, match):
                count += 1
                
        return count


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxNumberOfBalloons('balon')  
    # grid = [[1,1,1], [1,0,1], [0,0,1]] -> 3
    # grid = [[1,0,1,0], [1,0,0,0],
    #         [0,0,1,0], [1,1,1,0]] -> 3
    print(Solve)
from typing import List
from collections import deque


class Solution:
    @staticmethod
    def findCircleNum(isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Create a visited list to keep track of which cities have been visited
        visited = [0] * n
        # Initialize the number of provinces to 0
        num_provinces = 0

        for i in range(n):
            # If the city has not been visited yet
            if visited[i] == 0:
                # Use BFS to traverse all the cities that are directly or indirectly connected to it
                queue = deque([i])
                visited[i] = 1
                while queue:
                    city = queue.popleft()
                    for j in range(n):
                        if isConnected[city][j] == 1 and visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
                # Increase the number of provinces by 1
                num_provinces += 1
        return num_provinces


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
    # isConnected = [[1,1,0],[1,1,0],[0,0,1]] -> 2
    # isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] -> 3
    print(Solve)



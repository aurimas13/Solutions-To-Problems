from collections import deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        # Create a set to store the visited vertices
        visited = set()

        # Create a queue and add the source vertex to it
        queue = [source]
        while queue:
            # Pop the first vertex from the queue
            vertex = queue.pop(0)

            # If the popped vertex is the destination vertex, return true
            if vertex == destination:
                return True

            # Mark the vertex as visited
            visited.add(vertex)

            # Add all the neighbors of the popped vertex to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        # Return false if the destination vertex was not reached
        return False


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)
    # n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2 -> true
    # n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 -> false
    print(Solve)

from collections import deque, defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to check path
        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return False

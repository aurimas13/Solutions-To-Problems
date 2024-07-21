from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(edges: List[List[int]], k: int) -> List[int]:
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            for u, v in edges:
                graph[u].append(v)
                in_degree[v] += 1
                
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            topo_order = []
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix

# Example usage:
sol = Solution()
print(sol.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))  # Example 1
print(sol.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]))  # Example 2

from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        # Add an index to each edge so we can reference them later
        m = len(edges)
        for i in range(m):
            edges[i].append(i)
        
        # Sort edges by their weights
        edges.sort(key=lambda x: x[2])

        # Union-find's find operation with path compression
        def find(uf, x):
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        # The Kruskal's algorithm to compute the MST's weight
        def kruskal(n, edges, banned, forced):
            uf = list(range(n))
            total_weight = 0
            if forced != -1:
                u, v, w, _ = edges[forced]
                if find(uf, u) != find(uf, v):
                    union(uf, u, v)
                    total_weight += w
                    n -= 1
            
            for i, (u, v, w, _) in enumerate(edges):
                if i == banned or i == forced:
                    continue
                if find(uf, u) != find(uf, v):
                    union(uf, u, v)
                    total_weight += w
                    n -= 1
            return total_weight if n == 1 else float('inf')

        # Union-find's union operation
        def union(uf, x, y):
            uf[find(uf, x)] = find(uf, y)

        # Compute the weight of the original MST
        original_mst = kruskal(n, edges, -1, -1)

        critical, pseudo = [], []

        # Check for critical edges
        for i in range(m):
            if kruskal(n, edges, i, -1) > original_mst:
                critical.append(edges[i][3])

        # Check for pseudo-critical edges
        for i in range(m):
            if edges[i][3] not in critical and kruskal(n, edges, -1, i) == original_mst:
                pseudo.append(edges[i][3])

        return [critical, pseudo]

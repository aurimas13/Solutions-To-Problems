from typing import List, Tuple

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort the edge list by weight in ascending order
        edgeList.sort(key=lambda x: x[2])

        # Initialize a list to store the parents of each node
        parents = list(range(n))

        # Initialize a list to store the rank of each node
        rank = [0] * n

        # Define a helper function to find the parent of a node
        def find(node: int) -> int:
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        # Define a helper function to perform union of two nodes
        def union(a: int, b: int) -> None:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                if rank[root_a] < rank[root_b]:
                    parents[root_a] = root_b
                elif rank[root_a] > rank[root_b]:
                    parents[root_b] = root_a
                else:
                    parents[root_b] = root_a
                    rank[root_a] += 1

        # Initialize the result list for queries
        result = [False] * len(queries)

        # Pair each query with its index, and sort the queries by their limit
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])

        # Initialize edge index for iterating through the edge list
        edge_idx = 0

        # Iterate through the sorted queries
        for query_idx, (p, q, limit) in queries:
            # Keep adding edges to the path while the edge weight is less than the query limit
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                a, b, _ = edgeList[edge_idx]
                edge_idx += 1
                # Union the two sets containing nodes a and b
                union(a, b)

            # Check if the nodes p and q belong to the same set, and update the result list
            result[query_idx] = find(p) == find(q)

        # Return the result list containing the answers for all queries
        return result

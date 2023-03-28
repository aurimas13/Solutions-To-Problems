# Import typing to use List and Tuple types
from typing import List, Tuple

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort the edge list by weight in ascending order
        edgeList.sort(key=lambda x: x[2])

        # Initialize a list to store the parents of each node
        parents = list(range(n))

        # Define a helper function to find the parent of a node
        def find(node: int) -> int:
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

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
                parents[find(a)] = find(b)

            # Check if the nodes p and q belong to the same set, and update the result list
            result[query_idx] = find(p)
            # Check if the nodes p and q belong to the same set, and update the result list
            result[query_idx] = find(p) == find(q)

        # Return the result list containing the answers for all queries
        return result


# Test the solution in the terminal
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Test case 1
    n1 = 3
    edgeList1 = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    queries1 = [[0, 1, 2], [0, 2, 5]]
    assert solution.distanceLimitedPathsExist(n1, edgeList1, queries1) == [False, True]

# Test case 2
    n2 = 5
    edgeList2 = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries2 = [[0, 4, 14], [1, 3, 8], [0, 3, 7]]
    assert solution.distanceLimitedPathsExist(n2, edgeList2, queries2) == [True, False, False]

    # Test case 3
    n3 = 6
    edgeList3 = [[0, 1, 3], [1, 2, 4], [2, 3, 6], [3, 4, 7], [4, 5, 9], [0, 5, 12]]
    queries3 = [[0, 3, 6], [0, 5, 10], [1, 4, 7], [2, 5, 10]]
    assert solution.distanceLimitedPathsExist(n3, edgeList3, queries3) == [True, True, False, True]

    print("All tests passed!")
    
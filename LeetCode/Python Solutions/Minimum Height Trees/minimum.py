from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            # Remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        new_leaves.append(neighbor)

            # Prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
    
if __name__ == '__main__':
    sol = Solution()

    n1 = 4
    edges1 = [[1, 0], [1, 2], [1, 3]]
    assert sol.findMinHeightTrees(n1, edges1) == [1]

    n2 = 6
    edges2 = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    assert set(sol.findMinHeightTrees(n2, edges2)) == set([3, 4])  # convert to sets before comparison

    print("All tests passed.")

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Initialize the color of all nodes to be white (0)
        color = [0] * len(graph)

        # A helper function to do the DFS search
        def dfs(node):
            # If we have visited this node before, return whether it is safe
            if color[node] > 0:
                return color[node] == 1

            # Mark the node as currently visiting
            color[node] = 2
            # For each neighbour of the node
            for nei in graph[node]:
                # If any neighbour is unsafe or currently visiting, then the node is unsafe
                if not dfs(nei):
                    return False

            # If all neighbours are safe, then the node is safe
            color[node] = 1
            return True

        # For each node in the graph, do a DFS
        return [i for i in range(len(graph)) if dfs(i)]

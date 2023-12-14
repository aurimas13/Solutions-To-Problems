from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

     # Initializing the result list to store all paths
        result = []

        # Helper function to perform Depth First Search (DFS) on the graph
        def dfs(path: List[int]) -> None:
            # When the last node in the path is the target node, add the path to the result list
            if path[-1] == len(graph) - 1:
                result.append(path)
                return

            # If not the target node, explore the adjacent nodes recursively using DFS
            for neighbor in graph[path[-1]]:
                dfs(path + [neighbor])

        # Start DFS from the source node (0)
        dfs([0])

        return result


# Test the solution using if __name__ == '__main__' clause
if __name__ == '__main__':
    sol = Solution()

    graph1 = [[1, 2], [3], [3], []]
    assert sol.allPathsSourceTarget(graph1) == [[0, 1, 3], [0, 2, 3]]

    graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    assert sol.allPathsSourceTarget(graph2) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

    graph3 = [[1], []]
    assert sol.allPathsSourceTarget(graph3) == [[0, 1]]

    print("All tests passed.")

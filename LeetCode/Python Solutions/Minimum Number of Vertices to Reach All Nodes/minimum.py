from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set of all destination vertices
        destinations = {to_vertex for _, to_vertex in edges}
        
        # Return the set of vertices that are not destinations
        return [vertex for vertex in range(n) if vertex not in destinations]


# Tests:
if __name__ == "__main__":
    solution = Solution()   
    n, m = 6, 5
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    edges_1 = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    print(solution.findSmallestSetOfVertices(n, edges))
    # Output: [0, 3]
    print(solution.findSmallestSetOfVertices(m, edges_1))
    # Output: [0, 2, 3]

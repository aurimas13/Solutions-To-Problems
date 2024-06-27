from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Since it's a star graph, the center node must appear in the first two edges
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]

# Example usage:
sol = Solution()
print(sol.findCenter([[1, 2], [2, 3], [4, 2]]))  # Output: 2
print(sol.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))  # Output: 1

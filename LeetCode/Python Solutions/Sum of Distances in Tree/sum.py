from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create adjacency list for the tree
        tree = defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        # Initialize variables to store counts and sums
        count = [1] * n
        ans = [0] * n

        # Helper function for post-order traversal
        def post_order(node: int, parent: int):
            for child in tree[node]:
                if child != parent:
                    post_order(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        # Helper function for pre-order traversal
        def pre_order(node: int, parent: int):
            for child in tree[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    pre_order(child, node)

        # Perform post-order and pre-order traversals
        post_order(0, -1)
        pre_order(0, -1)

        return ans


# Test cases to try in the terminal/console
if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))  # Output: [8, 12, 6, 10, 10, 10]

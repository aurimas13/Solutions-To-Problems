from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        self.components -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Sort edges to process type-3 edges first
        edges.sort(key=lambda x: -x[0])

        # Initialize UnionFind for Alice and Bob
        uf_alice, uf_bob = UnionFind(n), UnionFind(n)

        # Count the number of edges removed
        removed_edges = 0

        for edge in edges:
            edge_type, u, v = edge
            u, v = u - 1, v - 1

            # If edge is type-3, try to add it to both Alice's and Bob's UnionFind
            if edge_type == 3:
                added_alice = uf_alice.union(u, v)
                added_bob = uf_bob.union(u, v)
                if not (added_alice or added_bob):
                    removed_edges += 1
            # If edge is type-1, try to add it to Alice's UnionFind
            elif edge_type == 1:
                if not uf_alice.union(u, v):
                    removed_edges += 1
            # If edge is type-2, try to add it to Bob's UnionFind
            else:
                if not uf_bob.union(u, v):
                    removed_edges += 1

        # Check if both Alice's and Bob's graphs are fully connected
        if uf_alice.components == 1 and uf_bob.components == 1:
            return removed_edges
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    result = solution.maxNumEdgesToRemove(n, edges)
    print("Result:", result)  # Expected output: 2


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize the parent list with each node as its own parent
        self.rank = [0] * size  # Initialize the rank list with all nodes having rank 0

    def find(self, x):
        if self.parent[x] != x:  # If the parent of the node is not itself
            self.parent[x] = self.find(self.parent[x])  # Recursively find the representative of the set
        return self.parent[x]  # Return the representative

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)  # Find the representatives of the two nodes

        if root_x == root_y:  # If both nodes have the same representative, they are in the same set
            return False

        # Merge the two sets based on rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)  # Initialize the UnionFind data structure

        # Iterate through each edge and try to perform a union operation
        return next(edge for edge in edges if not uf.union(edge[0], edge[1]))

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y + 10001)  # Offset y to avoid collision with x
        
        components = set(uf.find(x) for x, y in stones) | set(uf.find(y + 10001) for x, y in stones)
        return len(stones) - len(components)
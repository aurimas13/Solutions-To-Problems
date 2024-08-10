class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)
        
        def get_index(row, col, pos):
            return 4 * (row * n + col) + pos
        
        for i in range(n):
            for j in range(n):
                if i > 0:
                    uf.union(get_index(i-1, j, 2), get_index(i, j, 0))
                if j > 0:
                    uf.union(get_index(i, j-1, 1), get_index(i, j, 3))
                
                if grid[i][j] != '/':
                    uf.union(get_index(i, j, 0), get_index(i, j, 1))
                    uf.union(get_index(i, j, 2), get_index(i, j, 3))
                if grid[i][j] != '\\':
                    uf.union(get_index(i, j, 0), get_index(i, j, 3))
                    uf.union(get_index(i, j, 1), get_index(i, j, 2))
        
        return uf.count
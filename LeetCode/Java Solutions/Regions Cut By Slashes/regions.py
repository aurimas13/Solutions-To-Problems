class Solution {
    class UnionFind {
        int[] parent;
        int count;
        
        UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            count = n;
        }
        
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
                count--;
            }
        }
    }
    
    public int regionsBySlashes(String[] grid) {
        int n = grid.length;
        UnionFind uf = new UnionFind(4 * n * n);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) uf.union(getIndex(n, i-1, j, 2), getIndex(n, i, j, 0));
                if (j > 0) uf.union(getIndex(n, i, j-1, 1), getIndex(n, i, j, 3));
                
                if (grid[i].charAt(j) != '/') {
                    uf.union(getIndex(n, i, j, 0), getIndex(n, i, j, 1));
                    uf.union(getIndex(n, i, j, 2), getIndex(n, i, j, 3));
                }
                if (grid[i].charAt(j) != '\\') {
                    uf.union(getIndex(n, i, j, 0), getIndex(n, i, j, 3));
                    uf.union(getIndex(n, i, j, 1), getIndex(n, i, j, 2));
                }
            }
        }
        
        return uf.count;
    }
    
    private int getIndex(int n, int row, int col, int pos) {
        return 4 * (row * n + col) + pos;
    }
}
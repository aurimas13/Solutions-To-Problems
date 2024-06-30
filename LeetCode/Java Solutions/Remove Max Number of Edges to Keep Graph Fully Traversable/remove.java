import java.util.*;

class DSU {
    int[] parent;
    int[] rank;
    
    public DSU(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }
    
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    public boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
        return false;
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        DSU dsuA = new DSU(n + 1);
        DSU dsuB = new DSU(n + 1);
        Arrays.sort(edges, (a, b) -> b[0] - a[0]);  // Sort edges by type in descending order

        int usedEdges = 0;

        for (int[] edge : edges) {
            int type = edge[0];
            int u = edge[1];
            int v = edge[2];
            if (type == 3) {
                if (dsuA.union(u, v) | dsuB.union(u, v)) {
                    usedEdges++;
                }
            } else if (type == 1) {
                if (dsuA.union(u, v)) {
                    usedEdges++;
                }
            } else if (type == 2) {
                if (dsuB.union(u, v)) {
                    usedEdges++;
                }
            }
        }

        // Check if both graphs are fully traversable
        int rootA = dsuA.find(1);
        int rootB = dsuB.find(1);
        for (int i = 2; i <= n; i++) {
            if (dsuA.find(i) != rootA || dsuB.find(i) != rootB) {
                return -1;
            }
        }

        return edges.length - usedEdges;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxNumEdgesToRemove(4, new int[][]{{3,1,2},{3,2,3},{1,1,3},{1,2,4},{1,1,2},{2,3,4}}));  // Output: 2
        System.out.println(sol.maxNumEdgesToRemove(4, new int[][]{{3,1,2},{3,2,3},{1,1,4},{2,1,4}}));  // Output: 0
        System.out.println(sol.maxNumEdgesToRemove(4, new int[][]{{3,2,3},{1,1,2},{2,3,4}}));  // Output: -1
    }
}

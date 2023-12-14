import java.util.*;

class Solution {
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        int m = edges.length;
        int[][] newEdges = new int[m][4];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 3; j++) {
                newEdges[i][j] = edges[i][j];
            }
            newEdges[i][3] = i;
        }
        
        Arrays.sort(newEdges, (a, b) -> Integer.compare(a[2], b[2]));
        
        int originalMST = kruskal(n, newEdges, -1, -1);
        List<Integer> critical = new ArrayList<>();
        List<Integer> pseudo = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            if (kruskal(n, newEdges, i, -1) > originalMST) {
                critical.add(newEdges[i][3]);
            }
        }

        for (int i = 0; i < m; i++) {
            if (!critical.contains(newEdges[i][3]) && kruskal(n, newEdges, -1, i) == originalMST) {
                pseudo.add(newEdges[i][3]);
            }
        }

        return Arrays.asList(critical, pseudo);
    }
    
    private int find(int[] uf, int x) {
        if (uf[x] != x) uf[x] = find(uf, uf[x]);
        return uf[x];
    }

    private void union(int[] uf, int x, int y) {
        uf[find(uf, x)] = find(uf, y);
    }

    private int kruskal(int n, int[][] edges, int banned, int forced) {
        int[] uf = new int[n];
        for (int i = 0; i < n; i++) uf[i] = i;
            
        int totalWeight = 0;
        if (forced != -1) {
            int u = edges[forced][0], v = edges[forced][1], w = edges[forced][2];
            if (find(uf, u) != find(uf, v)) {
                union(uf, u, v);
                totalWeight += w;
                n--;
            }
        }
            
        for (int i = 0; i < edges.length; i++) {
            if (i == banned || i == forced) continue;
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            if (find(uf, u) != find(uf, v)) {
                union(uf, u, v);
                totalWeight += w;
                n--;
            }
        }
            
        return n == 1 ? totalWeight : Integer.MAX_VALUE;
    }
}


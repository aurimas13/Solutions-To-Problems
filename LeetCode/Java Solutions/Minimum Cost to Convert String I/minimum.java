import java.util.*;

class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        int n = 26;
        int INF = 1000000000;

        // Initialize the cost graph with infinity
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        // Fill in the initial costs based on the given transformations
        for (int i = 0; i < original.length; i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            dist[u][v] = Math.min(dist[u][v], cost[i]);
        }

        // Floyd-Warshall algorithm to compute shortest paths
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] < INF && dist[k][j] < INF) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        // Calculate the minimum cost to convert source to target
        long totalCost = 0;
        for (int i = 0; i < source.length(); i++) {
            int s = source.charAt(i) - 'a';
            int t = target.charAt(i) - 'a';
            if (s == t) {
                continue;
            }
            if (dist[s][t] == INF) {
                return -1;
            }
            totalCost += dist[s][t];
        }

        return totalCost;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minimumCost("abcd", "acbe", new char[]{'a','b','c','c','e','d'}, new char[]{'b','c','b','e','b','e'}, new int[]{2,5,5,1,2,20}));  // Output: 28
        System.out.println(sol.minimumCost("aaaa", "bbbb", new char[]{'a','c'}, new char[]{'c','b'}, new int[]{1,2}));  // Output: 12
        System.out.println(sol.minimumCost("abcd", "abce", new char[]{'a'}, new char[]{'e'}, new int[]{10000}));  // Output: -1
    }
}

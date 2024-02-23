import java.util.Arrays;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // Initialize distances array with infinity, except the source city
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        
        // Temporary array to store new distances in each iteration
        int[] newDist;
        
        // Bellman-Ford: Relax edges up to k+1 times
        for (int i = 0; i <= k; i++) {
            newDist = dist.clone();
            for (int[] flight : flights) {
                int u = flight[0], v = flight[1], cost = flight[2];
                if (dist[u] != Integer.MAX_VALUE && dist[u] + cost < newDist[v]) {
                    newDist[v] = dist[u] + cost;
                }
            }
            dist = newDist;
        }
        
        // Check if the destination is reachable
        return dist[dst] == Integer.MAX_VALUE ? -1 : dist[dst];
    }
}

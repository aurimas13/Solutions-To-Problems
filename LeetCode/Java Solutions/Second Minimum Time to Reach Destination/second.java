import java.util.*;

class Solution {
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        // Build the adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        // Initialize distances array and priority queue
        int[][] dist = new int[n + 1][2];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{1, 0});
        dist[1][0] = 0;
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0], currTime = curr[1];
            
            // If we've found the second minimum time to reach node n, return it
            if (node == n && dist[n][1] != Integer.MAX_VALUE) {
                return dist[n][1];
            }
            
            // Calculate the actual time considering traffic signal changes
            int actualTime = currTime;
            if ((actualTime / change) % 2 == 1) {
                actualTime = (actualTime / change + 1) * change;
            }
            actualTime += time;
            
            for (int neighbor : graph.get(node)) {
                if (actualTime < dist[neighbor][0]) {
                    dist[neighbor][1] = dist[neighbor][0];
                    dist[neighbor][0] = actualTime;
                    pq.offer(new int[]{neighbor, actualTime});
                } else if (actualTime > dist[neighbor][0] && actualTime < dist[neighbor][1]) {
                    dist[neighbor][1] = actualTime;
                    pq.offer(new int[]{neighbor, actualTime});
                }
            }
        }
        
        return -1; // Should never reach here given the problem constraints
    }
}
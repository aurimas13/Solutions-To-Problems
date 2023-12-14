import java.util.*;

class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        // Create adjacency list
        Map<Integer, List<Pair<Integer, Double>>> adjList = new HashMap<>();
        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            adjList.putIfAbsent(edge[0], new ArrayList<>());
            adjList.putIfAbsent(edge[1], new ArrayList<>());
            adjList.get(edge[0]).add(new Pair<>(edge[1], succProb[i]));
            adjList.get(edge[1]).add(new Pair<>(edge[0], succProb[i]));
        }
        
        // Initialize distance and visited arrays
        double[] distance = new double[n];
        boolean[] visited = new boolean[n];
        
        // Initialize priority queue
        PriorityQueue<Pair<Double, Integer>> pq = new PriorityQueue<>(Comparator.comparingDouble(Pair::getKey));
        pq.offer(new Pair<>(-1.0, start));
        
        // Iterate until priority queue is empty
        while (!pq.isEmpty()) {
            // Pop the node with the highest probability
            Pair<Double, Integer> pair = pq.poll();
            double prob = pair.getKey();
            int node = pair.getValue();
            
            // If the node is already visited, continue
            if (visited[node]) {
                continue;
            }
            
            // Mark the node as visited
            visited[node] = true;
            
            // Update distance
            distance[node] = -prob;
            
            // Iterate through the neighbors of the node
            List<Pair<Integer, Double>> neighbors = adjList.getOrDefault(node, new ArrayList<>());
            for (Pair<Integer, Double> neighborPair : neighbors) {
                int neighbor = neighborPair.getKey();
                double edgeProb = neighborPair.getValue();
                // If the neighbor is not visited, push it to the priority queue
                if (!visited[neighbor]) {
                    pq.offer(new Pair<>(prob * edgeProb, neighbor));
                }
            }
        }
        
        // Return the distance to the end node
        return distance[end];
    }
    
    public static class Pair<K, V> {
        private final K key;
        private final V value;
        
        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
        
        public K getKey() {
            return key;
        }
        
        public V getValue() {
            return value;
        }
    }
}

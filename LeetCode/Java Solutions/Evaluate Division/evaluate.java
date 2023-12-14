import java.util.*;

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // Initialize adjacency list
        Map<String, List<Pair<String, Double>>> graph = new HashMap<>();
        
        // Construct the graph
        for (int i = 0; i < equations.size(); i++) {
            List<String> equation = equations.get(i);
            double value = values[i];
            String a = equation.get(0);
            String b = equation.get(1);
            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(a).add(new Pair<>(b, value));
            graph.get(b).add(new Pair<>(a, 1/value));
        }
        
        // Prepare result array
        double[] ans = new double[queries.size()];
        
        // For each query, apply BFS to find the result
        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            ans[i] = bfs(query.get(0), query.get(1), graph, new HashSet<>());
        }
        
        return ans;
    }
    
    private double bfs(String start, String end, Map<String, List<Pair<String, Double>>> graph, Set<String> visited) {
        // If start or end node does not exist, return -1.0
        if (!graph.containsKey(start) || !graph.containsKey(end)) {
            return -1.0;
        }
        
        // Initialize queue for BFS, starting from 'start' node
        Queue<Pair<String, Double>> queue = new LinkedList<>();
        queue.offer(new Pair<>(start, 1.0));
        visited.add(start);
        
        while (!queue.isEmpty()) {
            // Pop a node from the front of the queue
            Pair<String, Double> node = queue.poll();
            String currNode = node.getKey();
            double currVal = node.getValue();
            
            // If the current node is the end node, return the value
            if (currNode.equals(end)) {
                return currVal;
            }
            
            // Add all unvisited neighbors to the queue
            for (Pair<String, Double> neighbor : graph.get(currNode)) {
                if (!visited.contains(neighbor.getKey())) {
                    visited.add(neighbor.getKey());
                    queue.offer(new Pair<>(neighbor.getKey(), currVal * neighbor.getValue()));
                }
            }
        }
        
        // If no path found, return -1.0
        return -1.0;
    }
}

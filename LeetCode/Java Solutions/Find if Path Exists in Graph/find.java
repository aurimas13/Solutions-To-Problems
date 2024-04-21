import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) {
            return true;
        }

        // Build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }

        // BFS to check path
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(source);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (node == destination) {
                return true;
            }
            if (!visited.contains(node)) {
                visited.add(node);
                for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
                    if (!visited.contains(neighbor)) {
                        queue.offer(neighbor);
                    }
                }
            }
        }

        return false;
    }
}

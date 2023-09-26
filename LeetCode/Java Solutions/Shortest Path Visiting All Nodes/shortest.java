import java.util.*;

class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        int target = (1 << n) - 1;
        Set<String> visited = new HashSet<>();
        Queue<int[]> queue = new LinkedList<>();
        
        // Initialize by adding all nodes to the queue
        for (int i = 0; i < n; i++) {
            queue.offer(new int[]{i, 1 << i});
            visited.add(i + "," + (1 << i));
        }
        
        int step = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] current = queue.poll();
                int node = current[0];
                int state = current[1];
                if (state == target) {
                    return step;
                }
                
                for (int nextNode : graph[node]) {
                    int nextState = state | (1 << nextNode);
                    String key = nextNode + "," + nextState;
                    if (!visited.contains(key)) {
                        visited.add(key);
                        queue.offer(new int[]{nextNode, nextState});
                    }
                }
            }
            step++;
        }
        
        return -1;
    }
}

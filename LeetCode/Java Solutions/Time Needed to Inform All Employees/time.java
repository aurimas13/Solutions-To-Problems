import java.util.*;

class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < manager.length; i++) {
            if (!graph.containsKey(manager[i])) {
                graph.put(manager[i], new ArrayList<>());
            }
            graph.get(manager[i]).add(i);
        }

        return dfs(headID, graph, informTime);
    }

    private int dfs(int node, Map<Integer, List<Integer>> graph, int[] informTime) {
        int maxTime = 0;
        if (graph.containsKey(node)) {
            for (int child : graph.get(node)) {
                maxTime = Math.max(maxTime, dfs(child, graph, informTime));
            }
        }
        return maxTime + informTime[node];
    }

    // Tests:
    public static void main(String[] args) {
        Solution instance = new Solution();
        int n = 1;
        int headID = 0;
        int[] manager = {-1};
        int[] informTime = {0};
        // n = 1, headID = 0, manager = [-1], informTime = [0] -> 0
        // n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] _> 1
        System.out.println(instance.numOfMinutes(n, headID, manager, informTime));
    }
}

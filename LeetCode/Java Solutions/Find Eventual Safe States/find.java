import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];  // Initialize color array with all nodes as unvisited (0)

        List<Integer> ans = new ArrayList<>();  // List to store the indices of all safe nodes
        for (int i = 0; i < n; ++i) {  // Loop through all nodes in the graph
            if (dfs(i, color, graph)) {  // If a node is safe, add it to the answer list
                ans.add(i);
            }
        }

        return ans;  // Return the list of safe nodes
    }

    public boolean dfs(int node, int[] color, int[][] graph) {
        if (color[node] > 0) {  // If the node has been visited before, return true if it is safe
            return color[node] == 1;
        }

        color[node] = 2;  // Mark the node as currently visiting (unsafe)
        for (int nei: graph[node]) {  // Loop through all neighbors of the current node
            if (!dfs(nei, color, graph)) {  // If any of the neighbors is unsafe or currently visiting, mark the current node as unsafe
                return false;
            }
        }

        color[node] = 1;  // If all neighbors are safe, mark the current node as safe
        return true;  // Return true as the node is safe
    }
}

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        // Initialize color array for storing colors
        int[] colors = new int[n];
        // fill colors array with -1 indicating no color assigned yet
        Arrays.fill(colors, -1);  

        // handle the case of non-connected graph
        for (int i = 0; i < n; ++i) {  
            if (colors[i] == -1) {
                Queue<Integer> queue = new LinkedList<>();
                // assign the first color
                colors[i] = 0;  
                queue.offer(i);
                
                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    for (int neighbour : graph[node]) {
                        // if neighbour has not been colored yet
                        if (colors[neighbour] == -1) {  
                            queue.offer(neighbour);
                            // color it with the opposite color
                            colors[neighbour] = colors[node] ^ 1;  
                        // if neighbour has been colored and its color is the same as current node
                        } else if (colors[neighbour] == colors[node]) {  
                            // the graph is not bipartite
                            return false;  
                        }
                    }
                }
            }
        }
        return true;  // the graph is bipartite
    }
}

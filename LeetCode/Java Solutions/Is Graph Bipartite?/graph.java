import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];
        Arrays.fill(colors, -1);  // fill colors array with -1 indicating no color assigned yet

        for (int i = 0; i < n; ++i) {  // handle the case of non-connected graph
            if (colors[i] == -1) {
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                colors[i] = 0;  // assign the first color
                
                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    for (int neighbour : graph[node]) {
                        if (colors[neighbour] == -1) {  // if neighbour has not been colored yet
                            queue.offer(neighbour);
                            colors[neighbour] = colors[node] ^ 1;  // color it with the opposite color
                        } else if (colors[neighbour] == colors[node]) {  // if neighbour has been colored and its color is the same as current node
                            return false;  // the graph is not bipartite
                        }
                    }
                }
            }
        }
        return true;  // the graph is bipartite
    }
}

import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        // Create a visited array to keep track of which cities have been visited
        int[] visited = new int[n];
        // Initialize the number of provinces to 0
        int numProvinces = 0;

        for (int i = 0; i < n; i++) {
            // If the city has not been visited yet
            if (visited[i] == 0) {
                // Use BFS to traverse all the cities that are directly or indirectly connected to it
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                visited[i] = 1;
                while (!queue.isEmpty()) {
                    int city = queue.poll();
                    for (int j = 0; j < n; j++) {
                        if (isConnected[city][j] == 1 && visited[j] == 0) {
                            queue.offer(j);
                            visited[j] = 1;
                        }
                    }
                }
                // Increase the number of provinces by 1
                numProvinces++;
            }
        }
        return numProvinces;
    }
}

import java.util.*;

class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        // Create an array to store count of connections for each city
        int[] count = new int[n];
        
        // Create a set to check if two cities are directly connected
        Set<String> connected = new HashSet<>();
        
        // Update the count array and connected set
        for(int[] road: roads) {
            int u = road[0];
            int v = road[1];
            count[u]++;
            count[v]++;
            // Store the connection as a string in the set
            connected.add(u + "," + v);
            connected.add(v + "," + u);
        }
        
        // Initialize the result
        int res = 0;
        
        // Check every combination of two cities
        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                // If two cities are connected, we subtract 1
                if(connected.contains(i + "," + j)) {
                    res = Math.max(res, count[i] + count[j] - 1);
                } else {
                    res = Math.max(res, count[i] + count[j]);
                }
            }
        }
        
        return res;
    }
}

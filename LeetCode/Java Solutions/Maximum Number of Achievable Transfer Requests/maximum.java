import java.util.List;

public class Solution {
    
    public int maximumRequests(int n, int[][] requests) {
        // Number of requests
        int m = requests.length;
        
        // Keep track of maximum number of achievable requests
        int maxRequests = 0;
        
        // Loop through all subsets of requests (2^m possibilities)
        for (int i = 1; i < (1 << m); i++) {
            // Building transfer counts, inCount[j] - outCount[j] for building j
            int[] buildings = new int[n];
            
            // Count number of set bits (i.e., included requests)
            int numRequests = 0;
            
            // Loop through each request and update building transfer counts
            for (int j = 0; j < m; j++) {
                // Check if jth bit is set
                if ((i & (1 << j)) > 0) {
                    // Increment incoming transfer count for target building
                    buildings[requests[j][1]] += 1;
                    // Decrement outgoing transfer count for source building
                    buildings[requests[j][0]] -= 1;
                    // Increment number of included requests
                    numRequests += 1;
                }
            }
            
            // Check if the subset is valid (inCount[j] == outCount[j] for all buildings)
            boolean isValid = true;
            for (int count : buildings) {
                if (count != 0) {
                    isValid = false;
                    break;
                }
            }
            
            // Update the maximum number of achievable requests
            if (isValid) {
                maxRequests = Math.max(maxRequests, numRequests);
            }
        }
        
        return maxRequests;
    }
}
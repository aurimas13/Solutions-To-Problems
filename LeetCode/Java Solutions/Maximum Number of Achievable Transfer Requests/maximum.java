from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # Number of requests
        m = len(requests)
        
        # Keep track of maximum number of achievable requests
        max_requests = 0
        
        # Loop through all subsets of requests (2^m possibilities)
        for i in range(1, 1 << m):
            # Building transfer counts, in_count[j] - out_count[j] for building j
            buildings = [0] * n
            
            # Count number of set bits (i.e., included requests)
            num_requests = 0
            
            # Loop through each request and update building transfer counts
            for j in range(m):
                # Check if jth bit is set
                if i & (1 << j):
                    # Increment incoming transfer count for target building
                    buildings[requests[j][1]] += 1
                    # Decrement outgoing transfer count for source building
                    buildings[requests[j][0]] -= 1
                    # Increment number of included requests
                    num_requests += 1
            
            # Check if the subset is valid (in_count[j] == out_count[j] for all buildings)
            if all(count == 0 for count in buildings):
                # Update the maximum number of achievable requests
                max_requests = max(max_requests, num_requests)
                
        return max_requests

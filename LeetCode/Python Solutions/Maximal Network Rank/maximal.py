from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Create an array to store count of connections for each city
        count = [0] * n
        
        # Create a set to check if two cities are directly connected
        connected = set()
        
        # Update the count array and connected set
        for u, v in roads:
            count[u] += 1
            count[v] += 1
            # Store the connection as a tuple in the set
            connected.add((u, v))
            connected.add((v, u))
        
        # Initialize the result
        res = 0
        
        # Check every combination of two cities
        for i in range(n):
            for j in range(i+1, n):
                # If two cities are connected, we subtract 1
                if (i, j) in connected:
                    res = max(res, count[i] + count[j] - 1)
                else:
                    res = max(res, count[i] + count[j])
        
        return res

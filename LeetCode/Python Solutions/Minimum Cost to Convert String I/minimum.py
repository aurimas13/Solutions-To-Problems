class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        import sys
        
        # Number of unique lowercase English letters
        n = 26
        INF = float('inf')
        
        # Initialize the cost graph with infinity
        dist = [[INF] * n for _ in range(n)]
        
        # Distance from a node to itself is zero
        for i in range(n):
            dist[i][i] = 0
        
        # Convert characters to their respective indices (0-25)
        def char_to_index(c):
            return ord(c) - ord('a')
        
        # Fill in the initial costs based on the given transformations
        for i in range(len(original)):
            u = char_to_index(original[i])
            v = char_to_index(changed[i])
            dist[u][v] = min(dist[u][v], cost[i])
        
        # Floyd-Warshall algorithm to compute shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate the minimum cost to convert source to target
        total_cost = 0
        for i in range(len(source)):
            s = char_to_index(source[i])
            t = char_to_index(target[i])
            if s == t:
                continue
            if dist[s][t] == INF:
                return -1
            total_cost += dist[s][t]
        
        return total_cost

# Example usage:
sol = Solution()
print(sol.minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))  # Output: 28
print(sol.minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))  # Output: 12
print(sol.minimumCost("abcd", "abce", ["a"], ["e"], [10000]))  # Output: -1

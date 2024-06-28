from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Count the number of connections for each city
        connections = [0] * n
        for a, b in roads:
            connections[a] += 1
            connections[b] += 1
        
        # Step 2: Sort the cities based on the number of connections
        sorted_cities = sorted(range(n), key=lambda x: connections[x], reverse=True)
        
        # Step 3: Assign values to cities based on their sorted order
        values = [0] * n
        for i in range(n):
            values[sorted_cities[i]] = n - i
        
        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]
        
        return total_importance

# Example usage:
sol = Solution()
print(sol.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # Output: 43
print(sol.maximumImportance(5, [[0,3],[2,4],[1,3]]))  # Output: 20

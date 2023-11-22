from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        minCost = [0] * n
        minCost[0], minCost[1] = cost[0], cost[1]
        
        for i in range(2, n):
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
            
        return min(minCost[n-1], minCost[n-2])

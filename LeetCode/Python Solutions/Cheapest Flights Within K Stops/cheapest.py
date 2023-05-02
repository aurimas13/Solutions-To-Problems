from typing import List


class Solution:
    def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a list to store the shortest distance to each city
        dist = [float('inf')] * n
        dist[src] = 0

        # Use Bellman-Ford algorithm to find the cheapest price from src to dst
        for _ in range(k + 1):
            new_dist = dist[:]
            for f in flights:
                new_dist[f[1]] = min(new_dist[f[1]], dist[f[0]] + f[2])
            dist = new_dist

        return dist[dst] if dist[dst] != float('inf') else -1


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
    # n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 -> 700
    # n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 -> 500
    print(Solve)

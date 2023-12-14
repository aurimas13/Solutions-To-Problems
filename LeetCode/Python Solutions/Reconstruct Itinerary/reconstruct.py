from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Construct the graph
        graph = defaultdict(list)
        for source, dest in sorted(tickets):
            heapq.heappush(graph[source], dest)

        path = []

        def dfs(airport):
            while graph[airport]:
                dfs(heapq.heappop(graph[airport]))
            path.append(airport)

        dfs('JFK')
        return path[::-1]  # reverse the path to get the answer

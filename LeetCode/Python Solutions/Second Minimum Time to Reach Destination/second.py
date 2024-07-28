from heapq import heappush, heappop

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize distances array and priority queue
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        pq = [(0, 1)]  # (time, node)
        dist[1][0] = 0
        
        while pq:
            curr_time, node = heappop(pq)
            
            # If we've found the second minimum time to reach node n, return it
            if node == n and dist[n][1] != float('inf'):
                return dist[n][1]
            
            # Calculate the actual time considering traffic signal changes
            actual_time = curr_time
            if (actual_time // change) % 2 == 1:
                actual_time = (actual_time // change + 1) * change
            actual_time += time
            
            for neighbor in graph[node]:
                if actual_time < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = actual_time
                    heappush(pq, (actual_time, neighbor))
                elif dist[neighbor][0] < actual_time < dist[neighbor][1]:
                    dist[neighbor][1] = actual_time
                    heappush(pq, (actual_time, neighbor))
        
        return -1  # Should never reach here given the problem constraints
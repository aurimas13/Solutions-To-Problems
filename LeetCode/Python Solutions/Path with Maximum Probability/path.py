class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
            # Create adjacency list
            adj_list = defaultdict(list)
            for i, edge in enumerate(edges):
                adj_list[edge[0]].append((edge[1], succProb[i]))
                adj_list[edge[1]].append((edge[0], succProb[i]))
            
            # Initialize distance and visited arrays
            distance = [0] * n
            visited = [False] * n
            
            # Initialize priority queue
            pq = []
            heapq.heappush(pq, (-1, start))
            
            # Iterate until priority queue is empty
            while pq:
                # Pop the node with the highest probability
                prob, node = heapq.heappop(pq)
                
                # If the node is already visited, continue
                if visited[node]:
                    continue
                
                # Mark the node as visited
                visited[node] = True
                
                # Update distance
                distance[node] = -prob
                
                # Iterate through the neighbors of the node
                for neighbor, edge_prob in adj_list[node]:
                    # If the neighbor is not visited, push it to the priority queue
                    if not visited[neighbor]:
                        heapq.heappush(pq, (prob * edge_prob, neighbor))
            
            # Return the distance to the end node
            return distance[end]

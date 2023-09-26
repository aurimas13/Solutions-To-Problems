from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target = (1 << n) - 1 # This is when all nodes are visited
        visited = set()
        queue = deque()
        
        # Initialize by adding all nodes to the queue
        for i in range(n):
            queue.append((i, 1 << i))  # (node, state)
            visited.add((i, 1 << i))
        
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, state = queue.popleft()
                if state == target:
                    return step
                
                for next_node in graph[node]:
                    next_state = state | (1 << next_node)
                    if (next_node, next_state) not in visited:
                        visited.add((next_node, next_state))
                        queue.append((next_node, next_state))
            
            step += 1
        
        return -1

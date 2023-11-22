from typing import List
from heapq import heappop, heappush
from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        visited = {}
        while heap:
            t, u = heappop(heap)
            if u not in visited:
                visited[u] = t
                for v, w in graph[u]:
                    heappush(heap, (t + w, v))
        return -1 if len(visited) < n else max(visited.values())


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)  # times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 -> 2 | times = [[1,2,1]], n = 2, k = 1 -> 1 | times = [[1,2,1]], n = 2, k = 2 -> -1
    print(Solve)


# OR
#
# def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#     graph = defaultdict(list)
#     for u, v, w in times:
#         graph[u].append((v, w))
#     queue = deque([(0, k)])
#     visited = {}
#     while queue:
#         t, u = queue.popleft()
#         if u not in visited or t < visited[u]:
#             visited[u] = t
#             for v, w in graph[u]:
#                 queue.append((t + w, v))
#     return -1 if len(visited) < n else max(visited.values())
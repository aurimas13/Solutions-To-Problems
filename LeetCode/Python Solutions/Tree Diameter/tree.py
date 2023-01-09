from typing import List
from collections import deque, defaultdict


class Solution:
    @staticmethod
    def treeDiameter(edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        search_queue = deque([])
        search_queue.append((0, -1))

        while search_queue:
            node, parent = search_queue.popleft()
            for neighbour in graph[node]:
                if neighbour != parent:
                    search_queue.append((neighbour, node))

        search_queue = deque([])
        search_queue.append((node, 0, [node]))

        while search_queue:
            node, distance, path = search_queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in set(path):
                    search_queue.append((neighbour, distance + 1, path + [neighbour]))

        return distance


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.treeDiameter(
        edges = [[0,1],[1,2],[2,3],[1,4],[4,5]])
    # edges = [[0,1],[0,2]] -> 2
    # edges = [[0,1],[1,2],[2,3],[1,4],[4,5]] -> 4
    print(Solve)

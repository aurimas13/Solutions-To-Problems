from typing import List
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        queue = deque([i for i in range(n) if len(adj[i]) == 1])
        while queue:
            i = queue.popleft()
            if not adj[i]:
                continue
            nb = adj[i].pop()
            adj[nb].discard(i)
            if len(adj[nb]) == 1:
                queue.append(nb)

        return all([len(x) == 0 for x in adj])


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])  # n = 5, edges = [[0,1],[0,2],[0,3],[1,4]] -> true | n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]] -> false
    print(Solve)
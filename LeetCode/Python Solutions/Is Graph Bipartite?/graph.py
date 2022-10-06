from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def helper(node, graph, a, b):
            a.add(node)
            for v in graph[node]:
                if v in b: continue
                if v in a or not helper(v, graph, b, a):
                    return False
            return True

        a, b = set(), set()
        for u in range(len(graph)):
            if u in a or u in b: continue
            if not helper(u, graph, a, b):
                return False
        return True


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]) # graph = [[1,2,3],[0,2],[0,1,3],[0,2]] -> False
    print(Solve)

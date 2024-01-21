from typing import List
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        1) Create Graph from words
        2) If cycle exist => No ordering; return ""
        3) Topological sort and join
        Note: It might be possible to merge (2) in (3) but I kept them separate to make code decoupled and easy to         debug
        """
        # (1)
        graph = {x: [] for x in set(''.join(words))}
        for i in range(len(words) - 1):
            s1, s2 = words[i], words[i + 1]
            n, m = len(s1), len(s2)
            x = y = 0
            while x < n and y < m:
                if s1[x] == s2[y]:
                    x += 1
                    y += 1
                else:
                    graph[s1[x]].append(s2[y])
                    break
            else:
                if x < n and y == m:
                    return ""

        def toposort(start):
            vstd[start] = True
            for node in graph[start]:
                if not vstd[node]:
                    toposort(node)
            order.append(f"{start}")

        def has_cycle(start):
            vstd[start] = True
            instack[start] = True
            for node in graph[start]:
                if instack[node]:
                    return True
                if not vstd[node] and has_cycle(node):
                    return True
            instack[start] = False
            return False

        # (2)
        vstd = defaultdict(lambda: False)
        instack = defaultdict(lambda: False)
        for node in graph:
            if not vstd[node] and has_cycle(node):
                return ""

        # (3)
        order = []
        vstd.clear()
        for node in graph:
            if not vstd[node]:
                toposort(node)

        return ''.join(order[::-1]) or ""


# Instantiation to check values
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.alienOrder(words = ["wrt","wrf","er","ett","rftt"])  # words = ["wrt","wrf","er","ett","rftt"] -> "wertf"
    print(Solve)

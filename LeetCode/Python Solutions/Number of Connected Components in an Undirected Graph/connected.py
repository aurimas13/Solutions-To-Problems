from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        parent = [i for i in range(n)]

        def find(i):
            ind = i
            while(parent[ind] != ind):
                ind = parent[ind]

            while(parent[i]!=i):
                temp = parent[i]
                parent[i] = ind
                i = temp

            return ind

        def union(i,j):
            nonlocal components
            pi = find(i)
            pj = find(j)

            if pi == pj:
                return

            parent[pi] = pj
            components -= 1

        for edge in edges:
            union(edge[0],edge[1])

        return components


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])  # n = 5, edges = [[0,1],[1,2],[2,3],[3,4]] -> 1
    print(Solve)
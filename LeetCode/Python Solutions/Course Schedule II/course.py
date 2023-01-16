from collections import deque
from typing import List


class Solution:
    @staticmethod
    def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result if len(result) == numCourses else []


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findOrder(numCourses = 2, prerequisites = [[1,0]])
    # numCourses = 2, prerequisites = [[1,0]] -> [0,1]
    # numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] -> [0,2,1,3]
    print(Solve)
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Define an adjacency list
        adj_list = [[] for _ in range(numCourses)]
        # Define a visit list, 0 means unvisited, 1 means being visited, 2 means completely visited
        visit = [0] * numCourses

        # Convert edge list to adjacency list
        for x, y in prerequisites:
            adj_list[x].append(y)

        # Define a helper function to do DFS
        def dfs(i):
            # If it is being visited, then we have a cycle, thus return False
            if visit[i] == 1:
                return False
            # If it is done visited, then do not visit again
            if visit[i] == 2:
                return True
            # Mark as being visited
            visit[i] = 1
            # Visit all the neighbours
            for j in adj_list[i]:
                if not dfs(j):
                    return False
            # After visit all the neighbours, mark it as done visited
            visit[i] = 2
            return True

        # Do DFS from each node
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


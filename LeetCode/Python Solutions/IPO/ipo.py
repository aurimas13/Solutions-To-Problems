from heapq import heappush, heappop
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair projects with their capital requirements and profits
        projects = list(zip(capital, profits))
        
        # Sort projects by their capital requirements
        projects.sort()
        
        max_heap = []
        project_index = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all projects that can be started with the current capital into the heap
            while project_index < n and projects[project_index][0] <= w:
                heappush(max_heap, -projects[project_index][1])  # Use negative profit to simulate max-heap
                project_index += 1
            
            # If there are no projects that can be started, break out
            if not max_heap:
                break
            
            # Pop the project with the maximum profit
            w += -heappop(max_heap)
        
        return w

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(sol.findMaximizedCapital(k, w, profits, capital))  # Output: 4

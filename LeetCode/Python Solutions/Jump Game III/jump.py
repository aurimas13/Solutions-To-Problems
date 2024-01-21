from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Edge case: If the starting index is already 0, return True
        if arr[start] == 0:
            return True

        # Initialize a queue for BFS
        queue = deque([start])

        # Initialize a set to keep track of visited indices
        visited = set()

        # Perform BFS
        while queue:
            curr = queue.popleft()

            # Check if the current index is 0
            if arr[curr] == 0:
                return True

            # Add the two possible next indices to the queue
            # If they are within the bounds of the array and have not been visited yet
            if curr + arr[curr] < len(arr) and curr + arr[curr] not in visited:
                queue.append(curr + arr[curr])
                visited.add(curr + arr[curr])
            if curr - arr[curr] >= 0 and curr - arr[curr] not in visited:
                queue.append(curr - arr[curr])
                visited.add(curr - arr[curr])

        # If we have exhausted all possibilities and have not found a 0, return False
        return False


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.canReach(arr = [4,2,3,0,3,1,2], start = 5)
    # Test cases:
    # arr = [4,2,3,0,3,1,2], start = 5 -> True
    # arr = [3,0,2,1,2], start = 2 -> False
    # arr = [4,2,3,0,3,1,2], start = 0 -> True
    print(Solve)

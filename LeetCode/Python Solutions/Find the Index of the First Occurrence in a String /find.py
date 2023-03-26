import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Initialize the heap with the first element of each row
        heap = [(sum(row[0] for row in mat), [0] * len(mat))]
        # Initialize a set to store the visited states
        visited = set(tuple(state) for _, state in heap)
        # Loop until we find the kth smallest sum or the heap is empty
        for i in range(k-1):
            # Get the current smallest sum and state from the heap
            current_sum, state = heapq.heappop(heap)
            # Generate all possible next states by incrementing the index of the current element in each row
            for j, index in enumerate(state):
                if index < len(mat[j])-1:
                    next_state = list(state)
                    next_state[j] += 1
                    # Check if we've already visited this state
                    if tuple(next_state) not in visited:
                        # Add the new sum and state to the heap and mark the state as visited
                        next_sum = current_sum + mat[j][index+1] - mat[j][index]
                        heapq.heappush(heap, (next_sum, next_state))
                        visited.add(tuple(next_state))
        # Return the kth smallest sum
        return heap[0][0]


# Checking in terminal/console:
if __name__ == '__main__':
    sol = Solution()
    mat = [[1,3,11],[2,4,6]]
    k = 5
    print(sol.kthSmallest(mat, k))  # Expected output: 7

    mat = [[1,3,11],[2,4,6]]
    k = 9
    print(sol.kthSmallest(mat, k))  # Expected output: 17

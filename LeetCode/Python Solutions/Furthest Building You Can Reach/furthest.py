import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Min heap to keep track of the largest jumps where ladders are used
        heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            # If the next building is taller, add the difference to the heap
            if diff > 0:
                heapq.heappush(heap, diff)
            
            # If we have more ladders than needed, remove the smallest jump from the heap
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            
            # If we run out of bricks, return the current index
            if bricks < 0:
                return i
        
        # If we didn't run out of bricks, we can reach the last building
        return len(heights) - 1

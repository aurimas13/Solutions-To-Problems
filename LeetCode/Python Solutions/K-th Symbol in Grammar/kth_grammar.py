from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        # Min-heap to store tuples of (fraction value, numerator index, denominator index)
        min_heap = [(arr[0] / arr[j], 0, j) for j in range(1, n)]
        heapq.heapify(min_heap)
        
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(min_heap)
            # Move to the next fraction with the same numerator but next smaller denominator
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
        
        return [arr[min_heap[0][1]], arr[min_heap[0][2]]]

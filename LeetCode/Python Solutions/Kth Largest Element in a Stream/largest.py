import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If heap size is less than k, we can directly push the element
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Else we compare the incoming element with the minimum element (root of the heap)
        # if incoming element is greater, it will replace the root
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        # Return the root of the heap as the kth largest element
        return self.heap[0]


# Tests:
if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))  # returns 4
    print(obj.add(5))  # returns 5
    print(obj.add(10)) # returns 5
    print(obj.add(9))  # returns 8
    print(obj.add(4))  # returns 8

from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.hi, self.lo = [], []

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)
        heappush(self.hi, -heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) > len(self.hi) else .5*(-self.lo[0] + self.hi[0])

# Tests:
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    Solve = obj.findMedian()
    # [1,2] -> 1.5
    print(Solve)
    obj.addNum(3)
    Solve = obj.findMedian()
    # [1,2,3] -> 2
    print(Solve)
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort()
        heap = []

        room = 0
        for interval in intervals:
            if not heap or heap[0][0] > interval[0]:
                room += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, (interval[1], interval[0]))

        return room


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.minMeetingRooms([[0,30],[5,10],[15,20]])  #intervals = [[0,30],[5,10],[15,20]] -> 2
    print(Solve)

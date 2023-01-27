from typing import List
import heapq


class Solution:
    @staticmethod
    def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for (L, R, H) in buildings]
        events += [(R, 0, 0) for (_, R, _) in buildings]
        events.sort()

        ans = [(0, 0)]
        live = [(0, float("inf"))]
        for (L, negH, R) in events:
            while live[0][1] <= L:
                heapq.heappop(live)
            if negH:
                heapq.heappush(live, (negH, R))
            if ans[-1][1] != -live[0][0]:
                ans.append((L, -live[0][0]))
        return ans[1:]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
    # buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]] ->
    # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    print(Solve)
from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                d[dist] += 1
            for k in d.values():
                res += k * (k - 1)
        return res

# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numberOfBoomerangs(points = [[0,0],[1,0],[2,0]])
    # points = [[0,0],[1,0],[2,0]] -> 2
    # points = [[1,1],[2,2],[3,3]] -> 2
    print(Solve)



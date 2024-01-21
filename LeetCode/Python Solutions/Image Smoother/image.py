from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img:
            return []

        rows, cols = len(img), len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                count = 0
                _sum = 0

                for x in range(max(0, i-1), min(i+2, rows)):
                    for y in range(max(0, j-1), min(j+2, cols)):
                        _sum += img[x][y]
                        count += 1

                res[i][j] = _sum // count

        return res

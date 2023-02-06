from typing import List


class Solution:
    @staticmethod
    def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
                if not rowSum[i]:
                    break

        return res


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.restoreMatrix(rowSum = [3,8], colSum = [4,7])
    # rowSum = [3,8], colSum = [4,7]
    # -> [[3,0], [1,7]]
    # rowSum = [5,7,10], colSum = [8,6,8]
    # -> [[0,5,0], [6,1,0], [2,0,8]]
    print(Solve)

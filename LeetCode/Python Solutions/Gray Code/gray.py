from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        arr = self.grayCode(n - 1)
        return arr + [(1 << (n - 1)) + k for k in arr[::-1]]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.grayCode(n = 2)
    # n = 2 -> [0,1,3,2]
    # n = 1 -> [0,1]
    print(Solve)

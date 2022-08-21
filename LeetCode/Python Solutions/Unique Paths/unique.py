from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(x,y):
            if (x,y) in mem:
                return mem[(x,y)]
            if x == 1 and y == 1:
                return 1
            if x < 1 or y < 1:
                return 0
            mem[(x,y)] = paths(x,y-1) + paths(x-1,y)
            return mem[(x,y)]
        mem = {}
        return paths(m,n)



if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.uniquePaths( m = 3, n = 7) # m = 3, n = 2 -> 3 | m = 3, n = 7 -> 28
    print(Solve)

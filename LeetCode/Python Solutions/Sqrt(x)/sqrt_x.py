import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.mySqrt(int(input()))  # 8 gives 2, 4 gives 2
    print(Solve)
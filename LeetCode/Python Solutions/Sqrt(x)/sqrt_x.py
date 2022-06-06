import math
class Solution:
    def mySqrt(self, x: int) -> int:
        class Solution:
            def mySqrt(self, x):
                if x < 2:
                    return x

                x0 = x
                x1 = (x0 + x / x0) / 2
                while abs(x0 - x1) >= 1:
                    x0 = x1
                    x1 = (x0 + x / x0) / 2

                return int(x1)

# or
# return math.floor(math.sqrt(x))

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.mySqrt(int(input()))  # 8 gives 2, 4 gives 2
    print(Solve)
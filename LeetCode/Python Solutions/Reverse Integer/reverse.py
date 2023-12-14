import math
class Solution:
    def reverse(self, x: int) -> int:
        return int(math.copysign(int(str(x).replace('-','')[::-1]), x))
        # if x > 0:
        #     return int(math.copysign(int(str(x)[::-1]), x))
        # else:
        #     return int(math.copysign(int(str(x).replace('-','')[::-1]), x))


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.reverse(-120)  # 123 -> 321 | -123 -> -321 | 120 -> 21 | -120 -> -21
    print(Solve)
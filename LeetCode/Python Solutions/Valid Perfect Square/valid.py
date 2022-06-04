from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num // 2
        y = set([x])
        while x * x != num:
            if x == 0:
                return True
            else:
                x = (x + (num // x)) // 2
            if x in y: return False
            y.add(x)
        return True

        # if num < 0:
        #     return False
        # if num == 0:
        #     return True
        # if num == 1:
        #     return True
        # if num > 1:
        #     for i in range(0, num):
        #         if i * i == num:
        #             return True
        # return False

        # import math
        # if (num < 0):
        #     return False
        # if (int(math.sqrt(num)) == math.sqrt(num)):
        #     return True
        # else:
        #     return False

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPerfectSquare(17) # 36 -> True | 17 -> False
    print(Solve)
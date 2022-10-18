from math import sqrt
class Solution:
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:
            x = (left + right) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        return False

        # or

        # x = num // 2
        # y = set([x])
        # while x * x != num:
        #     if x == 0:
        #         return True
        #     else:
        #         x = (x + (num // x)) // 2
        #     if x in y: return False
        #     y.add(x)
        # return True

        # or

        # import math
        # if (num < 0):
        #     return False
        # if (int(math.sqrt(num)) == math.sqrt(num)):
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPerfectSquare(49) # 36 -> True | 17 -> False
    print(Solve)

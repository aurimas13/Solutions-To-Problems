from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def isHappy(n: int) -> bool:
        nums = set()
        while True:
            n = sum(int(c) ** 2 for c in str(n))
            if n == 1:
                return True

            if n in nums:
                return False
            nums.add(n)


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isHappy(n = 19)
    # n = 19 -> true | n = 2 -> false
    print(Solve)


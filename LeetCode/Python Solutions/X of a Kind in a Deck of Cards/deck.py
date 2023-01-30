from typing import List
from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    @staticmethod
    def hasGroupsSizeX(deck: List[int]) -> bool:
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.hasGroupsSizeX([1,2,3,4,4,3,2,1])
    # [1,2,3,4,4,3,2,1] -> true | deck = [1,1,1,2,2,2,3,3] -> false
    print(Solve)

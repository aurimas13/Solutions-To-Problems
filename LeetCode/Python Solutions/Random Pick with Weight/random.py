from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        curr = 0
        self.prefix_sums = [curr := curr + i for i in w]
        self.sum = curr

    def pickIndex(self) -> int:
        res = self.sum * random.random()
        l, r = 0, len(self.prefix_sums)
        while l < r:
            m = l + (r - l) // 2
            if res > self.prefix_sums[m]:
                l = m + 1
            else:
                r = m
        return l

from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        MOD = 10**9 + 7
        count = defaultdict(int)

        for num in nums:
            count[num - rev(num)] += 1

        nicePairs = 0
        for freq in count.values():
            nicePairs += freq * (freq - 1) // 2

        return nicePairs % MOD

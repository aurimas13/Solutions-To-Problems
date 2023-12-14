from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        Finds the maximum possible sum of the shorter two billboards from the given set of rods. 
        The rods list contains the lengths of all the rods.
        Returns the maximum possible sum of the shorter two billboards.
        """
        dp = {0: 0}
        for x in rods:
            dp2 = dict(dp)
            for d, y in dp.items():
                dp2[d + x] = max(dp2.get(d + x, 0), y)
                dp2[abs(d - x)] = max(dp2.get(abs(d - x), 0), y + min(d, x))
            dp = dp2
        return dp[0]

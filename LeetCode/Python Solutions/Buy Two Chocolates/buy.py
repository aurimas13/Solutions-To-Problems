from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = float('inf')

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                cost = prices[i] + prices[j]
                if cost <= money:
                    min_cost = min(min_cost, cost)

        return money if min_cost == float('inf') else money - min_cost

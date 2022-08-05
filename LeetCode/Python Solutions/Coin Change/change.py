from typing import List
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set([amount])
        while q:
            accum_amount, num_coins = q.popleft()
            if accum_amount == 0:
                return num_coins
            for coin in coins:
                if accum_amount - coin >= 0 and accum_amount - coin not in seen:
                    q.append((accum_amount - coin, num_coins + 1))
                    seen.add(accum_amount - coin)

        return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.coinChange([1,2,5], 11)  # coins = [1,2,5], amount = 11 -> 3 | coins = [2], amount = 3 -> -1
    print(Solve)
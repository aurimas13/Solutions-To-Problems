from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort the piles in descending order
        piles.sort(reverse=True)
        
        # Initialize total coins
        total_coins = 0
        
        # Start from the second element and pick every third element
        for i in range(1, len(piles) - len(piles) // 3, 2):
            total_coins += piles[i]
        
        return total_coins

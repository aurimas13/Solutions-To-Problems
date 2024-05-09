from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort happiness in descending order
        happiness.sort(reverse=True)
        
        max_sum = 0
        # Calculate the maximum sum by taking the top k elements
        for i in range(k):
            max_sum += max(0, happiness[i] - i)
        
        return max_sum

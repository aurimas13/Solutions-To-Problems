from typing import List
from itertools import pairwise

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        Calculates the difference between the sum of the k largest and k smallest sums of pairs of weights.

        Parameters:
            weights (List[int]): A list of integers representing the weights of the marbles.
            k (int): The number of pairs of weights to consider.

        Returns:
            int: The difference between the sum of the k largest and k smallest sums of pairs of weights.
        """
        if k == 1 or k == len(weights):
            return 0
        
        sorted_pairs = sorted(map(sum, pairwise(weights)))
        
        max_sum = sum(sorted_pairs[-k+1:])
        min_sum = sum(sorted_pairs[:k-1])
        
        return max_sum - min_sum


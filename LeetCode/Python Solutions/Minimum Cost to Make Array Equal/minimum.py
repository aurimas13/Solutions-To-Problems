from typing import List

class WeightedNum:
    def __init__(self, num, weight):
        self.num = num
        self.weight = weight

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Create and sort the list of WeightedNums
        weighted_nums = sorted([WeightedNum(n, w) for n, w in zip(nums, cost)], key=lambda x: x.num)

        # Calculate the total weight
        total_weight = sum(cost)

        # Find the number to minimize to
        current_running_weight = 0
        number_to_minimize_to = 0
        for weighted_num in weighted_nums:
            current_running_weight += weighted_num.weight
            if current_running_weight / total_weight >= 0.5:
                number_to_minimize_to = weighted_num.num
                break

        # Calculate the minimum cost
        return sum(abs(weighted_num.num - number_to_minimize_to) * weighted_num.weight 
                   for weighted_num in weighted_nums if weighted_num.num != number_to_minimize_to)


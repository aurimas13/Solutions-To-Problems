from typing import List

# Defines a class for holding a number and its associated weight
class WeightedNum:
    def __init__(self, num, weight):
        self.num = num
        self.weight = weight

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Creates a list of WeightedNum objects based on the input arrays and sorts it based on the number
        weighted_nums = sorted([WeightedNum(n, w) for n, w in zip(nums, cost)], key=lambda x: x.num)

        # Calculates the total weight by summing all the weights
        total_weight = sum(cost)

        # Initializes the running weight and the number to minimize to
        current_running_weight = 0
        number_to_minimize_to = 0

        # Iterates over the sorted list of WeightedNums
        # If the running weight exceeds half of the total weight, sets the current number as the number to minimize to
        for weighted_num in weighted_nums:
            current_running_weight += weighted_num.weight
            if current_running_weight / total_weight >= 0.5:
                number_to_minimize_to = weighted_num.num
                break

        # Returns the minimum cost by summing the product of the absolute difference between each number and the number
        # to minimize to and its weight. Only considers the numbers that are not equal to the number to minimize to
        return sum(abs(weighted_num.num - number_to_minimize_to) * weighted_num.weight 
                   for weighted_num in weighted_nums if weighted_num.num != number_to_minimize_to)


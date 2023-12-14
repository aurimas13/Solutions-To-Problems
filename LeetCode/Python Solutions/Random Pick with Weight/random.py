import random
from typing import List
from itertools import accumulate

class Solution:
    def __init__(self, w: List[int]):
        # calculate prefix sums
        self.prefix_sums = list(accumulate(w))
        # total sum
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        # generate a random number
        random_num = self.total_sum * random.random()
        # binary search for the index
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = left + (right - left) // 2
            if random_num > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    # test case
    obj = Solution([1, 3, 4])
    result = obj.pickIndex()
    print(result)
    # since the weights are 1, 3, 4, the result should be more likely to be 2

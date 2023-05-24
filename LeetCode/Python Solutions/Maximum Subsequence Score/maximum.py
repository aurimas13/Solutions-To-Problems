from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxScore(self, nums1, nums2, k):
        ans = sorted([(i,j) for i,j in zip(nums1,nums2)], key = lambda x: -x[1])

        result, total, max_val = [], 0, float("-inf")

        for i,j in ans:
            heapq.heappush(result,i)
            total += i

            if len(result) > k:
                total -= heapq.heappop(result)

            if len(result) == k:
                max_val = max(max_val,total*j)

        return max_val

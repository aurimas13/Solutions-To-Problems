from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxScore(self, nums1, nums2, k):
        # Sort the list of tuples based on the second element of each tuple in descending order
        ans = sorted([(i,j) for i,j in zip(nums1,nums2)], key = lambda x: -x[1])

        # Initialize variables
        result, total, max_val = [], 0, float("-inf")

        # Iterate over the sorted list
        for i,j in ans:
            # Add the current element from nums1 to the heap
            heapq.heappush(result,i)
            # Update the total sum of elements in the heap
            total += i

            # If the size of the heap exceeds k, remove the smallest element and update the total sum
            if len(result) > k:
                total -= heapq.heappop(result)

            # If the size of the heap is equal to k, compute the product of the total sum and the current element from nums2
            # Update max_val if the product is greater
            if len(result) == k:
                max_val = max(max_val,total*j)

        # Return the maximum product obtained
        return max_val

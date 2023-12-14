from bisect import bisect_left
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        # This nested function calculates the number of pairs in `nums` that 
        # have a difference less than or equal to `mx`.
        def pairCtr(mx: int) -> int:                       
            cnt, idx = 0, 1
            # Loop through the sorted `nums` to count such pairs.
            while idx < n:                                 
                if nums[idx] - nums[idx - 1] <= mx:
                    cnt += 1  # If difference <= mx, increment the count.
                    idx += 1  # Also, move to the next index.
                idx += 1      # Move to the next index.
            return cnt         

        # If p is 0, the required difference is 0 as no pairs need to be removed.
        if p == 0: return 0

        # Length of the nums array.
        n = len(nums)
        
        # Sort the `nums` list to compute differences easily.
        nums.sort()
        
        # Construct a set containing differences between consecutive numbers in `nums`.
        # The set is converted to a sorted list named `arr`.
        arr = sorted({nums[i] - nums[i - 1] for i in range(1, n)})
        
        # The bisect_left method is used to find the position to insert `p` in `arr` 
        # in such a way that the list remains sorted. The key for sorting is `pairCtr`.
        # The value at the found position in `arr` is the answer.
        return arr[bisect_left(arr, p, key=pairCtr)]

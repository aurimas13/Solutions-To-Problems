from typing import List
from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # Sort the arr2 for binary search
        arr2.sort()

        # Initialize a DP map with a key of -1 and value of 0
        dp = {-1: 0}

        # Iterate over each number in arr1
        for num in arr1:
            tmp = {}  # Temporary DP map for the current iteration

            # For each key (previous value) in the DP map
            for key in dp:
                # If the current number is greater than the previous value
                if num > key:  
                    # Update the minimum operations needed for the current number in the temporary DP map
                    tmp[num] = min(tmp.get(num, float('inf')), dp[key])

                # Find the position of the first number in arr2 that is greater than the key (previous value)
                idx = bisect_right(arr2, key)

                # If such a number exists in arr2
                if idx < len(arr2):
                    # Update the minimum operations needed for the number in arr2 in the temporary DP map
                    tmp[arr2[idx]] = min(tmp.get(arr2[idx], float('inf')), dp[key] + 1)
            
            # Update the DP map with the temporary DP map
            dp = tmp
        
        # If there is any possibility to make arr1 strictly increasing, return the minimum operations needed
        if dp:
            return min(dp.values())
        # If there is no way to make arr1 strictly increasing, return -1
        else:
            return -1


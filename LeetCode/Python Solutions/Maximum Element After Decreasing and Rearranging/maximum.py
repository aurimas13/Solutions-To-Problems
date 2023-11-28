from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()  # Step 1: Sort the array
        arr[0] = 1  # Step 2: Set the first element to 1

        # Step 3: Adjust subsequent elements
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1

        # Step 4: The last element is the maximum value possible
        return arr[-1]

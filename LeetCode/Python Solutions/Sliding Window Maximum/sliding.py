from collections import deque
from typing import List

class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        # Handle edge cases
        if not nums or len(nums) < k:
            raise ValueError()

        # Initialize deque (double-ended queue) and result list
        window = deque()
        res = []

        # Iterate through the input list
        for i in range(len(nums)):
            # Remove elements that are out of the current sliding window from the front of the deque
            while window and (i - k) >= window[0][1]:
                window.popleft()

            # Remove elements smaller than the current element from the back of the deque
            while window and (nums[i] >= window[-1][0]):
                window.pop()

            # Append the current element and its index to the deque
            window.append((nums[i], i))

            # Append the maximum element of the current sliding window to the result list
            if window and i >= k - 1:
                res.append(window[0][0])

        return res

#  Tests:
if __name__ == '__main__':
    # Call the 'maxSlidingWindow' method with the input list and window size
    result1 = Solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)  # Expected output: [3, 3, 5, 5, 6, 7]
    result2 = Solution.maxSlidingWindow(nums=[1], k=1)  # Expected output: [1]
    result3 = Solution.maxSlidingWindow(nums=[1, -1], k=1)  # Expected output: [1, -1]
    result4 = Solution.maxSlidingWindow(nums=[9, 11], k=2)  # Expected output: [11]
    result5 = Solution.maxSlidingWindow(nums=[4, -2, -8, 5, -2, 7, 7, 2, -6, 5], k=4)  # Expected output: [5, 5, 7, 7, 7]

    # Print the results
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)

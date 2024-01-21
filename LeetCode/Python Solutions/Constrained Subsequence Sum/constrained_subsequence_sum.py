from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n  # Initialize DP table
        dp[0] = nums[0]
        
        # Initialize a deque and add the first element index
        maxDeque = deque([0])

        for i in range(1, n):
            # The front of the deque gives the index of the maximum element for the last k entries
            dp[i] = nums[i] + max(dp[maxDeque[0]], 0)
            
            # Maintain the deque to ensure the elements are in decreasing order
            while maxDeque and dp[i] >= dp[maxDeque[-1]]:
                maxDeque.pop()
                
            maxDeque.append(i)
            
            # Remove elements from the front if they are out of the current window (k size)
            if maxDeque[0] == i - k:
                maxDeque.popleft()
                
        return max(dp)

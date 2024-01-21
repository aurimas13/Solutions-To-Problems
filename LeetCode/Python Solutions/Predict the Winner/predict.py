class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Create a memoization table
        memo = dict()
        
        def dp(i, j):
            # If this subproblem has been solved before, return the result
            if (i, j) in memo:
                return memo[i, j]
                
            # If we are at the end of the array, return the last element
            if i == j:
                return nums[i]
            
            # Calculate the maximum difference the first player can get over the second player
            # Either pick the first element and subtract the result of the rest array
            # Or pick the last element and subtract the result of the rest array
            memo[i, j] = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
            return memo[i, j]
            
        # The first player can win if and only if their score is greater than or equal to the second player's score
        return dp(0, len(nums) - 1) >= 0

from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0 # Initialize the total number of arithmetic subsequences
        dp = [defaultdict(int) for _ in nums] # Create a list of default dictionaries

        for i in range(len(nums)): # Iterate through the list of numbers (nums)
            for j in range(i):  # Iterate over all element before the i-th elemtn using index j
                diff = nums[i] - nums[j] # Calculate the difference between the i-th and j-th elements
                prev_count = dp[j][diff] # Get the count of the subsequences ending at j-th element with the same difference
                dp[i][diff] += prev_count + 1 # Increment the count of the subsequences ending at i-th element with the same difference
                total += prev_count # Add only the count of subseqeunces that are already at least 2 elements long

        return total # Return the total number of valid arithmetic subsequences
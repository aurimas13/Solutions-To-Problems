class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)  # Total number of 1's in the array
        
        if ones == 0:
            return 0
        
        # Double the array to handle circular property
        nums = nums + nums
        
        # Initialize the window
        zeros_in_window = nums[:ones].count(0)
        min_swaps = zeros_in_window
        
        # Slide the window
        for i in range(ones, len(nums)):
            zeros_in_window -= (1 - nums[i - ones])  # Remove the leftmost element
            zeros_in_window += (1 - nums[i])  # Add the new rightmost element
            min_swaps = min(min_swaps, zeros_in_window)
        
        return min_swaps
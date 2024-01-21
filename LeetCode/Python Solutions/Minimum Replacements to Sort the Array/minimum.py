from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # Initialize the operations counter
        operations = 0
        
        # Start with the last number in the list as the boundary.
        # All numbers before this should be less than or equal to this number
        # for the list to be sorted in non-decreasing order.
        current_boundary = nums[-1]

        # Loop through the list in reverse (excluding the last element since it's our boundary).
        # This is because we're ensuring each number is less than or equal to the next number (from right to left).
        for num in reversed(nums[:-1]):
            # Calculate how many times we'd have to split 'num' 
            # to make its parts smaller than the current_boundary.
            # This ensures that the number is reduced to be less than the next number on its right.
            split_count = (num + current_boundary - 1) // current_boundary
            
            # Update the operations needed. Subtracting 1 since a split creates two numbers 
            # but we remove one instance of the original number.
            operations += split_count - 1
            
            # Update the current_boundary. This sets a new upper boundary for the next number.
            current_boundary = num // split_count
            
        return operations

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Keep track of the number of zeros seen
        zeros = 0
        
        # Keep track of the current length of subarray of ones
        curr = 0
        
        # Keep track of the maximum length of subarray of ones
        max_len = 0
        
        # Keep track of the length of subarray just before the last zero
        prev = 0
        
        # Loop through each number in the array
        for num in nums:
            # If the number is 1
            if num == 1:
                # Increment the current length
                curr += 1
            # If the number is 0
            else:
                # Increment the number of zeros seen
                zeros += 1
                # Move the length of subarray just before the last zero
                # to prev, and reset current length
                prev, curr = curr, 0
                
            # Update the maximum length
            max_len = max(max_len, prev + curr)
        
        # If the array has at least one zero, then we can get the maximum
        # length by deleting one element. Otherwise, we should reduce
        # the length by 1 as we have to delete one element
        return max_len if zeros > 0 else max_len - 1

# Time complexity: O(n), where n is the number of elements in the input array.
# Space complexity: O(1), as we are using only a constant amount of space.

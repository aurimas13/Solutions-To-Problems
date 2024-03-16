class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        running_sum = 0
        index_map = {0: -1}  # Initialize with 0 sum at index -1
        
        for i, num in enumerate(nums):
            # Increment or decrement running_sum based on the value of num
            running_sum += 1 if num == 1 else -1
            
            # If this running_sum has been seen before, update max_length
            if running_sum in index_map:
                max_length = max(max_length, i - index_map[running_sum])
            else:
                # Store the first occurrence of this running_sum
                index_map[running_sum] = i
        
        return max_length

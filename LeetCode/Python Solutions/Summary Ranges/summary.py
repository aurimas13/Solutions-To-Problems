from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        # Start is the beginning of the current range
        # result will store the formatted ranges
        start = nums[0]
        result = []
        
        # Iterate through the numbers from index 1 to the end
        for i in range(1, len(nums)):
            # If the current number is not consecutive to the previous number,
            # the current range ends at the previous number
            if nums[i] != nums[i-1] + 1:
                # If the range consists of a single number, 
                # append it as a string
                if start == nums[i-1]:
                    result.append(str(start))
                # Otherwise, append the range in the format "start->end"
                else:
                    result.append(f"{start}->{nums[i-1]}")
                
                # Update start to be the beginning of the next range
                start = nums[i]
        
        # Handle the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
    



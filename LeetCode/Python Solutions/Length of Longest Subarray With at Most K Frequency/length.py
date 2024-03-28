from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        freq = defaultdict(int)
        
        for right in range(len(nums)):
            # Update the frequency of the current right element
            freq[nums[right]] += 1
            
            # If the frequency of the current element exceeds k, shrink the window from the left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]  # Remove the element from freq to keep the map clean
                left += 1
                
            # Calculate the max length of the window after ensuring no frequency is greater than k
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength

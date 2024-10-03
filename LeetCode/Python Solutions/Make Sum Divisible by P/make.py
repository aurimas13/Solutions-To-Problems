class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum % p
        if target == 0:
            return 0
        
        prefix_sum_mod = {0: -1}
        current_sum = 0
        min_length = n
        
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            complement = (current_sum - target) % p
            
            if complement in prefix_sum_mod:
                min_length = min(min_length, i - prefix_sum_mod[complement])
            
            prefix_sum_mod[current_sum] = i
        
        return min_length if min_length < n else -1
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        # Handle edge case: if nums has only one element, all subarrays are special
        if n == 1:
            return [True] * len(queries)
        
        # Precompute parity difference
        parity_diff = [1 if nums[i] % 2 != nums[i + 1] % 2 else 0 for i in range(n - 1)]
        
        # Compute prefix sum for parity_diff
        prefix = [0] * (n - 1)
        prefix[0] = parity_diff[0]
        for i in range(1, len(parity_diff)):
            prefix[i] = prefix[i - 1] + parity_diff[i]
        
        # Answer queries
        result = []
        for fromi, toi in queries:
            if toi == fromi:  # A single element is always special
                result.append(True)
            else:
                total_diff = prefix[toi - 1] - (prefix[fromi - 1] if fromi > 0 else 0)
                result.append(total_diff == (toi - fromi))
        
        return result

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        
        # Count the frequency of each remainder
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Check if the array can be arranged into pairs
        for i in range(k // 2 + 1):
            if i == 0:
                # Remainder 0 should have even count
                if remainder_count[i] % 2 != 0:
                    return False
            elif i == k - i:
                # For k/2 (when k is even), count should be even
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                # For other remainders, count should match with its complement
                if remainder_count[i] != remainder_count[k - i]:
                    return False
        
        return True
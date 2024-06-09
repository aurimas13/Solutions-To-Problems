from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = defaultdict(int)
        remainder_map[0] = 1  # Initial condition: prefix sum of 0 with frequency 1
        
        cumulative_sum = 0
        count = 0
        
        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
            
            if remainder < 0:  # Adjust remainder to be positive
                remainder += k
            
            if remainder in remainder_map:
                count += remainder_map[remainder]
            
            remainder_map[remainder] += 1
        
        return count

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # 7
    print(sol.subarraysDivByK([5], 9))  # 0

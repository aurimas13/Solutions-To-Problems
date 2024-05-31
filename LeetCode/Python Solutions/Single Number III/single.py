from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find a differentiating bit (rightmost set bit)
        differentiating_bit = xor_result & -xor_result
        
        # Step 3: Partition the numbers and XOR within each partition
        num1 = 0
        num2 = 0
        for num in nums:
            if num & differentiating_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# Test cases
sol = Solution()
print(sol.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5]
print(sol.singleNumber([-1, 0]))  # Output: [-1, 0]
print(sol.singleNumber([0, 1]))  # Output: [1, 0]

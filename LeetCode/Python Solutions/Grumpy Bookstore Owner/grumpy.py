from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0
        additional_satisfied = 0
        max_additional_satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
            else:
                additional_satisfied += customers[i]
            
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return total_satisfied + max_additional_satisfied

# Example usage
sol = Solution()
print(sol.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))  # Output: 16
print(sol.maxSatisfied([1], [0], 1))  # Output: 1

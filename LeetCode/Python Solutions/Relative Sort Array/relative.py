from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a frequency counter for arr1
        freq = Counter(arr1)
        
        # Result list
        result = []
        
        # Add elements from arr2 based on their order and frequency
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]
        
        # Collect remaining elements and sort them
        remaining = sorted(freq.elements())
        
        # Add remaining elements to the result
        result.extend(remaining)
        
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])) # Output: [2,2,2,1,4,3,3,9,6,7,19]
    print(sol.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))         # Output: [22,28,8,6,17,44]

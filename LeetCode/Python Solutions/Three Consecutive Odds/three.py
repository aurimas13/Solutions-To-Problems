from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False

# Example usage:
sol = Solution()
print(sol.threeConsecutiveOdds([2, 6, 4, 1]))  # Output: False
print(sol.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Output: True

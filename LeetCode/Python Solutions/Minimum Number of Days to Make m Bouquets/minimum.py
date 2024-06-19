from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        return low

# Example usage:
sol = Solution()
print(sol.minDays([1,10,3,10,2], 3, 1))  # Output: 3
print(sol.minDays([1,10,3,10,2], 3, 2))  # Output: -1
print(sol.minDays([7,7,7,7,12,7,7], 2, 3))  # Output: 12
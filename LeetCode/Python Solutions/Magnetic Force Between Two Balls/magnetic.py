from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions to facilitate binary search
        position.sort()
        
        # Function to check if it's possible to place m balls with at least min_dist between them
        def canPlaceBalls(min_dist):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        # Binary search for the maximum minimum distance
        low, high = 1, position[-1] - position[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result

# Example usage:
sol = Solution()
print(sol.maxDistance([1,2,3,4,7], 3))  # Output: 3
print(sol.maxDistance([5,4,3,2,1,1000000000], 2))  # Output: 999999999

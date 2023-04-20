from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if Koko can eat all bananas within the given hours
        def can_eat(piles: List[int], speed: int, hours: int) -> bool:
            # Calculate the total hours required to eat all bananas at the current speed
            total_hours = sum((pile - 1) // speed + 1 for pile in piles)
            return total_hours <= hours

        # Binary search to find the minimum eating speed
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left

if __name__ == '__main__':
    solution = Solution()

    # Test cases
    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    print("All tests passed!")

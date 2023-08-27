from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        
        n = len(stones)
        if n == 1:
            return True
        if stones[1] != 1:
            return False
        
        last_stone = stones[-1]
        # Memoization
        memo = {}
        
        for stone in stones:
            memo[stone] = set()
        
        memo[0].add(0)
        
        for stone in stones:
            for step in memo[stone]:
                # Check all possible step sizes, i.e., k-1, k, k+1
                for shift in [-1, 0, 1]:
                    if step + shift <= 0:  # Ignore non-positive step sizes
                        continue
                    next_jump = stone + step + shift
                    if next_jump == last_stone:
                        return True
                    if next_jump in memo:
                        memo[next_jump].add(step + shift)
        
        return False

# Example usage:
solution = Solution()
print(solution.canCross([0,1,3,5,6,8,12,17]))  # True
print(solution.canCross([0,1,2,3,4,8,9,11]))  # False

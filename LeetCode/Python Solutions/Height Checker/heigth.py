from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create a sorted version of the heights list
        expected = sorted(heights)
        
        # Count the number of indices where the heights differ from the expected
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
                
        return count

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1, 1, 4, 2, 1, 3]))  # Output: 3
    print(sol.heightChecker([5, 1, 2, 3, 4]))     # Output: 5
    print(sol.heightChecker([1, 2, 3, 4, 5]))     # Output: 0

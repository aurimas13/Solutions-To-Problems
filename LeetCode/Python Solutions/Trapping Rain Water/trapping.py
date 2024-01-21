from typing import List

class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        # Initialize variables
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        volume = 0

        # Iterate through the landscape until the left and right pointers meet
        while left < right:
            # Update left_max if a higher left boundary is found
            if height[left] > left_max:
                left_max = height[left]
            
            # Update right_max if a higher right boundary is found
            if height[right] > right_max:
                right_max = height[right]

            # Calculate trapped water volume based on the current minimum boundary
            if left_max < right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

if __name__ == '__main__':
    # Instantiate the solution class
    instant = Solution()
    # Call the 'trap' method with the input landscape heights
    solve = instant.trap(height=[4, 2, 0, 3, 2, 5])  # height=[4, 2, 0, 3, 2, 5] -> 9
    # Print the result
    print(solve)
    
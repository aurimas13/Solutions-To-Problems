from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        max_time = 0  # Track the maximum time in the current group of same-colored balloons.
        current_time = 0  # Track the total time for the current group.

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                # If the color changes, add the total time of the previous group minus the max time.
                total_time += current_time - max_time
                # Reset the max_time and current_time for the new group.
                max_time = 0
                current_time = 0
            
            # Update the current and max times.
            current_time += neededTime[i]
            max_time = max(max_time, neededTime[i])
        
        # Add the time for the last group of balloons.
        total_time += current_time - max_time
        
        return total_time

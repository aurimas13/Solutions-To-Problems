from typing import List  # Import List from typing module to define the type of input

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0  # Initialize altitude to 0
        max_altitude = 0  # Initialize max_altitude to 0
        
        # Iterate through each gain
        for g in gain:
            altitude += g  # Add gain to current altitude
            max_altitude = max(max_altitude, altitude)  # Update max_altitude if current altitude is greater
        
        # Return the max altitude
        return max_altitude
        

# Sample usage
solution = Solution()
print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Output: 1
print(solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Output: 0

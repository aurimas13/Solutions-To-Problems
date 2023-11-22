class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Calculate the total power of all batteries
        total_power = sum(batteries)
        
        # The lower and upper bounds of our search space
        left, right = 1, total_power // n

        # Binary search for the maximum possible running time
        while left < right:
            # Calculate the middle of the current search space
            time = (left + right + 1) // 2
            
            # Check if the current running time is possible with the given batteries
            if self.check(batteries, n, time):
                # If it is possible, we update the lower bound to the current time
                left = time
            else:
                # If it is not possible, we update the upper bound to the current time minus 1
                right = time - 1
                
        # Return the maximum possible running time
        return left
    
    def check(self, batteries: List[int], n: int, time: int) -> bool:
        # Calculate the total power that can be provided for the given running time
        total_power_for_time = sum(min(battery, time) for battery in batteries)
        
        # Check if the total power is at least the product of the running time and the number of computers
        return total_power_for_time >= time * n


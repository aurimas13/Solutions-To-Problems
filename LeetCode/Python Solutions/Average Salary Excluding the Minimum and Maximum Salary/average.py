from typing import List


class Solution:
    # Define the method 'average' with input type hint List[int] and output type hint float
    def average(self, salary: List[int]) -> float:
        # Initialize max_val, min_val, and total with the first element of the salary list and 0, respectively
        max_val, min_val, total = salary[0], salary[0], 0

        # Calculate the total, max_val, and min_val using a generator expression within the sum function
        total = sum((max_val := max(max_val, num), min_val := min(min_val, num), num)[2] for num in salary)

        # Calculate the average by subtracting max_val and min_val from the total and dividing by (len(salary) - 2)
        return (total - max_val - min_val) / (len(salary) - 2)

    
# Test cases:
if __name__ == "__main__":
    assert Solution().average([4000,3000,1000,2000]) == 2500.00000
    assert Solution().average([1000,2000,3000]) == 2000.00000   
    assert Solution().average([6000,5000,4000,3000,2000,1000]) == 3500.00000

print ("All passed")

# Performance Result:   

#   Runtime: 40 ms, faster than 15.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#   Memory Usage: 16.3 MB, less than 8.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#   Coding Time: 00:00:00:040  
#   Time Complexity: O(n)
#   Space Complexity: O(1)


# Alernative Solution:
# import numpy as np

# class Solution:
#     def average(self, salary: List[int]) -> float:
#         salary_np = np.array(salary)
#         total = np.sum(salary_np)
#         max_val = np.amax(salary_np)
#         min_val = np.amin(salary_np)

#         return (total - max_val - min_val) / (len(salary) - 2)

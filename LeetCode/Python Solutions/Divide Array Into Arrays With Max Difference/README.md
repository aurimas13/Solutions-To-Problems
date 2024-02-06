The problem description of "Divide Array Into Arrays With Max Difference" can be found [here](https://binarysearch.com/problems/Divide-Array-Into-Arrays-With-Max-Difference) while the solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Python%20Solutions/Divide%20Array%20Into%20Arrays%20With%20Max%20Difference/divide.py).

## Implementation

The solution efficiently solve the problem of dividing an array into subarrays of size 3, where the difference between any two elements in each subarray is less than or equal to k. The key steps involve sorting the array and iterating through it to form subarrays of three consecutive elements, checking if they satisfy the given condition. If any group does not meet the condition, the function returns an empty array. This approach ensures that the solution is as efficient as possible given the problem constraints, with a primary time complexity factor being the sort operation.
from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # Initialize a stack to store the cars
        stack = []

        # Initialize the result list with -1.0 for each car
        result = [-1.0] * len(cars)

        # Iterate through the cars from the end to the beginning
        for i in range(len(cars) - 1, -1, -1):
            # Check if the current car is faster than the cars in the stack
            while stack and (cars[i][1] <= cars[stack[-1]][1] or
                             (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1]) >= result[stack[-1]] > 0):
                stack.pop()

            # Calculate the collision time for the current car and the next car in the stack
            if stack:
                result[i] = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])

            # Add the current car to the stack
            stack.append(i)

        return result

# Test cases to run in the terminal/console
if __name__ == "__main__":
    s = Solution()

    assert s.getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]) == [1.00000, -1.00000, 3.00000, -1.00000]
    assert s.getCollisionTimes([[3, 4], [5, 4], [6, 3], [9, 1]]) == [2.00000, 1.00000, 1.50000, -1.00000]
    assert s.getCollisionTimes([[1, 1], [2, 1], [3, 1], [4, 1]]) == [-1.00000, -1.00000, -1.00000, -1.00000]

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Initialize a stack to keep track of visible people
        stack = []

        # Initialize the result list with zeros
        result = [0] * len(heights)

        # Iterate through the heights list in reverse
        for i in reversed(range(len(heights))):
            # Pop elements from the stack until a taller person is found
            while stack and heights[stack[-1]] <= heights[i]:
                result[i] += 1
                stack.pop()

            # Add the taller person to the result count
            if stack:
                result[i] += 1

            # Append the current index to the stack
            stack.append(i)

        return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    heights = [10, 6, 8, 5, 11, 9]
    print(sol.canSeePersonsCount(heights))  # Output: [3, 1, 2, 1, 1, 0]

    heights = [5, 1, 2, 3, 10]
    print(sol.canSeePersonsCount(heights))  # Output: [4, 1, 1, 1, 0]

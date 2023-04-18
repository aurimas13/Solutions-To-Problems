from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Initialize an empty list to store the combinations
        result = []

        # Define a recursive function to generate combinations
        def backtrack(start, current_combination):
            # If the current combination is of the required length, add it to the result
            if len(current_combination) == k:
                result.append(current_combination[:])
                return

            # Iterate through the remaining numbers and generate combinations
            for i in range(start, n + 1):
                # Add the current number to the combination
                current_combination.append(i)
                # Recursively generate combinations with the remaining numbers
                backtrack(i + 1, current_combination)
                # Remove the last added number to explore other possibilities
                current_combination.pop()

        # Call the recursive function to generate combinations starting from 1
        backtrack(1, [])

        return result


# Test cases
solution = Solution()

# Test case 1
assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Test case 2
assert solution.combine(1, 1) == [[1]]

# Test case 3
assert solution.combine(4, 4) == [[1, 2, 3, 4]]

print("All test cases passed!")

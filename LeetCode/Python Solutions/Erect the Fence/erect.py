from typing import List, Tuple


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Define the orientation function to calculate the cross product of the difference of points
        def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        # Sort the trees by their coordinates
        trees.sort(key=lambda tree: (tree[0], tree[1]))

        # Initialize two lists to store the lower and upper hulls
        lower_hull, upper_hull = [], []

        # Iterate through the sorted trees
        for tree in trees:
            # Calculate the lower hull
            # Check the orientation of the last two points in the lower hull and the current tree
            # If the orientation is positive (clockwise), pop the last point from the lower hull
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], tuple(tree)) > 0:
                lower_hull.pop()
            # Append the current tree as a tuple to the lower hull
            lower_hull.append(tuple(tree))

            # Calculate the upper hull
            # Check the orientation of the last two points in the upper hull and the current tree
            # If the orientation is negative (counterclockwise), pop the last point from the upper hull
            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], tuple(tree)) < 0:
                upper_hull.pop()
            # Append the current tree as a tuple to the upper hull
            upper_hull.append(tuple(tree))

        # Combine the lower and upper hulls, remove duplicates using set, and convert the tuples back to lists
        return list(set(lower_hull + upper_hull))

# Test function to test the solution
def main():
    solution = Solution()

    test_cases = [
        ([
            [1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]], 
            [[1, 1], [2, 0], [2, 4], [4, 2]]),
        ([
            [1, 2], [2, 2], [4, 2]], [
            [1, 2], [2, 2], [4, 2]])
    ]
    for trees, expected_output in test_cases:
        result = solution.outerTrees(trees)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

print("All test cases passed!")   


# Checking in terminal/console::
if __name__ == "main":
    main()

from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        trees.sort(key=lambda tree: (tree[0], tree[1]))

        lower_hull, upper_hull = [], []

        for tree in trees:
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], tuple(tree)) > 0:
                lower_hull.pop()
            lower_hull.append(tuple(tree))

            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], tuple(tree)) < 0:
                upper_hull.pop()
            upper_hull.append(tuple(tree))

        return list(set(lower_hull + upper_hull))


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

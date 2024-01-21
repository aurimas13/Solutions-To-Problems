from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Initialize a stack and a lower bound variable
        stack = []
        lower_bound = float('-inf')

        # Iterate through the preorder list
        for num in preorder:
            # If the current number is less than the lower bound, return False
            if num < lower_bound:
                return False

            # Pop elements from the stack while the top is less than the current number
            while stack and stack[-1] < num:
                # Update the lower bound to the popped element
                lower_bound = stack.pop()

            # Push the current number onto the stack
            stack.append(num)

        # If the loop completes, the preorder sequence is valid
        return True


def test_solution():
    s = Solution()

    assert s.verifyPreorder([5, 2, 1, 3, 6]) == True
    assert s.verifyPreorder([5, 2, 6, 1, 3]) == False
    assert s.verifyPreorder([1, 3, 4]) == True
    assert s.verifyPreorder([4, 2, 1, 3, 6, 5, 7]) == True
    assert s.verifyPreorder([4, 6, 5, 7, 2, 1, 3]) == False


if __name__ == '__main__':
    test_solution()

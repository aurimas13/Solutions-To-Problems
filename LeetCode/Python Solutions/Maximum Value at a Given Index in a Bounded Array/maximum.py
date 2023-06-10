class Solution:
def maxValue(self, n: int, index: int, maxSum: int) -> int:
    """
    Calculate the maximum value that can be placed at a certain index
    with a given sum and number of elements.

    Args:
    - n: number of elements
    - index: position to place the value
    - maxSum: maximum sum allowed

    Returns:
    - maxVal: maximum value that can be placed at the given index
    """
    maxSum -= n  # subtract n from maxSum to account for the initial values at each index
    left = 0
    right = maxSum

    while left < right:
        # calculate the midpoint
        mid = (left + right + 1) // 2  # In Python, // is used for integer division

        # if the sum of values to the left and right of the midpoint is less than or equal to maxSum
        # update left to mid
        if self.test(n, index, mid) <= maxSum:
            left = mid
        # otherwise, update right to mid - 1
        else:
            right = mid - 1

    maxVal = left + 1  # add 1 to account for the initial value at the given index
    return maxVal

def test(self, n: int, index: int, a: int) -> int:
    """
    Calculates the sum of the values of a sequence of integers
    based on the given parameters and returns the result.

    Args:
        n (int): The length of the sequence
        index (int): The index of the integer `a` in the sequence
        a (int): The integer value at the given index in the sequence

    Returns:
        int: The sum of the values of the sequence, excluding the value at the given index
    """

    # Calculate the sum of the integers to the left of the given index
    left_sum = (a + max(a - index, 0)) * (a - max(a - index, 0) + 1) // 2

    # Calculate the sum of the integers to the right of the given index
    right_sum = (a + max(a - ((n - 1) - index), 0)) * (a - max(a - ((n - 1) - index), 0) + 1) // 2

    # Return the sum of the left and right sides of the sequence, excluding the value at the given index
    return left_sum + right_sum - a

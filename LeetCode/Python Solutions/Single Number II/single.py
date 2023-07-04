class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Calculate the single number in the given list.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: The single number in the list.
        """
        once = twice = 0
        for num in nums:
            once = (once ^ num) & ~twice
            twice = (twice ^ num) & ~once
        return once


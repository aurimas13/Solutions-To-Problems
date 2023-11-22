class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        # Stack for possible "2"s.
        stack = []

        # Third number in the 132 sequence.
        third = float('-inf')

        # Traverse from right to left.
        for num in reversed(nums):

            # If the current number is less than the third number, return True.
            if num < third:
                return True

            # While there are elements in the stack and they are less than the current number.
            while stack and stack[-1] < num:
                third = stack.pop()

            # Push the current number onto the stack.
            stack.append(num)

        # If we couldn't find any 132 pattern, return False.
        return False

class Solution:
    def minOperations(self, s: str) -> int:
        # Initialize counters for differences from the two patterns.
        diff1, diff2 = 0, 0

        for i, char in enumerate(s):
            if i % 2 == 0:
                # Even index: should be '0' for the first pattern and '1' for the second.
                if char == '0':
                    diff2 += 1
                else:
                    diff1 += 1
            else:
                # Odd index: should be '1' for the first pattern and '0' for the second.
                if char == '1':
                    diff2 += 1
                else:
                    diff1 += 1

        # Return the minimum number of operations needed.
        return min(diff1, diff2)

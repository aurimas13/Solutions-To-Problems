from collections import Counter
from itertools import permutations

class Solution:
    def largestVariance(self, input_str: str) -> int:
        # Initialize the maximum difference (variance) as zero
        # 'Counter' returns a dictionary where keys are elements of the input list and values are the count of the elements
        max_diff, char_counter = 0, Counter(input_str)

        # 'set' returns unique characters in the string, 'permutations' gives all possible arrangements of two characters
        # Iterate through each permutation
        for char_1, char_2 in permutations(set(input_str), 2):
            # If count of char_1 in the string is 1, skip this case as we need the count of char_1 to be greater than or equal to char_2 for a positive variance
            if char_counter[char_1]==1:
                continue   
            
            # Initialize temporary variables for the substring count and the difference
            substr_count, diff = 0, -len(input_str)

            # Iterate through each character in the string
            for char in input_str:
                if char==char_1:
                    # If the character matches char_1, increment substring count and difference
                    substr_count += 1
                    diff += 1
                elif char==char_2:
                    # If the character matches char_2, decrement substring count and update difference
                    substr_count -= 1
                    diff = substr_count
                    # If substring count is negative, reset it to zero
                    if substr_count<0: 
                        substr_count = 0
                # If current difference is greater than the maximum difference, update the maximum difference
                if max_diff < diff:
                    max_diff = diff
        # Return the maximum difference (variance)
        return max_diff


from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count the frequency of characters in the input string
        char_count = Counter(s)

        # Initialize a dictionary to store the count of digits
        digits_count = {}

        # Count each unique digit using the unique character present in the English word for that digit
        digits_count['0'] = char_count['z']  # 'z' is unique to "zero"
        digits_count['2'] = char_count['w']  # 'w' is unique to "two"
        digits_count['4'] = char_count['u']  # 'u' is unique to "four"
        digits_count['6'] = char_count['x']  # 'x' is unique to "six"
        digits_count['8'] = char_count['g']  # 'g' is unique to "eight"

        digits_count['1'] = char_count['o'] - digits_count['0'] - digits_count['2'] - digits_count['4']
        digits_count['3'] = char_count['t'] - digits_count['2'] - digits_count['8']
        digits_count['5'] = char_count['f'] - digits_count['4']
        digits_count['7'] = char_count['s'] - digits_count['6']
        digits_count['9'] = char_count['i'] - digits_count['5'] - digits_count['6'] - digits_count['8']

        # Sort the digits and reconstruct the original digits string
        result = ''.join(digit * count for digit, count in sorted(digits_count.items()))

        return result

if __name__ == '__main__':
    # Initialize the solution object
    solution = Solution()

    # Test cases
    test1 = "owoztneoer"
    test2 = "fviefuro"
    test3 = "niesevehrtfeev"

    # Test the solution and print the results
    print(solution.originalDigits(test1))  # Expected output: '012'
    print(solution.originalDigits(test2))  # Expected output: '45'
    print(solution.originalDigits(test3))  # Expected output: '35679'

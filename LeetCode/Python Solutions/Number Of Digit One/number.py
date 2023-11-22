class Solution:
    def countDigitOne(self, n: int) -> int:
        # Initialize the count of digit one
        count = 0
        
        # Initialize the multiplier to track different positions of the number
        multiplier = 1
        
        # Iterate while the number is greater than zero
        while n >= multiplier:
            # Calculate the count of ones in the current position and add it to the total count
            count += (n // (multiplier * 10)) * multiplier + min(max(n % (multiplier * 10) - multiplier + 1, 0), multiplier)
            
            # Move to the next higher position (tens, hundreds, etc.)
            multiplier *= 10
        
        # Return the total count of digit one
        return count


if __name__ == '__main__':
    solution = Solution()

    test_cases = [
        (13, 6),
        (0, 0),
        (100, 21),
        (1234, 689)
    ]

    for n, expected in test_cases:
        result = solution.countDigitOne(n)
        assert result == expected, f"For {n}, expected {expected} but got {result}"

    print("All tests passed!")

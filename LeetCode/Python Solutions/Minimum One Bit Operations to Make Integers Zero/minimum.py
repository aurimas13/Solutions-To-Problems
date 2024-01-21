class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Initialize the result to 0
        result = 0
        
        # Iterate while n is greater than 0
        while n > 0:
            # Update the result with XOR operation between the result and n
            result ^= n
            # Right shift n by 1 bit
            n >>= 1
        
        return result


# Test cases to try in the terminal/console
if __name__ == "__main__":
    solution = Solution()

    test1 = 0
    test2 = 3
    test3 = 9
    test4 = 333

    print(solution.minimumOneBitOperations(test1))  # Expected output: 0
    print(solution.minimumOneBitOperations(test2))  # Expected output: 2
    print(solution.minimumOneBitOperations(test3))  # Expected output: 14
    print(solution.minimumOneBitOperations(test4))  # Expected output: 392


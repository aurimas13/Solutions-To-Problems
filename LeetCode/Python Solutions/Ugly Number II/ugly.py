class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize ugly numbers list with the first ugly number (1)
        ugly_numbers = [1]
        
        # Initialize indices for 2, 3, and 5
        i2, i3, i5 = 0, 0, 0
        
        # Loop until we find the n-th ugly number
        while len(ugly_numbers) < n:
            # Calculate the next ugly numbers by multiplying current indices with 2, 3, and 5
            next_ugly_2, next_ugly_3, next_ugly_5 = ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5
            
            # Find the minimum of the next ugly numbers
            next_ugly = min((next_ugly_2, next_ugly_3, next_ugly_5))
            
            # Add the next ugly number to the list
            ugly_numbers.append(next_ugly)
            
            # Increment indices based on which number was added
            i2 += next_ugly == next_ugly_2
            i3 += next_ugly == next_ugly_3
            i5 += next_ugly == next_ugly_5
        
        # Return the n-th ugly number
        return ugly_numbers[-1]

# Tests to run in the terminal/console
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n1 = 10
    assert solution.nthUglyNumber(n1) == 12, f"Expected 12, but got {solution.nthUglyNumber(n1)}"
    
    # Test case 2
    n2 = 1
    assert solution.nthUglyNumber(n2) == 1, f"Expected 1, but got {solution.nthUglyNumber(n2)}"
    
    # Test case 3
    n3 = 4
    assert solution.nthUglyNumber(n3) == 4, f"Expected 4, but got {solution.nthUglyNumber(n3)}"

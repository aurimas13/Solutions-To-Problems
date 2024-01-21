class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize the shift count
        shift = 0
        
        # We shift both numbers to the right until they become equal
        # This gives us the common prefix in the binary representation
        while left != right:
            left >>= 1  # Right shift left by 1 bit
            right >>= 1  # Right shift right by 1 bit
            shift += 1  # Increment the shift count

        # Shift the common prefix to the left by the number of remaining bits
        # This is equivalent to appending the remaining bits as zeroes at the end
        return left << shift

# Test Cases:
if __name__ == "__main__":
    assert Solution().rangeBitwiseAnd(5, 7) == 4
    assert Solution().rangeBitwiseAnd(0, 0) == 0
    assert Solution().rangeBitwiseAnd(1, 2147483647) == 0
    print("All passed")
    
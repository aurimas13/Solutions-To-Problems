class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string into the numeric form
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Perform the digit sum transformation k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        # Convert the final result back to integer
        return int(num_str)

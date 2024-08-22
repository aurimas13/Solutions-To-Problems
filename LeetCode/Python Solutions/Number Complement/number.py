class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits in num
        if num == 0:
            return 1
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        
        # XOR with all 1's will flip all bits
        return num ^ mask
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        return bin(xor).count('1')
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1

        for c in reversed(s):
            if c.isdigit():
                length //= int(c)
                k %= length
            else:
                if k == 0 or k == length:
                    return c
                length -= 1
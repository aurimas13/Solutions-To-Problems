# Solution implementing dynamic programming
class Solution:
    @staticmethod
    def numSplits(s: str) -> int:
        n = len(s)
        left = [0] * n
        right = [0] * n
        left_count = {}
        right_count = {}
        for i in range(n):
            c = s[i]
            left_count[c] = left_count.get(c, 0) + 1
            left[i] = len(left_count)
        for i in range(n-1, -1, -1):
            c = s[i]
            right_count[c] = right_count.get(c, 0) + 1
            right[i] = len(right_count)
        result = 0
        for i in range(1, n):
            if left[i-1] == right[i]:
                result += 1
        return result



# Checking in console/PyCharm
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numSplits(s = "aacaba")
    # s = "aacaba" -> 2
    # s = "abcd" -> 1
    print(Solve)

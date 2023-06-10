class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left = 0
        right = maxSum

        while left < right:
            mid = (left + right + 1) // 2  # In Python, // is used for integer division
            if self.test(n, index, mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1

    def test(self, n, index, a):
        b = max(a - index, 0)
        res = (a + b) * (a - b + 1) // 2  # In Python, // is used for integer division
        b = max(a - ((n - 1) - index), 0)
        res += (a + b) * (a - b + 1) // 2  # In Python, // is used for integer division
        return res - a

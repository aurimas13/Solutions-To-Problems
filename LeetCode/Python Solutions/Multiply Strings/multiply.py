class Solution:
    @staticmethod
    def strToInt(num: str) -> int:
        multiplier = 1
        ans = 0
        for each in reversed(num):
            ans += multiplier * (ord(each) - ord('0'))
            multiplier *= 10
        return ans

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strToInt(num1) * self.strToInt(num2))


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.multiply(num1="123", num2="456")  # num1="123", num2="456" -> "56088"
    print(Solve)

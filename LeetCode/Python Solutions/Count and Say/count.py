class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def sayNumber(n):
            n = str(n)
            say = ""
            curDigit = n[0]
            digCount = 1
            for dig in n[1:]:
                if dig == curDigit:
                    digCount += 1
                else:
                    say += str(digCount) + curDigit
                    curDigit = dig
                    digCount = 1
            say += str(digCount) + curDigit
            return say

        return sayNumber(self.countAndSay(n - 1))


# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countAndSay(4)  #  n = 4 -> 1211 | n = 1 -> 1
    print(Solve)

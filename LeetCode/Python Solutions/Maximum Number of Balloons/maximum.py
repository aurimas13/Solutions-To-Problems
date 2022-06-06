import math
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bCount, aCount, lCount, oCount, nCount = 0, 0, 0, 0, 0

        for i in range(len(text)):
            if text[i] == 'b':
                bCount += 1
            elif text[i] == 'a':
                aCount+= 1
            elif text[i] == 'l':
                lCount+= 1
            elif text[i] == 'o':
                oCount+= 1
            elif text[i] == 'n':
                nCount+= 1

        lCount = lCount / 2;
        oCount = oCount / 2;

        return math.floor(min(bCount, aCount, lCount, oCount, nCount))

# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxNumberOfBalloons('balon')  # nlaebolko -> 1 | loonbalxballpoon -> 2
    print(Solve)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ''
        last={c:i for i,c in enumerate(s)}
        pos=0
        for i in range(len(s)):
            if s[i]<s[pos]:
                pos=i
            if i==last[s[i]]: break

        return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos],''))


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeDuplicateLetters(s = "cbacdcbc")  # s = "cbacdcbc" -> "acdb"
    print(Solve)
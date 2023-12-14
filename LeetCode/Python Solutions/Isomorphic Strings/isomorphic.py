class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        l={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if c1 not in l:
                if c2 in l.values():
                    return False
                l[c1]=c2
            elif l[c1]!=c2:
                return False
        return True


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isIsomorphic(s = "egg", t = "add")
    # s = "egg", t = "add" -> true
    # s = "foo", t = "bar" -> false
    print(Solve)

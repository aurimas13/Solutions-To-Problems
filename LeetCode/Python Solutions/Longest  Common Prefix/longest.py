from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if len(strs)==0: return prefix

        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix

# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.longestCommonPrefix(["flower","flow","flight"])  # ["flower","flow","flight"] -> "fl"
    print(Solve)
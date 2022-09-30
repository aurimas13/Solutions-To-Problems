class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s1 = dict([(j,i) for i,j in enumerate(S)])
        T = list(T)
        T.sort(key =lambda x:s1[x] if x in s1.keys() else float('inf'))
        return ''.join(T)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.customSortString("cbafg", "abcd")  # "cbafg", "abcd" -> "cbad" | "cba", "abcd" -> "cbad"
    print(Solve)
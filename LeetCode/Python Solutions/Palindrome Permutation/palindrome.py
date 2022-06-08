import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return [curr_count % 2 != 0 for curr_count in collections.Counter(s).values()].count(True) < 2


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.canPermutePalindrome('code')  # 'code' -> false, 'aab' -> True
    print(Solve)

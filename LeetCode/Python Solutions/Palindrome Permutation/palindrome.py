import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return [curr_count % 2 != 0 for curr_count in collections.Counter(s).values()].count(True) < 2
class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        return len(set(zip(pattern, s))) == len(set(s)) and len(set(s)) == len(set(pattern))

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.wordPattern( pattern = "abba", s = "dog cat cat fish")
    #  pattern = "abba", s = "dog cat cat fish" -> false
    #  pattern = "abba", s = "dog cat cat dog" -> true
    print(Solve)

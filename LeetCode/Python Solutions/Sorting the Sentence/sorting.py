class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([c[:-1] for c in sorted(s.split(), key=lambda x: x[-1])])

# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.sortSentence("is2 sentence4 This1 a3")  # "is2 sentence4 This1 a3" -> "This is a sentence" | "Myself2 Me1 I4 and3" -> "Me Myself and I"
    print(Solve)
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfString("hello"))  # Output: 13
    print(sol.scoreOfString("zaz"))    # Output: 50

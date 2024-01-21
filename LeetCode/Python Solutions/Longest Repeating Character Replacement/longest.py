from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Calculate the longer repeating character
        string when replacing with one letter
        Args:
            s (str): String to evaluate
            k (int): Number of characters to replace
        Returns:
            int: Length of longest repeating sequence
        """
        behind, ahead = 0, 0
        char_count = defaultdict(int)
        char_count[s[ahead]] += 1
        max_length = 0

        while ahead < len(s):
            length = ahead - behind + 1
            max_freq = max(char_count.values())
            if length - max_freq <= k:
                max_length = max(length, max_length)
                ahead += 1
                if ahead == len(s):
                    break
                char_count[s[ahead]] += 1
            else:
                char_count[s[behind]] -= 1
                behind += 1

        return max_length


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.characterReplacement(s = "ABAB", k = 2 )  # s = "ABAB", k = 2 -> 4
    print(Solve)
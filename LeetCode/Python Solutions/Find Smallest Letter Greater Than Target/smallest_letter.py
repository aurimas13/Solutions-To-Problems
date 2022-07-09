from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        n = len(letters)
        lo, hi = 0, n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            # what we want is on the right side, not in [0...mid]
            if letters[mid] <= target:
                lo = mid + 1
            # mid might or might not be the smallest but it's the right way. Let reduce the searching space to [0...mid]
            else:
                hi = mid

        return letters[hi]


# Check in the PyCharm/terminal:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.nextGreatestLetter(["c","f","j"])  # letters = ["c","f","j"], target = "a" -> "c"" | letters = ["c","f","j"], target = "d" -> "f"
    print(Solve)

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # If there are no three consecutive 'A's or 'B's, Bob wins by default
        if "AAA" not in colors and "BBB" not in colors:
            return False

        aMoves = 0
        bMoves = 0

        i = 0
        n = len(colors)

        while i < n:
            j = i
            # Count consecutive 'A's
            while j < n and colors[j] == 'A':
                j += 1
            aMoves += max(0, j - i - 2)
            i = j
         

            # Count consecutive 'B's
            while j < n and colors[j] == 'B':
                j += 1
            bMoves += max(0, j - i - 2)
            i = j

        return aMoves > bMoves




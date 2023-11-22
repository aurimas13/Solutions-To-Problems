from functools import lru_cache
import math

class Solution:
    @lru_cache(None)
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        if n == 0 or n <= k:
            return 0  # If there are no songs or the number of songs is less than or equal to k, return 0
        if n == 1:
            return 1  # If there is only one song, return 1
        M = 10**9 + 7  # Modulus to prevent overflow
        
        # Calculate all the combinations, including those that do not include every song
        for i in range(goal):
            if i == 0:
                result = n  # If i is 0, result is n
            else:
                if i <= k:
                    result *= (n-i)  # If i is less than or equal to k, multiply result by (n-i)
                else:
                    result *= (n-k)  # If i is greater than k, multiply result by (n-k)

        # So far the result contains all the combinations where 1 or more songs are never played, therefore we need to
        # remove those combinations
        for j in range(1, n - k):
            # j represents the number of songs that are never played.
            result -= (math.comb(n, j) * self.numMusicPlaylists(n-j, goal, k))  # Subtract the combinations where j songs are never played

        return result % M  # Return the result modulo M to prevent overflow

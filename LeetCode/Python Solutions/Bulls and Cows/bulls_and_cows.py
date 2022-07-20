from collections import Counter, defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, count, n = 0, 0, Counter(secret), len(secret)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                count[guess[i]] -= 1
                if count[guess[i]] < 0:
                    cows -= 1
            elif guess[i] in count and count[guess[i]] > 0:
                cows += 1
                count[guess[i]] -= 1
        return f"{bulls}A{cows}B"


# # OR
#
#     def getHint(self, secret: str, guess: str) -> str:
#         h = Counter(secret)
#
#         bulls = cows = 0
#         for idx, ch in enumerate(guess):
#             if ch in h:
#                 # corresponding characters match
#                 if ch == secret[idx]:
#                     # update the bulls
#                     bulls += 1
#                     # update the cows
#                     # if all ch characters from secret
#                     # were used up
#                     cows -= int(h[ch] <= 0)
#                 # corresponding characters don't match
#                 else:
#                     # update the cows
#                     cows += int(h[ch] > 0)
#                 # ch character was used
#                 h[ch] -= 1
#
#         return "{}A{}B".format(bulls, cows)
#
#
# # OR
#
#     def getHint(self, secret: str, guess: str) -> str:
#         h = defaultdict(int)
#         bulls = cows = 0
#
#         for idx, s in enumerate(secret):
#             g = guess[idx]
#             if s == g:
#                 bulls += 1
#             else:
#                 cows += int(h[s] < 0) + int(h[g] > 0)
#                 h[s] += 1
#                 h[g] -= 1
#
#         return "{}A{}B".format(bulls, cows)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.getHint(secret = "1807", guess = "7810")  # secret = "1807", guess = "7810" -> "1A3B" | secret = "1123", guess = "0111" -> "1A1B"
    print(Solve)

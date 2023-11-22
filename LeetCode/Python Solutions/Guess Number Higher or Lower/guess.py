class Solution:
    def guessNumber(self, n: int) -> int:
            low = 0
            high = n

            while low <= high:
                mid = (low + high) // 2
                if guess(mid) == 0 :
                    return int(mid)
                elif guess(mid) == -1:
                    high = mid
                else:
                    low = mid + 1
            return None


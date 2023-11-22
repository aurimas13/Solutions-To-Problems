class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7  # modulo constant
        # Initialize dp list with 1 for 0 index and 0 for rest of the indices
        dp = [1 if i == 0 else 0 for i in range(high + 1)]
        total = 0  # keep track of the total number of good strings

        # Iterate over the range from 1 to high (inclusive)
        for i in range(1, high + 1):
            # If we can append '0' to a shorter string
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            # If we can append '1' to a shorter string
            if i - one >= 0:
                dp[i] += dp[i - one]
            # If the current length is within the range [low, high]
            if low <= i <= high:
                total += dp[i]  # add the count of good strings of current length to total

        return total % mod  # return the total modulo 10^9 + 7


# Tests
if __name__ == "__main__":

    assert Solution().countGoodStrings(3, 3, 1, 1) == 8
    assert Solution().countGoodStrings(2, 3, 1, 2) == 5
    print("All tests passed")
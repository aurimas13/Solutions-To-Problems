class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}  # This dictionary is used to memoize results of subproblems

        def dp(i, j):
            # This is the recursive function that calculates the optimal solution
            if i > j:  # If the start of the substring is after its end, it's an empty substring
                return 0  # The printer needs 0 turns to print an empty substring
            if (i, j) not in memo:  # If this subproblem has not been solved before
                ans = dp(i+1, j) + 1  # The printer will need at least one more turn than the optimal solution for the substring that doesn't include the first character
                for k in range(i+1, j+1):  # For every possible ending of the substring
                    if s[k] == s[i]:  # If the character at the ending is the same as the character at the beginning
                        # It might be better to print them together
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))  # The printer will need the minimum number of turns between the current best and the new option
                memo[i, j] = ans  # The result is stored in the dictionary
            return memo[i, j]  # The result is returned

        return dp(0, len(s)-1)  # The function is called with the full string

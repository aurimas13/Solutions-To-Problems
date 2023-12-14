class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7

        # We sort the array so that whenever we pick a number, 
        # all possible factors for it are already processed.
        arr.sort()

        # This dictionary holds the number of trees with 'key' as root.
        dp = {num: 1 for num in arr}  # A single node is a valid tree.

        # For each number, we check if it can be the root of a new tree.
        for i, num in enumerate(arr):
            for j in range(i):
                # If the number can be obtained by multiplying two numbers in the array
                if num % arr[j] == 0:
                    right = num // arr[j]
                    # If both parts are in the dictionary, it's a valid combination.
                    if right in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right]) % MOD

        return sum(dp.values()) % MOD

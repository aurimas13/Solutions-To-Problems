from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1  # If there are less trust relationships than n-1, a judge can't exist

        # Initialize trust counts
        trust_counts = [0] * (n + 1)

        # Calculate trust counts
        for a, b in trust:
            trust_counts[a] -= 1  # Person a trusts someone, decrease their count
            trust_counts[b] += 1  # Person b is trusted by someone, increase their count

        # Find the town judge
        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:
                return i  # The judge is found

        return -1  # No judge found



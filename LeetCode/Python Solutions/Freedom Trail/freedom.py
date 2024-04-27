from collections import defaultdict
import sys

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        pos = defaultdict(list)
        
        # Collect positions for each character in the ring
        for i, char in enumerate(ring):
            pos[char].append(i)
        
        # dp[i][j]: minimum steps to process up to i-th character in key, ending with j-th character in ring
        dp = [[sys.maxsize] * n for _ in range(m + 1)]
        dp[0][0] = 0  # Start at position 0 in ring
        
        for i in range(1, m + 1):
            for curPos in pos[key[i - 1]]:
                for k in range(n):
                    if dp[i - 1][k] != sys.maxsize:
                        dist = min(abs(curPos - k), n - abs(curPos - k))
                        dp[i][curPos] = min(dp[i][curPos], dp[i - 1][k] + dist + 1)
        
        # Find the minimal steps to complete the last character in key
        min_steps = min(dp[m])
        
        return min_steps

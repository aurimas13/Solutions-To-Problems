class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)  # Reduce k to be within one full cycle
        
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        
        return 0  # This line should never be reached
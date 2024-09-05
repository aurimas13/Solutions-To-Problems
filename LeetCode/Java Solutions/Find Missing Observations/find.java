class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        known_sum = sum(rolls)
        missing_sum = total_sum - known_sum
        
        if missing_sum < n or missing_sum > 6*n:
            return []
        
        quotient, remainder = divmod(missing_sum, n)
        
        return [quotient + 1] * remainder + [quotient] * (n - remainder)
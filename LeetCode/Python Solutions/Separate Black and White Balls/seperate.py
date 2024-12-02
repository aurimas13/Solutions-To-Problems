class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        black_count = 0
        
        for ball in s:
            if ball == '1':
                black_count += 1
            else:
                steps += black_count
        
        return steps
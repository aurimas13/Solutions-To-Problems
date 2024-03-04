class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Sort tokens to play smallest or largest
        score = 0
        maxScore = 0
        left, right = 0, len(tokens) - 1
        
        while left <= right:
            if power >= tokens[left]:  # Play the smallest face-up
                power -= tokens[left]
                score += 1
                maxScore = max(maxScore, score)
                left += 1
            elif score > 0:  # Play the largest face-down if beneficial
                power += tokens[right]
                score -= 1
                right -= 1
            else:  # Cannot play anymore
                break
        
        return maxScore

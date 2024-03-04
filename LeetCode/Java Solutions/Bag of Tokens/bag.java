class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);  // Sort tokens to play smallest or largest
        int score = 0, maxScore = 0;
        int left = 0, right = tokens.length - 1;
        
        while (left <= right) {
            if (power >= tokens[left]) {  // Play the smallest face-up
                power -= tokens[left++];
                maxScore = Math.max(maxScore, ++score);
            } else if (score > 0) {  // Play the largest face-down if beneficial
                power += tokens[right--];
                score--;
            } else {  // Cannot play anymore
                break;
            }
        }
        
        return maxScore;
    }
}

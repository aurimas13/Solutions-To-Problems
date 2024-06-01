class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        for (int i = 1; i < s.length(); i++) {
            score += Math.abs(s.charAt(i) - s.charAt(i - 1));
        }
        return score;
    }

    // Example Usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.scoreOfString("hello"));  // Output: 13
        System.out.println(sol.scoreOfString("zaz"));    // Output: 50
    }
}

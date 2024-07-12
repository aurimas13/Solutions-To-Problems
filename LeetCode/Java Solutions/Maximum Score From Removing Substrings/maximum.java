class Solution {
    public int maximumGain(String s, int x, int y) {
        StringBuilder sb;
        int score1, score2;
        
        if (x > y) {
            sb = new StringBuilder();
            score1 = removeSubstring(s, 'a', 'b', x, sb);
            score2 = removeSubstring(sb.toString(), 'b', 'a', y, new StringBuilder());
        } else {
            sb = new StringBuilder();
            score1 = removeSubstring(s, 'b', 'a', y, sb);
            score2 = removeSubstring(sb.toString(), 'a', 'b', x, new StringBuilder());
        }
        
        return score1 + score2;
    }
    
    private int removeSubstring(String s, char first, char second, int points, StringBuilder sb) {
        int score = 0;
        for (char c : s.toCharArray()) {
            if (c == second && sb.length() > 0 && sb.charAt(sb.length() - 1) == first) {
                sb.deleteCharAt(sb.length() - 1);
                score += points;
            } else {
                sb.append(c);
            }
        }
        return score;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maximumGain("cdbcbbaaabab", 4, 5));  // Output: 19
        System.out.println(sol.maximumGain("aabbaaxybbaabb", 5, 4));  // Output: 20
    }
}

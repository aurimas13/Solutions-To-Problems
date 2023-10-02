public class Solution {

    public boolean winnerOfGame(String colors) {
        // If there are no three consecutive 'A's or 'B's, Bob wins by default
        if (!colors.contains("AAA") && !colors.contains("BBB")) {
            return false;
        }

        int aMoves = 0;
        int bMoves = 0;

        int i = 0;
        int n = colors.length();

        while (i < n) {
            int j = i;

            // Count consecutive 'A's
            while (j < n && colors.charAt(j) == 'A') {
                j++;
            }
            aMoves += Math.max(0, j - i - 2);
            i = j;

            // Count consecutive 'B's
            while (j < n && colors.charAt(j) == 'B') {
                j++;
            }
            bMoves += Math.max(0, j - i - 2);
            i = j;
        }

        return aMoves > bMoves;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String colors1 = "AAABABB";
        String colors2 = "AA";
        String colors3 = "ABBBBBBBAAA";
        String colors4 = "BBBAAAABB";
        
        System.out.println(solution.winnerOfGame(colors1));  // Expected output: true
        System.out.println(solution.winnerOfGame(colors2));  // Expected output: false
        System.out.println(solution.winnerOfGame(colors3));  // Expected output: false
        System.out.println(solution.winnerOfGame(colors4));  // Expected output: true
    }
}

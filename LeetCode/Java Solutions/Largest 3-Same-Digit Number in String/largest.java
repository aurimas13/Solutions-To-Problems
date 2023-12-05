public class Solution {
    public String largestGoodInteger(String num) {
        String maxGood = "";

        for (int i = 0; i < num.length() - 2; i++) {
            // Check if the substring of length 3 has the same character
            if (num.charAt(i) == num.charAt(i + 1) && num.charAt(i) == num.charAt(i + 2)) {
                // Update maxGood if the current substring is greater
                maxGood = max(maxGood, num.substring(i, i + 3));
            }
        }

        return maxGood;
    }

    private String max(String a, String b) {
        return a.compareTo(b) > 0 ? a : b;
    }
}

public class Solution {

    public String longestPalindrome(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }

        int start = 0, end = 0;
        int length = s.length();

        for (int i = 0; i < length; i++) {
            int maxLen1 = getMaxLen(s, i, i); // Assume odd length, try to extend Palindrome as possible
            int maxLen2 = getMaxLen(s, i, i + 1); // Assume even length.
            int maxLen = Math.max(maxLen1, maxLen2);

            if (maxLen > end - start) {
                start = i - (maxLen - 1) / 2;
                end = i + maxLen / 2;
            }
        }

        return s.substring(start, end + 1); // Java's substring function requires end + 1 as the ending index
    }

    private int getMaxLen(String s, int left, int right) {
        int length = s.length();

        while (left >= 0 && right < length && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1; // Subtract 1 from the length since we've previously done an extra add for both pointers
    }
}

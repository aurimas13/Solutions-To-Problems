public class Solution {
    public String largestOddNumber(String num) {
        // Iterate from the end to the beginning
        for (int i = num.length() - 1; i >= 0; i--) {
            if ((num.charAt(i) - '0') % 2 != 0) {
                // Return the substring up to and including the odd digit
                return num.substring(0, i + 1);
            }
        }
        // If no odd digit is found, return an empty string
        return "";
    }
}
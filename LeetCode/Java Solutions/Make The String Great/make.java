public class Solution {
    public String makeGood(String s) {
        StringBuilder stack = new StringBuilder();
        for (char c : s.toCharArray()) {
            int lastCharIndex = stack.length() - 1;
            // Check if the current and last character in the stack form a bad pair
            if (stack.length() > 0 && Math.abs(c - stack.charAt(lastCharIndex)) == 32) {
                stack.deleteCharAt(lastCharIndex); // Remove last character
            } else {
                stack.append(c);
            }
        }
        return stack.toString();
    }
}

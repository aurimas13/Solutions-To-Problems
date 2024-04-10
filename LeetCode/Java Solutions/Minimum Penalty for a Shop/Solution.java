public class Solution {
    public String minRemoveToMakeValid(String s) {
        StringBuilder validString = new StringBuilder();
        int balance = 0;
        
        // First pass: Remove invalid closing parentheses
        for (char c : s.toCharArray()) {
            if (c == '(') {
                balance++;
            } else if (c == ')') {
                if (balance == 0) continue;  // Skip this character
                balance--;
            }
            validString.append(c);
        }
        
        // Second pass: Remove invalid opening parentheses from the end
        StringBuilder result = new StringBuilder();
        for (int i = validString.length() - 1; i >= 0; i--) {
            char c = validString.charAt(i);
            if (c == '(' && balance-- > 0) continue;  // Skip this character
            result.append(c);
        }
        
        return result.reverse().toString();
    }
}

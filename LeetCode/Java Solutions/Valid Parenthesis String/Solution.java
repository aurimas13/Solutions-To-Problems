public class Solution {
<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
+    /**
+     * Returns true if the given string of parentheses is valid.
+     * 
+     * A string S of parentheses is valid if:
+     *   - S is the empty string, or
+     *   - S can be written as AB (A concatenated with B), where A and B are valid strings, or
+     *   - S can be written as (A), where A is a valid string.
+     * 
+     * Given a string s of parentheses, return true if the string is valid.
+     */
    public boolean checkValidString(String s) {
+        // Min balance represents the minimum number of opening parentheses still needed to make a valid string.
+        // Max balance represents the maximum number of opening parentheses that could be left unclosed at any point.
        int minBalance = 0, maxBalance = 0;
+        
+        // Iterate through each character in the input string
        for (char c : s.toCharArray()) {
+            // If the current character is an opening parentheses, increase the minimum and maximum balance by 1.
            if (c == '(') {
                minBalance++;
                maxBalance++;
+            }
+            
+            // If the current character is a closing parentheses, decrease the maximum balance by 1.
+            // If the maximum balance becomes negative, return false because there aren't enough opening parentheses to match the closing parentheses.
+            else if (c == ')') {
-            } else if (c == ')') {
-                minBalance = Math.max(minBalance - 1, 0);
                maxBalance--;
                if (maxBalance < 0) {
                    return false;
                }
+            }
+            
+            // If the current character is a wildcard, decrease the minimum balance by 1.
+            else {  // c == '*'
-            } else {  // c == '*'
                minBalance = Math.max(minBalance - 1, 0);
                maxBalance++;
            }
        }
        
+        // If the minimum balance is 0, the string is valid.
        return minBalance == 0;
    }
+
<<<<<<<  d2ee5536-4bd8-4348-82cd-fcd07f0f0234  >>>>>>>
}

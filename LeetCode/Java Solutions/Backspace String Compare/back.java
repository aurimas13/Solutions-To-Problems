import java.util.Stack;

public class Solution {
    // Helper method to process the string
    private String processString(String str) {
        Stack<Character> stack = new Stack<>();

        // Iterate through each character in the string
        for (char ch : str.toCharArray()) {
            if (ch == '#') {
                // If it's a backspace, we pop the stack (if it's not empty)
                if (!stack.empty()) {
                    stack.pop();
                }
            } else {
                // Otherwise, we push the character into the stack
                stack.push(ch);
            }
        }

        // Build the final string from the stack
        StringBuilder processed = new StringBuilder();
        for (char ch : stack) {
            processed.append(ch);
        }

        return processed.toString();
    }

    public boolean backspaceCompare(String s, String t) {
        // Process both strings and then compare the results
        return processString(s).equals(processString(t));
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test cases
        String[][] testCases = {
            {"ab#c", "ad#c"}, // True
            {"ab##", "c#d#"}, // True
            {"a##c", "#a#c"}, // True
            {"a#c", "b"},     // False
        };

        boolean[] expectedResults = {true, true, true, false};

        for (int i = 0; i < testCases.length; i++) {
            boolean result = solution.backspaceCompare(testCases[i][0], testCases[i][1]);
            if (result != expectedResults[i]) {
                System.out.println("Test case " + i + " failed: expected " + expectedResults[i] + ", got " + result);
            } else {
                System.out.println("Test case " + i + " succeeded");
            }
        }
    }
}

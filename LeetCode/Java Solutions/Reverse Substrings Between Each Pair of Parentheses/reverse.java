import java.util.Stack;

class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == ')') {
                // Pop characters until finding the matching '('
                StringBuilder temp = new StringBuilder();
                while (!stack.isEmpty() && stack.peek() != '(') {
                    temp.append(stack.pop());
                }
                // Pop the '(' from the stack
                stack.pop();
                // Push the reversed string back to the stack
                for (char c : temp.toString().toCharArray()) {
                    stack.push(c);
                }
            } else {
                // Push the current character to the stack
                stack.push(ch);
            }
        }
        
        StringBuilder result = new StringBuilder();
        for (char ch : stack) {
            result.append(ch);
        }
        
        return result.toString();
    }
}

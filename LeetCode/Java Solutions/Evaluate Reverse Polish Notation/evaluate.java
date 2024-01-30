import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                // Pop the last two numbers from the stack
                int num2 = stack.pop();
                int num1 = stack.pop();

                // Evaluate the expression based on the operator
                switch (token) {
                    case "+":
                        stack.push(num1 + num2);
                        break;
                    case "-":
                        stack.push(num1 - num2);
                        break;
                    case "*":
                        stack.push(num1 * num2);
                        break;
                    case "/":
                        stack.push(num1 / num2);  // Truncate towards zero
                        break;
                }
            } else {
                // Push the number onto the stack
                stack.push(Integer.parseInt(token));
            }
        }

        // The final result is the last item in the stack
        return stack.peek();
    }
}

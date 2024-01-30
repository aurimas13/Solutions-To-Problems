Problem description of "Evaluate Reverse Polish Notation" can be found [here](https://leetcode.com/problems/evaluate-division/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Evaluate%20Reverse%20Polish%20Notation/evaluate.java).


To check the solution in terminal first compile Java file as `javac evaluate.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The provided solution uses a stack to evaluate an arithmetic expression in Reverse Polish Notation (RPN). The approach involves iterating through each token in the expression, performing stack operations depending on whether the token is an operand or an operator. When an operator is encountered, the last two operands are popped from the stack, the operation is performed, and the result is pushed back onto the stack. The implementation ensures that the expression is evaluated correctly according to the rules of RPN, and the final result is obtained from the top of the stack. This method is efficient, with a linear time complexity relative to the number of tokens, making it well-suited for evaluating arithmetic expressions in RPN format.
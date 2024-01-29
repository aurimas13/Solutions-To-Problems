import java.util.Stack;

class MyQueue {
    Stack<Integer> stack1;  // Stack for enqueue
    Stack<Integer> stack2;  // Stack for dequeue

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);  // Push element onto stack1
    }
    
    public int pop() {
        move();
        return stack2.pop();  // Pop element from stack2
    }
    
    public int peek() {
        move();
        return stack2.peek();  // Peek element from stack2
    }
    
    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();  // Check if both stacks are empty
    }
    
    private void move() {
        if (stack2.isEmpty()) {  // Move elements from stack1 to stack2 if stack2 is empty
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
    }
}

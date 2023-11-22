import java.util.Queue;
import java.util.LinkedList;

class MyStack {

    Queue<Integer> q1 = new LinkedList<>();  // Primary queue
    Queue<Integer> q2 = new LinkedList<>();  // Secondary queue
    
    // Initialize the stack
    public MyStack() {
    }
    
    // Push an element onto the stack
    public void push(int x) {
        // Add the element to q2
        q2.add(x);
        
        // Transfer all the elements from q1 to q2
        while(!q1.isEmpty()) {
            q2.add(q1.poll());
        }
        
        // Swap the names of q1 and q2
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    // Pop the top element from the stack and return it
    public int pop() {
        return q1.poll();
    }
    
    // Return the top element of the stack
    public int top() {
        return q1.peek();
    }
    
    // Return true if the stack is empty, false otherwise
    public boolean empty() {
        return q1.isEmpty();
    }
}


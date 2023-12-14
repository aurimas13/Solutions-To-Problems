import java.util.*;

// Assuming NestedInteger is provided by the problem, like:
// public interface NestedInteger {
//     public boolean isInteger();
//     public Integer getInteger();
//     public List<NestedInteger> getList();
// }

public class NestedIterator implements Iterator<Integer> {
    // Stack to store elements of type NestedInteger
    private Deque<NestedInteger> stack = new ArrayDeque<>();

    // Constructor initializes the iterator with the nested list
    public NestedIterator(List<NestedInteger> nestedList) {
        // Prepare the stack to iterate from the end of the list to the start
        for (int i = nestedList.size() - 1; i >= 0; i--) {
            stack.push(nestedList.get(i));
        }
    }

    // Method to check if there is the next integer in the nested list
    @Override
    public boolean hasNext() {
        // Make sure the top of the stack is an integer
        // Otherwise, keep popping the nested lists and push their items onto the stack
        while (!stack.isEmpty()) {
            NestedInteger top = stack.peek();
            if (top.isInteger()) {
                return true;
            }
            stack.pop();
            for (int i = top.getList().size() - 1; i >= 0; i--) {
                stack.push(top.getList().get(i));
            }
        }
        return false;
    }

    // Method to return the next integer in the nested list
    @Override
    public Integer next() {
        return stack.pop().getInteger(); // This should be called after hasNext() returns true
    }
}

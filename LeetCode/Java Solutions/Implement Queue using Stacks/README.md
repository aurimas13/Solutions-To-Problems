The problem description of "Implement Queue using Stacks"
can be found [here](https://leetcode.com/problems/implement-queue-using-stacks/description/) while its solution can be found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Implement%20Queue%20using%20Stacks/implement.java).

To check the solution in terminal first compile Java file as `javac implement.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implemetation

The Java solution implements a FIFO queue using two stacks, stack1 for enqueue operations and stack2 for dequeue operations. The key to achieving O(1) amortized time complexity for pop/peek operations lies in lazy transfer of elements from stack1 to stack2, which only occurs when stack2 is empty and a pop/peek operation is requested. This ensures that the elements are in reverse order in stack2, enabling FIFO behavior. The push operation is always O(1) as it simply pushes elements onto stack1. The empty operation checks if both stacks are empty. The overall space complexity is O(n), as it depends on the total number of elements in the queue. This implementation provides an efficient queue operation using stack primitives, suitable for situations where only stack data structures are available.
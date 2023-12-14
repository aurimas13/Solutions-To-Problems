The problem description of "Copy List with Random Pointer" can be found [here](https://leetcode.com/problems/copy-list-with-random-pointer/description/) while the solution is [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Copy%20List%20with%20Random%20Pointer/copy.java).


**Explanation**:

1. We initially check if the head of the list is null, if yes, we return null since the copied list will also be null.
2. We then iterate through the original list and create a duplicate of each node, placing the duplicate node immediately after the original node.
3. The random pointer of each duplicate node is then set by pointing it to the node next to the node that the random pointer of the original node points to.
4. Lastly, we separate the original and duplicate nodes to obtain our deep copied list.

**Implementation**:

Imagine a system that keeps a list of tasks to be done. Each task might have a random pointer indicating some form of relationship with another task, like maybe one task is a sub-task of another or two tasks have some dependency relationship. When the user wants to duplicate a project, they'd want to copy the entire list, preserving the relationships between tasks.
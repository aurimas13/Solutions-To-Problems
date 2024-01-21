import java.util.*;

class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        // Step 1: Find the root (node not a child of any other node)
        Set<Integer> nonRootNodes = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            if (leftChild[i] != -1) nonRootNodes.add(leftChild[i]);
            if (rightChild[i] != -1) nonRootNodes.add(rightChild[i]);
        }
        
        // There should be exactly one node that is not in nonRootNodes set
        if (nonRootNodes.size() != n - 1) return false;
        
        // Identify the root. It's the node not present in nonRootNodes.
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (!nonRootNodes.contains(i)) {
                root = i;
                break;
            }
        }

        // Step 2: Perform a BFS traversal to check for cycles and single parent property.
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (visited.contains(node)) {
                // Cycle detected
                return false;
            }
            visited.add(node);

            // Add children to the queue
            if (leftChild[node] != -1) queue.offer(leftChild[node]);
            if (rightChild[node] != -1) queue.offer(rightChild[node]);
        }

        // If all nodes are visited, it's a valid tree
        return visited.size() == n;
    }
}

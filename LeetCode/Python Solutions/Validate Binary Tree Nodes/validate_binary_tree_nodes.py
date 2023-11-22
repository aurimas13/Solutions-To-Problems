from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        # Step 1: Find the root (the node that is not a child of any other node)
        non_root_nodes = set()
        for i in range(n):
            if leftChild[i] != -1:
                non_root_nodes.add(leftChild[i])
            if rightChild[i] != -1:
                non_root_nodes.add(rightChild[i])

        # There should be exactly one node that is not in the non_root_nodes set
        if len(non_root_nodes) != n - 1:
            return False

        # Identify the root. It's the node not present in non_root_nodes.
        root = -1
        for i in range(n):
            if i not in non_root_nodes:
                root = i
                break

        # Step 2: Perform a BFS traversal to check for cycles and single parent property.
        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                # Cycle detected
                return False
            visited.add(node)

            # Add children to the queue
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        # If all nodes are visited, it's a valid tree
        return len(visited) == n

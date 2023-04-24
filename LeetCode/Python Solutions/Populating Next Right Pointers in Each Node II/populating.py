# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:  # If the root is None, return None
            return None

        # Initialize the level_nodes list with the root node
        level_nodes = [root]

        # Continue the loop until there are no more nodes in the level_nodes list
        while level_nodes:
            # Connect the next pointers of the nodes in the current level
            for i in range(len(level_nodes) - 1):
                level_nodes[i].next = level_nodes[i + 1]

            # Initialize a new list for the next level's nodes
            next_level_nodes = []

            # Iterate through the current level's nodes and add their children to the next_level_nodes list
            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            # Set level_nodes to the next_level_nodes for the next iteration
            level_nodes = next_level_nodes

        return root


# Tests
if __name__ == '__main__':
    # Test case 1
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_7 = Node(7)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.right = node_7

    solution = Solution()
    result = solution.connect(node_1)

    assert result.left.next == node_3
    assert result.left.left.next == node_5
    assert result.left.right.next == node_7
    assert result.left.right.next.next is None

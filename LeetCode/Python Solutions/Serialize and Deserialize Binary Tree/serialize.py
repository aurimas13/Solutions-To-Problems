# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None,"
        return f"{root.val},{self.serialize(root.left)}{self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(node_values):
            val = node_values.pop(0)
            if val == "None":
                return None

            root = TreeNode(int(val))
            root.left = helper(node_values)
            root.right = helper(node_values)
            return root

        node_values = data.split(',')
        root = helper(node_values[:-1])
        return root


def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()

    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Test serialization and deserialization
    serialized = ser.serialize(root)
    deserialized = deser.deserialize(serialized)
    assert inorder_traversal(root) == inorder_traversal(deserialized)


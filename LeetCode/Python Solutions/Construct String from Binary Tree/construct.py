from typing import List, Optional

def serialize(root):
    """Encodes a tree to a single string."""
    if not root:
        return [None]
    serialized_tree = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            serialized_tree.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            serialized_tree.append(None)
    # Remove trailing Nones
    while serialized_tree[-1] is None:
        serialized_tree.pop()
    return serialized_tree


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(root_idx_in_pre, in_start_idx, in_end_idx):
            if in_start_idx > in_end_idx:
                return None

            root = TreeNode(preorder[root_idx_in_pre])
            root_idx_in_in = inorder_map[root.val]

            left_subtree_size = root_idx_in_in - in_start_idx

            root.left = build(root_idx_in_pre + 1, in_start_idx, root_idx_in_in - 1)
            root.right = build(root_idx_in_pre + 1 + left_subtree_size, root_idx_in_in + 1, in_end_idx)
            return root

        N = len(preorder)
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return build(0, 0, N - 1)


# Tests:
if __name__ == '__main__':
    assert serialize(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])) == [3,9,20,None,None,15,7]
    assert serialize(Solution().buildTree([-1], [-1])) == [-1]
    assert serialize(Solution().buildTree([], [])) == [None]
    assert serialize(Solution().buildTree([1,2,3], [3,2,1])) == [1,2,None,3]
    print("All tests passed successfully.")
    
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def areIdentical(root1, root2):
            # Base Case
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False

            # Check fi the data of both roots is same and data of
            # left and right subtrees are also same
            return (root1.val == root2.val and
                    areIdentical(root1.left, root2.left) and
                    areIdentical(root1.right, root2.right)
                    )

        # Base Case
        if subRoot is None:
            return True

        if root is None:
            return False

        # Check the tree with root as current node
        if (areIdentical(root, subRoot)):
            return True

        # IF the tree with root as current node doesn't match
        # then try left and right subtree one by one
        return Solution().isSubtree(root.left, subRoot) or Solution().isSubtree(root.right, subRoot)


# OR

#         # Base cases
#         if not root and not subRoot: return True
#         if not root or not subRoot: return False
#         if not root.left and not root.right:
#             if root.val==subRoot.val and not subRoot.left and not subRoot.right:
#                 return True
#             return False

#         # Search decendant until (sub of root).val=subroot.val
#         # then check if after this
#         # all nodes are identical before reaching none
#         def isSame(root, subRoot):
#             if not root and not subRoot: return True
#             if not root or not subRoot: return False
#             if not root.left and not root.right:
#                 if root.val==subRoot.val and not subRoot.left and not subRoot.right:
#                     return True
#                 return False

#             # still has decendant
#             left = isSame(root.left, subRoot.left)
#             right = isSame(root.right, subRoot.right)
#             return root.val==subRoot.val and left and right

#         left = self.isSubtree(root.left, subRoot)
#         right = self.isSubtree(root.right, subRoot)
#         return isSame(root, subRoot) or left or right


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    Solve = Instant.isSubtree(root, subRoot) #  root representing a list of [3,4,5,1,2], subRoot representing a list of [4,1,2] -> true
    print(Solve)
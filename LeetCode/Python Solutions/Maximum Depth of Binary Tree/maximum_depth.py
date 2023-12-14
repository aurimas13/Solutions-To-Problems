def fromlist(values):
    def create(it):
        value = next(it)
        return None if value is None else TreeNode(value)

    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nextlevel = [root]
    try:
        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                if node:
                    node.left = create(it)
                    node.right = create(it)
                    nextlevel += [node.left, node.right]

    except StopIteration:
        return root
    raise ValueError("Invalid list")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# # or
#
# stack = []
# if root is not None:
#     stack.append((1, root))
#
# depth = 0
# while stack != []:
#     current_depth, root = stack.pop()
#     if root is not None:
#         depth = max(depth, current_depth)
#         stack.append((current_depth + 1, root.left))
#         stack.append((current_depth + 1, root.right))
#
# return depth


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxDepth(fromlist([3,9,20,None,None,15,7])) #  fromlist([3,9,20,None,None,15,7]) -> 3 | fromlist([1,None,2]) -> 2
    print(Solve)

from typing import Optional
from collections import deque


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


class Solution(TreeNode):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

        # # or
        #
        # def check(p, q):
        #     # if both are None
        #     if not p and not q:
        #         return True
        #     # one of p and q is None
        #     if not q or not p:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return True
        #
        # deq = deque([(p, q), ])
        # while deq:
        #     p, q = deq.popleft()
        #     if not check(p, q):
        #         return False
        #
        #     if p:
        #         deq.appendleft((p.left, q.left))
        #         deq.append((p.right, q.right))
        #
        # return True


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isSameTree(fromlist([1,2]), fromlist([1,None,2])) #fromlist([1,2,3]), fromlist([1,2,3]) -> true | fromlist([1,2]), fromlist([1,None,2]) -> false
    print(Solve)

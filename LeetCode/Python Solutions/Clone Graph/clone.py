"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = set()
        stack = []
        cloned = {}
        stack.append(node)
        while stack:
            cur = stack.pop()
            if cur.val in visited:
                continue
            visited.add(cur.val)
            if cur.val not in cloned:
                cloned[cur.val] = Node(cur.val, [])
            clone = cloned[cur.val]
            for n in cur.neighbors:
                if n.val not in cloned:
                    cloned[n.val] = Node(n.val, [])
                clone.neighbors.append(cloned[n.val])
                if n.val not in visited:
                    stack.append(n)
        return cloned[node.val]

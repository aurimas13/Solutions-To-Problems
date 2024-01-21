# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


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
    

# Tests:
def test_cloneGraph():
    s = Solution()

    # Test case 1: Single node with no neighbors
    n1 = Node(1)
    assert s.cloneGraph(n1).val == 1
    assert s.cloneGraph(n1).neighbors == []

    # Test case 2: Two nodes connected
    n2 = Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    cloned_n1 = s.cloneGraph(n1)
    assert cloned_n1.val == 1
    assert len(cloned_n1.neighbors) == 1
    assert cloned_n1.neighbors[0].val == 2

    # Test case 3: A graph with a cycle
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors.append(n3)
    n2.neighbors.append(n4)
    n3.neighbors.append(n4)
    n4.neighbors.append(n1)
    cloned_n1 = s.cloneGraph(n1)
    assert cloned_n1.val == 1
    assert len(cloned_n1.neighbors) == 2
    assert sorted([n.val for n in cloned_n1.neighbors]) == [2, 3]

    print("All tests passed!")


if __name__ == '__main__':
    test_cloneGraph()



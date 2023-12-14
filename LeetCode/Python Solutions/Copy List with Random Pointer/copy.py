# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:  # if head is null, return null
            return None

        # Step 1: Create duplicate nodes next to original nodes
        curr = head
        while curr:
            # creating duplicate of the current node
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Adjust the random pointers for all duplicate nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Detach duplicate nodes to form the deep copied list
        old_list = head
        new_list = head.next
        new_head = head.next
        while old_list:
            old_list.next = old_list.next.next
            if new_list.next:
                new_list.next = new_list.next.next
            old_list = old_list.next
            new_list = new_list.next

        return new_head
